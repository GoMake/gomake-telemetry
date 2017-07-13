import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF

import numpy as np
import pandas as pd
import os
from mailer import sendEmail

def get_input_fileName():
	global fileName
	fileName = input('Enter input csv name in single quotes with eg  MAVERICK20160620: ')
	fileName = fileName + '.csv'
	print(fileName + ' will be used for charts')


def set_key(axis,key): 
	print key
	if (axis == 'x'):
	   global x_axis_key 
	   x_axis_key = key
	else:
	   global y_axis_key 
	   y_axis_key = key


def get_axis_key(axis):
    print("""
    1.Temperature
    2.Barometer
    3.Sound
    4.Altitude
    """)
    print fileName
    ans=True
    while ans:			
	  	ans=input('What key would you like on '+ axis +' axis? . Note - Enclose it in single quotes: ')
	  	if ans=='1':
	  		set_key(axis,'Temperature')
	  		ans = False
	  	elif ans=="2":
			set_key(axis,'Barometer')
	  		ans = False
		elif ans=="3":
		    set_key(axis,'Sound')
		    ans = False
		elif ans=="4":
			set_key(axis,'Altitude')
	  		ans = False
		else:
			print("\n Not Valid Choice Try again")


def get_up_down_rows():
	global df,x_up_rows,y_up_rows, x_down_rows,y_down_rows
	os.chdir('outputs')
	df = pd.read_csv(fileName, sep='\s*,\s*',header=0, encoding='ascii', engine='python')
	max_row = np.argmax(df[x_axis_key].values)
	size = df[x_axis_key].size
	x_up_rows = df[x_axis_key].values[slice(0,max_row)]
	y_up_rows = df[y_axis_key].values[slice(0,max_row)]
	x_down_rows = df[x_axis_key].values[slice(max_row+1,size)]
	y_down_rows = df[y_axis_key].values[slice(max_row+1,size)]


def plot_lines(direction,x_rows,y_rows):
    trace1 = go.Scatter(x=x_rows, y=y_rows, # Data
    mode='lines', name=y_axis_key # Additional options
                   ) 
    title = 'Going' + direction + x_axis_key + 'VS' + y_axis_key
    layout = go.Layout(title=title,
    xaxis=dict(
        title= x_axis_key,
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title=y_axis_key,
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
                   plot_bgcolor='rgb(230, 230,230)')
    fig = go.Figure(data=[trace1], layout=layout)

    # Plot data in the notebook
    url = py.plot(fig, filename=fileName + '-' + title)
    subject = 'Graph Report for ' + fileName + '-' + title
    sendEmail(url,subject)


get_input_fileName()
get_axis_key('x')
get_axis_key('y')
get_up_down_rows()
plot_lines('Up',x_up_rows,y_up_rows)
plot_lines('Down',x_down_rows,y_down_rows)