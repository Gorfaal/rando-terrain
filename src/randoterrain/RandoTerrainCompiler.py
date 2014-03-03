# MayaPyCompiler.py
# (C)2013
# Scott Ernst

from pyglass.compile.PyGlassApplicationCompiler import PyGlassApplicationCompiler
from pyglass.compile.SiteLibraryEnum import SiteLibraryEnum
from RandoTerrainApplication import RandoTerrainApplication

#___________________________________________________________________________________________________ MayaPyCompiler
class RandoTerrainCompiler(PyGlassApplicationCompiler):
    """A class for..."""

#===================================================================================================
#                                                                                   G E T / S E T

#___________________________________________________________________________________________________ GS: siteLibraries
    @property
    def siteLibraries(self):
        return [SiteLibraryEnum.PYSIDE]

#___________________________________________________________________________________________________ GS: binPath
    @property
    def binPath(self):
        return ['..', '..', 'bin']

#___________________________________________________________________________________________________ GS: appFilename
    @property
    def appFilename(self):
        return 'RandoTerrain'

#___________________________________________________________________________________________________ GS: appDisplayName
    @property
    def appDisplayName(self):
        return 'RandoTerrain'

#___________________________________________________________________________________________________ GS: applicationClass
    @property
    def applicationClass(self):
        return RandoTerrainApplication

#___________________________________________________________________________________________________ GS: iconPath
    @property
    def iconPath(self):
        return ['apps', 'MayaPy']

####################################################################################################
####################################################################################################

if __name__ == '__main__':
    RandoTerrainCompiler().run()

