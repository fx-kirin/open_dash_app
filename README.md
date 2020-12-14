# open_dash_app

[![Latest PyPI version](https://img.shields.io/pypi/v/package_name.svg)](https://pypi.python.org/pypi/open_dash_app)

Open dash app in a browser only the port if not currently used.

This will prevent to open a lot of pages if you are using debug option of Plotly Dash app. Normaly, when you using `webbrowser` library to open dash url on startup of Dash app, the url will be opened everytime you save the python file.

## Usage

``` python
import open_dash_app

...

if __name__ == "__main__":
    open_dash_app.open_browser_for_local_dash_app(5050)
    app.run_server(port=5050, debug=True)
```


## Installation

``` sh
pip install open_dash_app
```

### Requirements

## Compatibility

## Licence

## Authors

open_dash_app was written by [fx-kirin](fx.kirin@gmail.com).
