# Mike Knowles
# Based on
# MayaPyMainWindow.py
# (C)2013
# Scott Ernst
from PySide import QtGui
from pyglass.windows.PyGlassWindow import PyGlassWindow
from views.home.RandoTerrainHomeWidget import RandoTerrainHomeWidget


class RandoTerrainMainWindow(PyGlassWindow):
    def __init__(self, **kwargs):
        PyGlassWindow.__init__(
            self,
            widgets={
                'home': RandoTerrainHomeWidget, },
            title='rando-terrain',
            **kwargs)

        self.setMinimumSize(1024, 480)
        self.setContentsMargins(0, 0, 0, 0)

        widget = self._createCentralWidget()
        layout = QtGui.QVBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        widget.setLayout(layout)

        self.setActiveWidget('home')
