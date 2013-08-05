#!/usr/bin/env python
# -*- coding: utf-8 -*-


#  http://tajribaty.com/yasser  ~Ghemit Yasser~  ghemit.yasser33311@gmail.com
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  


print 'Salam\nCollective Download v.1.0\n'

url1=raw_input('enter the part of url before numbers :')
url2=raw_input('enter the part of url after numbers :')
i=input('enter first number :')
f=input('enter last number :')
n=input('How many digits? :')
n=n-1
m='0'*n

import sys
import os
from time import gmtime, strftime
namecopy=strftime("%d-%m-%Y_%H-%M-%S", gmtime())

add=raw_input('Do you want to empty the file last and rewrite it? [Y]es :')
if add == 'Y' or 'y' :
	out = open ('last','w')
	out.write('\n')
	out.close()

p=i

print "\n:: Start ...\n"

while p <= f and p <= 9 :
	urlfull=url1+str(m)+str(p)+url2+'\n'
	out = open ('last','a')
	out.write(urlfull)
	out.close()
	p += 01

n=n-1
m='0'*n

while p <= f and p <= 99 :
	urlfull=url1+str(m)+str(p)+url2+'\n'
	out = open ('last','a')
	out.write(urlfull)
	out.close()
	p += 01

n=n-1
m='0'*n

while p <= f and p <= 999 :
	urlfull=url1+str(m)+str(p)+url2+'\n'
	out = open ('last','a')
	out.write(urlfull)
	out.close()
	p += 01

n=n-1
m='0'*n

while p <= f :
	urlfull=url1+str(m)+str(p)+url2+'\n'
	out = open ('last','a')
	out.write(urlfull)
	out.close()
	p += 01

print '\n- Writing '+url1+str(i)+url2+'\n   To :   '+url1+str(p-1)+url2


if sys.platform == 'linux2' :
	os1='cp last out/out_'+namecopy+'.txt'
else :
	os1='copy last out\\out_'+namecopy+'.txt'
os.system(os1) 
print '\n- output file in out folder is : out_'+namecopy+'.txt'

if sys.platform == 'linux2' :
	add=raw_input('\n- Do you want to download this list using wget now ? [Y]es :')
	if add == 'Y' or 'y' :
		os.system('wget -i last') 
