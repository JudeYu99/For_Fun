# -*- coding: utf-8 -*-
# @Author: chnzhuyu
# @Date:   2021-06-30 16:12:46
# @Last Modified by:   chnzhuyu
# @Last Modified time: 2021-06-30 16:47:02

## Note: for English input, release line 35!

import math

#strs = 'Happy!'
strs = '我爱苏大'
radius = 10

def heart_eq(x, y, cutoff):
	i = x / radius / 1.5
	j = y / radius 
	result = (i**2 + j**2 - 1)**3 - i**2 * j**3
	if result <= 0:
		return True
	else:
		return False

count = 0
result =''

if __name__ == '__main__':
	si = radius * 2
	sj = radius * 4
	for i in range(si, -si, -1):
		for j in range(-sj, sj):
			cutoff = 0.01 + 0.001 * i
			if heart_eq(j, i, cutoff):
				result += strs[count % len(strs)]
				#result += "*"
				count += 1
			else:
				result += '  '
			if j == (sj - 1):
				result += '\n'

	print(result)

