# Termblr
By Katie and Michael

## Installation
### Make Virtual Environment
```bash
mkvirtualenv -p `which python3` -a . Termblr
```
```bash
make install
```

## Contributing
### Our Toolchain
* [Py3Tumblr](https://github.com/dianakhuang/pytumblr/tree/diana/python-3-support) - Tumblr API wrapper compatible for Python 3
* [ObjectPath](https://pypi.python.org/pypi/objectpath/) - a specification for sanely querying JSON
    - [ObjectPath](https://github.com/adriank/ObjectPath) Python library
* [urwid](http://urwid.org/) - Console interface toolkit
* [Requests](http://docs.python-requests.org/en/latest/) - handles other web requests
* [lxml](http://lxml.de/) - For the occasional scraping

### Tools still requiring research
* Rendering images into ANSI/ASCII art
* Rendering videos into ANSI/ASCII
* Render audio into 8bit
