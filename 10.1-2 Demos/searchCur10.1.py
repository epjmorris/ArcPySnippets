import arcpy

arcpy.env.workspace = "C:/Student/PYTH/Database/SanDiego.gdb"

cur = arcpy.da.SearchCursor("MajorAttractions", ("NAME", "ADDR"))
# Iterate through the cursor, print tuple of values
# Tuple matches the field order of the cursor

for row in cur:
    print row[0]		#NAME
    print row[1]		#ADDR


# Need to DEL here as we are not using WITH... AS
del cur, row
