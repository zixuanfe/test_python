#!/usr/bin/env python
# -*- coding:utf-8 -*-

name = "Eric"

print("Hello " + name + ",would you like to learn some python today?")

print(name.lower())  # 小写
print(name.upper())  # 大写
print(name.title())  # 首字母大写


person = "Albert Einstein"
said = "\"A person who never made a mistake never tried anything new.\""
print(person + " said," + said)


person_name = " xx xx "
print(person_name.lstrip())
print(person_name.rstrip())
print(person_name.strip())
print(person_name + "\n" + person_name + "\n\t" + person_name)
