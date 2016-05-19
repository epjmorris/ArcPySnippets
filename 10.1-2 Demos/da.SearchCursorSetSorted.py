## Script which uses list comprehension!
##
## A list of values is obtained from the CITYNM field
## Unique values from that list are obtained and they
## are then sorted.

import arcpy

arcpy.env.workspace = r"C:\temp/SanDiego.gdb"


# Use SearchCursor with list comprehension to return a
values = [row[0] for row in arcpy.da.SearchCursor("MajorAttractions", ("CITYNM"))]

uniqueValues = set(values)          #Unique values in a list
print uniqueValues

sortedValues = sorted(uniqueValues) #Unique values then sorted

for val in sortedValues:
    print val

