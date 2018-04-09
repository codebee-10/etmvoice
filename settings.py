#!/usr/bin/env python
# encoding: utf-8
from urls import urls_pattern as url_handlers

uimodules = []
DEBUG = False
# the application settings

settings = {
    'cookie_secret': 'etmvo_v1.0',    # TODO: get the real secret
    #'xsrf_cookies': True,
}
