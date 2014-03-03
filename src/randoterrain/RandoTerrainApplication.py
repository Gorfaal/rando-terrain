# MayaPyApplication.py
# (C)2013
# Scott Ernst

from pyglass.app.PyGlassApplication import PyGlassApplication

#___________________________________________________________________________________________________ MayaPyApplication
class RandoTerrainApplication(PyGlassApplication):

#===================================================================================================
#                                                                                   G E T / S E T

#___________________________________________________________________________________________________ GS: debugRootResourcePath
    @property
    def debugRootResourcePath(self):
        return ['..', '..', 'resources']

#___________________________________________________________________________________________________ GS: splashScreenUrl
    @property
    def splashScreenUrl(self):
        return 'splashscreen.png'

#___________________________________________________________________________________________________ GS: appID
    @property
    def appID(self):
        return 'RandoTerrain'

#___________________________________________________________________________________________________ GS: appGroupID
    @property
    def appGroupID(self):
        return 'RandoTerrain'

#___________________________________________________________________________________________________ GS: mainWindowClass
    @property
    def mainWindowClass(self):
        from randoterrain.RandoTerrainMainWindow import RandoTerrainMainWindow
        return RandoTerrainMainWindow

####################################################################################################
####################################################################################################

if __name__ == '__main__':
    RandoTerrainApplication().run()
