from __future__ import print_function
from sage.all import *
htmlindex = open('index.html','w')
print('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">',file=htmlindex)
print('<html>',file=htmlindex)
print('<head>',file=htmlindex)
print('<title>Exact computation of the n-loop invariants</title>',file=htmlindex)
print('<link rel="STYLESHEET" type="text/css" href="style.css">',file=htmlindex)
print('<!-- <body bgcolor="#f6d5c3"> ',file=htmlindex)
print('     <body bgcolor="#F8ECE0"> -->',file=htmlindex)
print('</head>',file=htmlindex)

print('<li><a href="../../index.html">Parent Directory</a></li>',file=htmlindex)
print('<body bgcolor="#fff2ca">',file=htmlindex)
print('	<ul>',file=htmlindex)
print('	    <table>',file=htmlindex)
print('	      <tr>',file=htmlindex)
print('		<td valign="top">',file=htmlindex)
print('		  <ul>',file=htmlindex)

tetnum=9
till=0
for foo in range(1,till+1):
    print('<li><a href="K%d_%d.txt">K%d_%d</a></li>' %(tetnum,foo,tetnum,foo),file=htmlindex)

print('  		</ul>',file=htmlindex)
print('		</td>',file=htmlindex)
print('	      </tr>',file=htmlindex)
print('	    </table>',file=htmlindex)
print('           </ul>',file=htmlindex)
print('<p>',file=htmlindex)
print('</html>',file=htmlindex)
htmlindex.close()

