"""
根据坐标、位移和角度，计算出新的坐标
"""
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
