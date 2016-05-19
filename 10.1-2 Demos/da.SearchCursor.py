

import arcpy

arcpy.env.workspace = "C:/Student/PYTH/Database/SanDiego.gdb"

with arcpy.da.SearchCursor("MajorAttractions", ("NAME", "ADDR")) as cur:
# Iterate through the cursor, print tuple of values
# Tuple matches the field order of the cursor

    for row in cur:
        #print "NAME Field: " + row[0] + " ADDR field: " + row[1]
        print row

# No need to del the cursor