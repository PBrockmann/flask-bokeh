from flask import Flask
from flask import render_template

from bokeh.embed import json_item
from bokeh.plotting import figure

import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('layout.html', )

def make_plot():
    plot = figure(
	plot_width = 400,
	plot_height = 300,
        tools = "pan,wheel_zoom,box_zoom,reset,save",
        toolbar_location = "above",
        active_scroll = "wheel_zoom",
	sizing_mode = "stretch_both" 
	)

    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    y = [2**v for v in x]

    plot.line(x, y, line_width=2)

    return plot

@app.route('/plot')
def plot():
    plot = make_plot()
    return json.dumps(json_item(plot))


if __name__ == '__main__':
        app.run()
