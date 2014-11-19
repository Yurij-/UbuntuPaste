#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Setup.py
#
# Author: Kevin Hu

from setuptools import setup

setup(name = "UbuntuPaste",
      version = "0.0.1",
      description = "A gadget to paste file to UbuntuPaste from cli",
      author = "Kevin Hu"
      author_email = "hxy9243@gmail.com",
      keywords = "ubuntu pastebin",
      long_description = read("README.md"),
      url = "",
      packages = ["ubuntupaste"],
      packages = {"ubuntupaste": "src/ubuntupaste"},
)
