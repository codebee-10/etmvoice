#!/usr/bin/env python
# encoding: utf-8

__all__ = ['urls_pattern']

from controller.VoiceController import (VoiceHandler)

urls_pattern = [
    (r"/", VoiceHandler),
    (r"/tsvoice", VoiceHandler),
]

