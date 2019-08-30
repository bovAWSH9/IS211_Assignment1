#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 1 assignment1_part2.py"""

class Book:
    author = "Jules Verne"
    title = "20,000 Leagues Under the Sea"

    def __init__(self, author, title):
        self.author = author
        self.title = title

    def display(self):
        print(self.title + ",", "written by", self.author + ".")


a = Book("John Steinbeck", "Of Mice and Men")
b = Book("Harper Lee", "To Kill a Mockingbird")

a.display()
b.display()
