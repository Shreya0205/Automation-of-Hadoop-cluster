#!/usr/bin/python2
from bokeh.plotting import figure, output_file, show


x=[1,2,3,4,5]
y=[6,7,2,4,5]

output_file("/webcontent/lines.html")
p=figure(title="hello",x_axis_label='x',y_axis_label='y')
p.line(x,y,legend="Temp",line_width=2)
show(p)
