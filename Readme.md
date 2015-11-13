<!-- MarkdownTOC -->

- Termblr
    - Installation
    - Application Screenshot
    - Roadmap
    - Contributing

<!-- /MarkdownTOC -->
# Termblr
By Michael Sarfati (michael.sarfati@utoronto.ca), 2015

## Installation
### Make Virtual Environment
```bash
mkvirtualenv -p `which python3` -a . Termblr
```
```bash
make install
```

## Application Screenshot
### Termblr on 2015-11-13
![Alt text](docs/screenshots/Screenshot_2015-11-13_06-02-18.png "Termblr on 2015-11-13")

## Roadmap
### Towards version 1 (Current)
* Use of modular, clean and maintainable design pattern, and standardization of Termblr widgets and user conventions
* Login form, streamlined API key acquisition process
* Dashboard (text and quote posts only)
    - Reblog
    - Create text post (Markdown mode only)
    - Edit text post
    - View info
    - Follow
    - Like
    - Comment
* Automated testing
* Ensure compatibility with Linux, OS X, and Cygwin

### Future plans
* Graceful decay support - Termblr should be able to gracefully decay its color and unicode support in terminals with less and less color range, without losing user functionality
* Rendering of HTML markup
* Rendering of images and video posts into ANSI/ASCII art
* Play audio
    - also render audio into 8bit or midi mode ;-)
* Support for other terminals (Windows console, Powershell, BusyBox, etc.)

## Contributing
### Our Toolchain
* [Py3Tumblr](https://github.com/dianakhuang/pytumblr/tree/diana/python-3-support) - Tumblr API wrapper compatible for Python 3
* [ObjectPath](https://pypi.python.org/pypi/objectpath/) - a specification for sanely querying JSON and Python objects
    - [ObjectPath](https://github.com/adriank/ObjectPath) Python library
* [urwid](http://urwid.org/) - Console interface toolkit
* [Requests](http://docs.python-requests.org/en/latest/) - handles other web requests
* [lxml](http://lxml.de/) - For the occasional scraping

### Tools still requiring research
* Rendering images into ANSI/ASCII art
* Rendering videos into ANSI/ASCII
* Render audio into 8bit
