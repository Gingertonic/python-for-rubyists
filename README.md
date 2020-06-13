# Python for Rubyists
https://www.python.org/
1991 by Guido van Rossum (vs 1995 by Yukihiro Matsumoto)


## How to interact
### Interactive Shell
- like `irb`
- `python` (default install, usually 2.7 on Mac)
- `python3` if you have 3.x.x installed
- IDLE (Applications/Python 3.x.x/IDLE)

- Check current version with `python3 --version` - you want python3 (not Mac default install)
- If needed, install most current from `https://www.python.org/`

### Virtual Environment
- Make virtual env to encapsulate your version, all your installed libs etc
`python3 -m venv <make-a-name-here>`
- Your command prompt will show the name of your env if you are in it
- If not in the env, in VS code you can right click in a .py file and select 'Run python file in terminal' to re-enter

## Datatypes
See examples in /datatypes

## Formatting, Variables & Methods
See examples in /formatting

## OO
See examples in /oo

## Libraries & Debugging
See examples in /libs
- Install libs with pip package manager `pip install <package-name>`
- Debug with `breakpoint()` - triggers import of `pdb` and inserts breakpoint

## Web Frameworks
- Sinatra vs. Flask (vs. Express)
- Rails vs. Django
See flask API example in /web-frameworks
    - run `python3 web-frameworks/my_flask.py` to start server
    - run `open cat_app_client/index.html` to open front-end in browser

## Python specialisms
- Number manipulation => Data Science
See examples in /data
