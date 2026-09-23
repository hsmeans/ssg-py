from sys import argv

from build import build
from page_generator import generate_page_recursively

build()

basepath = argv[1]

generate_page_recursively("content/", "template.html", "docs/", basepath)
