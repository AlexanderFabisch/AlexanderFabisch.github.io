Title: Slither
Date: 2017-01-20 01:00
Category: Blog
Summary: A private replacement for online training logs.

All the commercial services that allow you to record your sport activities
like [Polar Flow](https://flow.polar.com/),
[Runtastic](https://www.runtastic.com/),
[Endomondo](https://www.endomondo.com/),
[Runkeeper](https://runkeeper.com),
[Strava](https://www.strava.com/),
[Google Fit](https://fit.google.com/),
or whatever store your data on some server which you cannot control.
You do not know what they use the data for and you cannot write your own
tools to analyze your own data.

This is the reason why I wanted to develop a small tool that can be modified
easily to fit my needs and stores the data on my computer. All features
that are important to me are now implemented:

* add and edit activities manually
* import TCX files
* detailed view: plot of velocitiy and heartrate, map that shows the path, pace, best splits
* personal records
* calendar view
* summary of weeks, months, years

It was very simple to implement the application with Python. I have a database
to which I communicate with [SQLAlchemy](http://www.sqlalchemy.org/), the
GUI is written with PyQt, the map is rendered with
[Leaflet](http://leafletjs.com/) and
[OpenStreetMap](https://www.openstreetmap.org). I use
[Matplotlib](http://matplotlib.org/) for plotting. Parsing XML files is very
easy with [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/).

The result can be seen here:

<img width="480" height="360" src="https://raw.githubusercontent.com/AlexanderFabisch/slither/master/doc/source/_static/slither.png" />

The code is available on [github](https://github.com/AlexanderFabisch/slither).
