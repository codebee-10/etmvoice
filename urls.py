#!/usr/bin/env python
# encoding: utf-8

__all__ = ['urls_pattern']

from controller.VoiceController import VoiceHandler
from controller.VoiceToAudioController import VoiceToAudioHandler

urls_pattern = [
    (r"/", VoiceHandler),
    (r"/tsvoice", VoiceToAudioHandler),
]

