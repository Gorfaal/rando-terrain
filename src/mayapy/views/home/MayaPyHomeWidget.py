# Rando Terrain by Mike Knowles
# Base project by Scott Ernst


from PySide import QtGui
from pyglass.widgets.PyGlassWidget import PyGlassWidget
from mayapy.enum.UserConfigEnum import UserConfigEnum
from mayapy.views.home.NimbleStatusElement import NimbleStatusElement
from nimble import cmds
from random import randint

class MayaPyHomeWidget(PyGlassWidget):
    def __init__(self, parent, **kwargs):
        super(MayaPyHomeWidget, self).__init__(parent, **kwargs)
        self._firstView = True
        self._statusBox, statusLayout = self._createElementWidget(self, QtGui.QVBoxLayout, True)
        statusLayout.addStretch()
        self._nimbleStatus = NimbleStatusElement(
            self._statusBox,
            disabled=self.mainWindow.appConfig.get(UserConfigEnum.NIMBLE_TEST_STATUS, True) )
        statusLayout.addWidget(self._nimbleStatus)
        self.sizeDial.setRange(1, 10)
        self.sizeDial.valueChanged.connect(self._sizeChanged)
        self.generateTerrainButton.clicked.connect(self._generateTerrain)
        self.sizes = []
        for n in range(1, 11):
            self.sizes.append(pow(2, n) + 1)
        self._sizeChanged(1)

    def _sizeChanged(self, val):
        self.size = self.sizes[val - 1]
        self.dimensionsLabel.setText(str(self.size) + "x" + str(self.size))

    def _activateWidgetDisplayImpl(self, **kwargs):
        if self._firstView:
            self._nimbleStatus.refresh()
            self._firstView = False

    def _generateTerrain(self):
        cmds.polyPlane(n='terrain', sx=self.size-1, sy=self.size-1, w=self.size, h=self.size)
        shapes = cmds.ls("terrain", sl=True, fl=True)
        self.terrain = shapes[0]
        a = self.setVertexHeight((0, 0), 10)
        b = self.setVertexHeight((self.size - 1, 0), 10)
        c = self.setVertexHeight((0, self.size - 1), 10)
        d = self.setVertexHeight((self.size - 1, self.size - 1), 10)

        average_offset = 50
        length = self.size - 1
        while length >= 2:
            half_length = length / 2
            #square
            for x in range(0, self.size - 1, length):
                for y in range(0, self.size - 1, length):
                    top_left = self.getVertexHeight((x, y))
                    top_right = self.getVertexHeight((x + length, y))
                    bottom_left = self.getVertexHeight((x, y + length))
                    bottom_right = self.getVertexHeight((x + length, y + length))
                    average = (top_left + top_right + bottom_left + bottom_right) / 4
                    offset = randint(-average_offset, average_offset)
                    self.setVertexHeight((x + half_length, y + half_length), average + offset)

            #diamond
            for x in range(0, self.size - 1, half_length):
                for y in range((x + half_length) % length, self.size-1, length):
                    left = self.getVertexHeight(((x - half_length + self.size) % self.size, y))
                    right = self.getVertexHeight(((x + half_length) % self.size, y))
                    top = self.getVertexHeight((x, (y + half_length + self.size) % self.size))
                    bottom = self.getVertexHeight((x, (y + half_length) % self.size))
                    average = (left + right + top + bottom) / 4
                    offset = randint(-average_offset, average_offset)
                    self.setVertexHeight((x, y), average + offset)
            average_offset /= 2
            length /= 2

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
        flat_index = y * self.size + x
        index_string = str(self.terrain)
        index_string += ".pnts["
        index_string += str(flat_index)
        index_string += "]"
        vertex_position = cmds.xform(index_string, query=True, translation=True, worldSpace=True)
        return vertex_position
