# -*- coding: utf-8 -*-
import os
import datetime


class FileInfo:
    def __init__(self, path):
        self.original_path = path
        self.filename = os.path.basename(path)

    def get_info(self):
        return (
            self.filename,
            self.original_path,
            os.path.abspath(self.original_path),
            os.path.getsize(self.original_path),
        )


class Logger:
    def __init__(self) -> None:
        self.messages = []

    def log(self, message: str) -> None:
        self.messages.append((datetime.datetime.now(), message))
