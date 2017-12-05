"""

Dependency of Top 10 Suppliers on MOD Business

Direct Data Source:
https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/
642042/Excel_tables_relating_to_finance_and_economics_annual_statistical_
bulletin_trade_industry_and_contracts_2017.xls

Cited Data Source:
Defence Economics analysis derived from DBS Finance and Trading Funds data sources

"""

import plotly
import plotly.graph_objs as go

organisation = ["BAE Systems PLC",
                "Babcock International Group PLC",
                "Airbus Group SE",
                "Rolls-Royce Holdings PLC",
                "Lockheed Martin Corporation",
                "Leonardo SpA",
                "QinetiQ Group PLC",
                "General Dynamics Corporation",
                "HP Inc",
                "Serco Group PLC"]

year07 = [20.6, 57.4, 1.5, 6.3, 3.5,
          9.1, 41.2, 1.8, 1.2, 20.1]

year08 = [19.5, 48.1, 1.4, 5.6, 2.5,
          7.8, 35.1, 1.6, 1.3, 15.2]

year09 = [19.2, 46.7, 1.4, 5.7, 2.1,
          5.9, 35.2, 1.2, 1.1, 11.6]

year10 = [15.6, 49.0, 1.4, 4.9, 2.1,
          6.1, 27.7, 1.7, 1.0, 10.9]

year11 = [17.4, 43.8, 1.8, 6.1, 2.3,
          6.0, 29.3, 2.3, 1.0, 10.4]

year12 = [20.2, 44.0, 1.4, 4.8, 2.3,
          6.8, 33.8, 1.8, 1.1, 12.2]

year13 = [20.6, 39.5, 1.8, 5.2, 2.4,
          7.8, 60.0, 1.5, 1.0, 13.0]

year14 = [22.8, 37.2, 1.9, 5.5, 2.6,
          8.0, 68.6, 1.8, 2.1, 16.2]

year15 = [21.9, 37.2, 1.6, 6.0, 2.0,
          7.8, 67.9, 1.3, 1.8, 15.9]

year16 = [20.5, 37.2, 1.5, 5.1, 2.0,
          5.8, 61.7, 1.9, 1.1, 11.7]

xAxis = ["2007/08", "2008/09", "2009/10", "2010/11", "2011/12",
         "2012/13", "2013/14", "2014/15", "2015/16", "2016/17"]

yAxisBAE = []
yAxisBabcock = []
yAxisAirbus = []
yAxisRR = []
yAxisLockheed = []
yAxisLeonardo = []
yAxisQinetiQ = []
yAxisGDC = []
yAxisHP = []
yAxisSerco = []

def RestructureData():
    global yAxisBAE
    global yAxisBabcock
    global yAxisAirbus
    global yAxisRR
    global yAxisLockheed    
    global yAxisLeonardo
    global yAxisQinetiQ
    global yAxisGDC
    global yAxisHP
    global yAxisSerco
    
    yAxisBAE = [year07[0], year08[0], year09[0], year10[0], year11[0],
                year12[0], year13[0], year14[0], year15[0], year16[0]]

    yAxisBabcock = [year07[1], year08[1], year09[1], year10[1], year11[1],
                year12[1], year13[1], year14[1], year15[1], year16[1]]

    yAxisAirbus = [year07[2], year08[2], year09[2], year10[2], year11[2],
                year12[2], year13[2], year14[2], year15[2], year16[2]]

    yAxisRR = [year07[3], year08[3], year09[3], year10[3], year11[3],
                year12[3], year13[3], year14[3], year15[3], year16[3]]

    yAxisLockheed = [year07[4], year08[4], year09[4], year10[4], year11[4],
                year12[4], year13[4], year14[4], year15[4], year16[4]]

    yAxisLeonardo = [year07[5], year08[5], year09[5], year10[5], year11[5],
                year12[5], year13[5], year14[5], year15[5], year16[5]]

    yAxisQinetiQ = [year07[6], year08[6], year09[6], year10[6], year11[6],
                year12[6], year13[6], year14[6], year15[6], year16[6]]

    yAxisGDC = [year07[7], year08[7], year09[7], year10[7], year11[7],
                year12[7], year13[7], year14[7], year15[7], year16[7]]

    yAxisHP  = [year07[8], year08[8], year09[8], year10[8], year11[8],
                year12[8], year13[8], year14[8], year15[8], year16[8]]

    yAxisSerco = [year07[9], year08[9], year09[9], year10[9], year11[9],
                year12[9], year13[9], year14[9], year15[9], year16[9]]

def PlotData():
    trace0 = go.Scatter(
        x = xAxis,
        y = yAxisBAE,
        name = organisation[0],
        line=dict(
            color=('rgb(230, 25, 75)'),
            width=4)
    )
    trace1 = go.Scatter(
        x=xAxis,
        y=yAxisBabcock,
        name=organisation[1],
        line=dict(
            color=('rgb(60, 180, 75)'),
            width=4)
    )
    trace2 = go.Scatter(
        x=xAxis,
        y=yAxisAirbus,
        name=organisation[2],
        line=dict(
            color=('rgb(255, 225, 25)'),
            width=4)
    )
    trace3 = go.Scatter(
        x=xAxis,
        y=yAxisRR,
        name=organisation[3],
        line=dict(
            color=('rgb(0, 130, 200)'),
            width=4)
    )
    trace4 = go.Scatter(
        x=xAxis,
        y=yAxisLockheed,
        name=organisation[4],
        line=dict(
            color=('rgb(245, 130, 48)'),
            width=4)
    )
    trace5 = go.Scatter(
        x=xAxis,
        y=yAxisLeonardo,
        name=organisation[5],
        line=dict(
            color=('rgb(145, 30, 180)'),
            width=4)
    )
    trace6 = go.Scatter(
        x=xAxis,
        y=yAxisQinetiQ,
        name=organisation[6],
        line=dict(
            color=('rgb(70, 240, 240)'),
            width=4)
    )
    trace7 = go.Scatter(
        x=xAxis,
        y=yAxisGDC,
        name=organisation[7],
        line=dict(
            color=('rgb(128, 128, 0)'),
            width=4)
    )
    trace8 = go.Scatter(
        x=xAxis,
        y=yAxisHP,
        name=organisation[8],
        line=dict(
            color=('rgb(128, 0, 0)'),
            width=4)
    )
    trace9 = go.Scatter(
        x=xAxis,
        y=yAxisSerco,
        name=organisation[9],
        line=dict(
            color=('rgb(0, 0, 0)'),
            width=4)
    )

    data = [trace0, trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9]

    # Edit the layout
    layout = dict(title='Dependency of Top 10 Suppliers on MOD Business',
                  xaxis=dict(title='Year'),
                  yaxis=dict(title='MOD Spending as a Percentage of Supplier\'s Global Revenue'),
                  )

    fig = dict(data=data, layout=layout)
    plotly.offline.plot(fig, filename='Top_10_Suppliers_Dependency.html')

RestructureData()
PlotData()