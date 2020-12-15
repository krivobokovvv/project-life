import mistune
from markdown import markdown

md = """
# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6

- 1
- 2
- 3

# Header 1

**sfsfdfsdfsdsd** ```sd``` fs s fs fsfsd

---

> def test():
>     pass


```
def test():
   pass
```

1. 1
1. 2
1. 3

Header 1
========

Header 2
---------
"""

html = mistune.html(md)
open('mistune.html', 'w').write(html)

html = markdown(md)
open('markdown.html', 'w').write(html)

import marko
html = marko.convert(md)
open('marko.html', 'w').write(html)
