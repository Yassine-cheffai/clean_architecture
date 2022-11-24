#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fileinfo.fileinfo import FileInfo, Logger
from unittest.mock import patch


def test_init():
    filename = "somefile.ext"
    fi = FileInfo(filename)
    assert fi.filename == filename


def test_init_relative():
    filename = "somefile.ext"
    relative_path = f"../{filename}"
    fi = FileInfo(relative_path)
    assert fi.filename == filename


@patch("os.path.getsize")
@patch("os.path.abspath")
def test_get_info(abspath_mock, getsize_mock):
    filename = "somefile.ext"
    original_path = f"../{filename}"
    fi = FileInfo(original_path)

    test_abspath = "some/abs/path"
    abspath_mock.return_value = test_abspath

    test_size = 1234
    getsize_mock.return_value = test_size

    fi = FileInfo(original_path)
    info = fi.get_info()

    abspath_mock.assert_called_with(original_path)
    getsize_mock.assert_called_with(original_path)
    assert info == (filename, original_path, test_abspath, test_size)


@patch("fileinfo.fileinfo.datetime.datetime")
def test_log(mock_datetime):
    test_now = 123
    test_message = "A test message"
    mock_datetime.now.return_value = test_now

    test_logger = Logger()
    test_logger.log(test_message)
    assert test_logger.messages == [(test_now, test_message)]
