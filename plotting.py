from viddetect import df
from bokeh.plotting import figure
from bokeh.io import output_file, show
p = figure(width = 1000, height = 100,x_axis_type = "datetime", title="Motion graph")
q = p.quad(left=df["start"],right=["end"],top=1,bottom=0,color="green")
output_file("graph.html")
show(p)
