from bokeh.models import ColumnDataSource, Label, LabelSet, Range1d
from bokeh.layouts import layout
from bokeh.models import Div, RangeSlider, Spinner
from bokeh.plotting import figure, show

sht_num = 41035
ch_num = 2

with open ("D:\Ioffe\slowADC\calculations\sht%d\\%d_process_ADC_ch%d_data.txt" %(sht_num, sht_num, ch_num), "r") as file:
    lines = file.readlines()

y = []
x = []

for i in range(1, int(len(lines)/5)):
    line = lines[i*5].split(',')
    x.append(float(line[0]) + 3)

for j in range(1, 11):
    temp = []
    for i in range(1, int(len(lines)/5)):
        line = lines[i*5].split(',')
        temp.append(float(line[j]))
    y.append(temp)


p = figure(title = 'shot %d , ch %d' %(sht_num,ch_num),x_range=(100,250), width=1700, height=1000)
#for i in range(len(y)):
#    p.line(x, y[i], legend_label="poly.%d" %(i+1), line_width=1 )
p.line(x, y[0], legend_label="poly.%d" %(1), line_width=1, line_color = 'red' )
p.line(x, y[1], legend_label="poly.%d" %(2), line_width=1, line_color = 'green' )
p.line(x, y[2], legend_label="poly.%d" %(3), line_width=1, line_color = 'blue' )
p.line(x, y[3], legend_label="poly.%d" %(4), line_width=1, line_color = 'yellow' )
p.line(x, y[4], legend_label="poly.%d" %(5), line_width=1, line_color = 'violet' )
p.line(x, y[5], legend_label="poly.%d" %(6), line_width=1, line_color = 'teal' )
p.line(x, y[6], legend_label="poly.%d" %(7), line_width=1, line_color = 'rosybrown' )
p.line(x, y[7], legend_label="poly.%d" %(8), line_width=1, line_color = 'mediumturquoise' )
p.line(x, y[8], legend_label="poly.%d" %(9), line_width=1, line_color = 'orchid' )
p.line(x, y[9], legend_label="poly.%d" %(10), line_width=1, line_color = 'coral' )


div = Div(
    text="""
          <p>Select the circle's size using this control element:</p>
          """,
    width=200,
    height=30,
)

range_slider = RangeSlider(
    title="Adjust x-axis range", # a title to display above the slider
    start=100,  # set the minimum value for the slider
    end=300,  # set the maximum value for the slider
    step=1,  # increments for the slider
    value=(p.x_range.start, p.x_range.end),  # initial values for slider
    )

range_slider.js_link("value", p.x_range, "start", attr_selector=0)
range_slider.js_link("value", p.x_range, "end", attr_selector=1)

p.yaxis[0].axis_label = 'Intensity,V '
p.xaxis[0].axis_label = 'Time, ms'

layout = layout([
    [range_slider],
    [p]
])


p.legend.location = "top_left"
p.legend.click_policy="hide"

show(layout)

