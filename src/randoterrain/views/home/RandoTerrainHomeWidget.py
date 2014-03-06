# rando-terrain by Mike Knowles
# Base project by Scott Ernst

from PySide import QtGui

from pyglass.widgets.PyGlassWidget import PyGlassWidget
from randoterrain.enum.UserConfigEnum import UserConfigEnum
from randoterrain.views.home.NimbleStatusElement import NimbleStatusElement
from random import randint
from nimble import cmds
import nimble
nimble.changeKeepAlive(True)

class RandoTerrainHomeWidget(PyGlassWidget):
    def __init__(self, parent, **kwargs):
        super(RandoTerrainHomeWidget, self).__init__(parent, **kwargs)
        self._firstView = True
        self._statusBox, statusLayout = self._createElementWidget(self, QtGui.QVBoxLayout, True)
        statusLayout.addStretch()
        self._nimbleStatus = NimbleStatusElement(
            self._statusBox,
            disabled=self.mainWindow.appConfig.get(UserConfigEnum.NIMBLE_TEST_STATUS, True))
        statusLayout.addWidget(self._nimbleStatus)
        self.magnitudeValLabel.setText('1')
        self.sizeDial.setRange(1, 10)
        self.magnitudeDial.setRange(1, 100)
        self.sizeDial.valueChanged.connect(self._sizeChanged)
        self.magnitudeDial.valueChanged.connect(self._magnitudeChanged)
        self.generateTerrainButton.clicked.connect(self._generateTerrain)
        self.sizes = []
        for n in range(1, 11):
            self.sizes.append(pow(2, n) + 1)
        self._sizeChanged(1)

    def _sizeChanged(self, val):
        self.size = self.sizes[val - 1]
        self.dimensionsLabel.setText(str(self.size) + "x" + str(self.size))

    def _magnitudeChanged(self, val):
        self.magnitude = val
        self.magnitudeValLabel.setText(str(val))

    def _activateWidgetDisplayImpl(self, **kwargs):
        if self._firstView:
            self._nimbleStatus.refresh()
            self._firstView = False

    def _generateTerrain(self):
        cmds.polyPlane(n='terrain', sx=self.size-1, sy=self.size-1, w=self.size, h=self.size)
        shapes = cmds.ls("terrain", sl=True, fl=True)
        self.terrain = shapes[0]

        offset_magnitude = self.magnitude
        self.setVertexHeight((0, 0), randint(-offset_magnitude, offset_magnitude))
        self.setVertexHeight((self.size - 1, 0), randint(-offset_magnitude, offset_magnitude))
        self.setVertexHeight((0, self.size - 1), randint(-offset_magnitude, offset_magnitude))
        self.setVertexHeight((self.size - 1, self.size - 1), randint(-offset_magnitude, offset_magnitude))

        length = self.size - 1
        while length >= 2:
            half_length = length / 2
            for x in range(0, self.size - 1, length):
                for y in range(0, self.size - 1, length):
                    bottom_left = self.getVertexHeight((x, y))
                    bottom_right = self.getVertexHeight((x + length, y))
                    top_left = self.getVertexHeight((x, y + length))
                    top_right = self.getVertexHeight((x + length, y + length))
                    average = (top_left + top_right + bottom_left + bottom_right) / 4
                    offset = randint(-offset_magnitude, offset_magnitude)
                    self.setVertexHeight((x + half_length, y + half_length), average + offset)

            for x in range(0, self.size - 1, half_length):
                for y in range((x + half_length) % length, self.size-1, length):
                    left = self.getVertexHeight(((x - half_length + self.size) % self.size, y))
                    right = self.getVertexHeight(((x + half_length) % self.size, y))
                    top = self.getVertexHeight((x, (y + half_length + self.size) % self.size))
                    bottom = self.getVertexHeight((x, (y - half_length) % self.size))
                    average = (left + right + top + bottom) / 4
                    offset = randint(-offset_magnitude, offset_magnitude)
                    self.setVertexHeight((x, y), average + offset)
            offset_magnitude /= 2
            length /= 2
        print "DONE!"

    def getVertexHeight(self, vertex):
        return self.getVertex(vertex)[1]

    def setVertexHeight(self, vertex, val):
        x, y = vertex
        flat_index = y * self.size + x
        index_string = str(self.terrain)
        index_string += ".pnts["
        index_string += str(flat_index)
        index_string += "]"
        vertex_position = cmds.xform(index_string, query=True, translation=True, worldSpace=True)
        cmds.xform(index_string, t=(vertex_position[0], val, vertex_position[2]), worldSpace=True)

    def getVertex(self, vertex):
        x, y = vertex
        if x * y < self.size * self.size:
            flat_index = y * self.size + x
            index_string = str(self.terrain)
            index_string += ".pnts["
            index_string += str(flat_index)
            index_string += "]"
            vertex_position = cmds.xform(index_string, query=True, translation=True, worldSpace=True)
            return vertex_position

