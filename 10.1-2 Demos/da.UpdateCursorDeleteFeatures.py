## da.DeleteCursor : delete

#Set current workspace
arcpy.env.workspace = "C:/Student/PYTH/Database/SanDiego.gdb"

#Create cursor on MajorAttractions feature class
with arcpy.da.UpdateCursor("MajorAttractions", "NAME",
                           '"NAME" = \'ESRI\'') as cur:
    for row in cur:
        cur.deleteRow()

#No need to del row or cur