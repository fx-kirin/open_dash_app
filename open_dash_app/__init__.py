"""open_dash_app - Open dash app in a browser only the port if not currently used."""

__version__ = "0.1.0"
__author__ = "fx-kirin <fx.kirin@gmail.com>"
__all__: list = ["open_browser_for_local_dash_app"]

import socket

import webbrowser


def __is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(("localhost", port)) == 0


def open_browser_for_local_dash_app(port, name=None):
    if not __is_port_in_use(5050):
        if name is not None:
            webbrowser.register("firefox", None)
        webbrowser.open("http://localhost:5050")
