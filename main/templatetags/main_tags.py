from django import template
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _, ngettext_lazy

import datetime

import calendar
from django.utils.html import avoid_wrapping
from django.utils.timezone import is_aware, utc

register = template.Library()


TIME_STRINGS = {
    'year': ngettext_lazy('%d year', '%d years'),
    'month': ngettext_lazy('%d month', '%d months'),
    'week': ngettext_lazy('%d week', '%d weeks'),
    'day': ngettext_lazy('%d day', '%d days'),
    'hour': ngettext_lazy('%d hour', '%d hours'),
    'minute': ngettext_lazy('%d minute', '%d minutes'),
    'second': ngettext_lazy('%d second', '%d seconds'),
    'past-day': _('%s ago'),
    'future-day': _('%s from now'),
}

TIMESINCE_CHUNKS = (
    (60 * 60 * 24 * 365, 'year'),
    (60 * 60 * 24 * 30, 'month'),
    # (60 * 60 * 24 * 7, 'week'),
    (60 * 60 * 24, 'day'),
    (60 * 60, 'hour'),
    (60, 'minute'),
    (1, 'second'),
)


def naturaltime(d, now=None, time_strings=None, depth=2):
    if time_strings is None:
        time_strings = TIME_STRINGS
    if depth <= 0:
        raise ValueError('depth must be greater than 0.')
    # Convert datetime.date to datetime.datetime for comparison.
    if not isinstance(d, datetime.datetime):
        d = datetime.datetime(d.year, d.month, d.day)
    if now and not isinstance(now, datetime.datetime):
        if isinstance(now, datetime.datetime):
            raise TypeError('now must be datetime.')
        else:
            now = datetime.datetime(now.year, now.month, now.day)

    now = now or datetime.datetime.now(utc if is_aware(d) else None)

    if now > d:
        is_future = False
    else:
        is_future = True
        d, now = now, d
    delta = now - d

    # Deal with leapyears by subtracing the number of leapdays
    leapdays = calendar.leapdays(d.year, now.year)
    if leapdays != 0:
        if calendar.isleap(d.year):
            leapdays -= 1
        elif calendar.isleap(now.year):
            leapdays += 1
    delta -= datetime.timedelta(leapdays)

    # ignore microseconds
    since = delta.days * 24 * 60 * 60 + delta.seconds
    result = []
    current_depth = 0
    i = 0
    while i < len(TIMESINCE_CHUNKS) and current_depth < depth:
        seconds, name = TIMESINCE_CHUNKS[i]
        count = since // seconds
        if count == 0:
            pass
        else:
            result.append(avoid_wrapping(time_strings[name] % count))
            since -= seconds * count
            current_depth += 1
        i += 1

    if len(result) == 0:
        return _('now')
    else:
        delta = _(', ').join(result)
        if is_future:
            return time_strings['future-day'] % delta
        else:
            return time_strings['past-day'] % delta


@register.filter('naturaltime', is_safe=True)
def naturaltime_filter(value):
    if not value:
        return ''
    try:
        return naturaltime(value)
    except (TypeError, ValueError):
        return ''


@register.simple_tag
def as_table(model):
    ret = ""
    for field in model._meta.get_fields():
        if field.one_to_many:
            raise Exception()
        elif field.many_to_one:
            r = getattr(model, f'{field.name}')
            ret += f'<tr><td class="name">{field.verbose_name}</td><td class="field"><a href="{r.get_admin_url()}">' + \
                   f'{r}</a></td></td>'
        elif field.many_to_many:
            res = getattr(model, field.name).all()
            first = True
            for r in res:
                if first:
                    ret += f'<tr><td class="name" rowspan={res.__len__()} style="vertical-align:middle">' + \
                           f'{r._meta.verbose_name}</td><td class="field"><a href="{r.get_admin_url()}">{r}</a>' + \
                           '</td></tr>'
                    first = False
                else:
                    ret += f'<tr><td class="field"><a href="{r.get_admin_url()}">{r}</a></td></tr>'
        else:
            r = getattr(model, field.name)
            if isinstance(r, datetime.datetime):
                ret += f'<tr><td class="name">{field.verbose_name}</td><td class="field">{r}<br/>{naturaltime(r)}' + \
                       '</td></td>'
            else:
                ret += f'<tr><td class="name">{field.verbose_name}</td><td class="field">{r}</td></td>'
    return mark_safe(ret)
