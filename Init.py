import FreeCAD, sys
# delete from sys.path for new style module
try:
	FreeCAD._newStyleModule("FCGear")
except AttributeError:
	sys.path.append("/home/lo/.FreeCAD/Mod")