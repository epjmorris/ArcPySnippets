## da.UpdateCursor

#Set current workspace
arcpy.env.workspace = "C:/Student/PYTH/Database/SanDiego.gdb"

#Create cursor on MajorAttractions feature class
with arcpy.da.UpdateCursor("MajorAttractions",
                           ("NAME", "ESTAB"),
                           '"NAME" = \'SAN DIEGO ZOO\'') as cur:
    for row in cur:
        row[0] = "Ed's Zoo"
        cur.updateRow(row)

#No need to del row or cur
