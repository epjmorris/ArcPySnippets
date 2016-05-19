## Search Cursor at Desktop 10.1

import arcpy

arcpy.env.workspace = "C:/Student/PYTH/Database/SanDiego.gdb"

with arcpy.da.SearchCursor("MajorAttractions", ("NAME", "ADDR")) as cur:
# Iterate through the cursor, print tuple of values
# Tuple matches the field order of the cursor

    for row in cur:
        print row[0]		#NAME
        print row[1]		#ADDR

# No need to del the cursor
