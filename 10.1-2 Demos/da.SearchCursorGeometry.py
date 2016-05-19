

import arcpy

arcpy.env.workspace = "C:/Student/PYTH/Database/SanDiego.gdb"

with arcpy.da.SearchCursor("MajorAttractions", ("SHAPE@XY", "SHAPE@")) as cur:
    for row in cur:
        #print "NAME Field: " + row[0] + " ADDR field: " + row[1]
        tXY = row[0]  #returns feature's XY coords as a tuple

        x = tXY[0]  # Get X value from tuple
        y = tXY[1]  # Get Y value from tuple

        geom = row[1]
        type = geom.type
        
        print "XCoord: " + str (x) + " - " + "YCoord is : " + \
              str(y) + " - the geom type is: " + type
        


        

# No need to del the cursor