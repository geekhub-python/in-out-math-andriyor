#!/usr/bin/env python3
time = int(input())
hours = (time // 60) % 24
minutes = time % 60
print(hours, minutes)
