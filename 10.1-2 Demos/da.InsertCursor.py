## InsertCurosr

import arcpy

arcpy.env.workspace = "C:/Student/PYTH/Database/SanDiego.gdb"
try:
    cur = arcpy.da.InsertCursor("MajorAttractions", ("NAME", "SHAPE@XY"))

    #point = arcpy.Point(6336283, 1877913)
    #cur.insertRow(["ESRI", point])

    cur.insertRow(["ESRI", (6336283, 1877913)])
except:
    print "InsertCursor error"
finally:
    del cur
    print "FInally"
    