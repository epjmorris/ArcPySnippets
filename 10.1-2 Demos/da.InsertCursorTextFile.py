######################################################################
## AddNewRows.py
## Author: Esri Instructor
## Date: <today>
## Purpose:  Read text file of field values, populate existing feature class
##           using da InsertCursor
######################################################################

# Import the ArcPy module and time module
import arcpy

# Set the current workspace path
arcpy.env.workspace = r"C:\Temp\SanDiego.gdb"

# Open text file in read mode
f = file(r"C:\temp\Attractions.txt", "r")
line = f.readline()  # Header line

# Establish da InsertCursor on feature class.
cur = arcpy.da.InsertCursor("MajorAttractions", ("NAME", "ESTAB", "ADDR", "CITYNM", "ZIP", "EMP", "ACRES", "SHAPE@XY"))

# Loop through lines in text file
for line in f.readlines():
    # Obtain list of values from current line
    row = line.split(",")
    print row

    # Strip off end of line character from last item in list
    yVal = row[9]
    yVal.rstrip()

    # float needed for X&Y values, X&Y passed as tuple to SHAPE@XY token
    xyVal = (float(row[8]), float(yVal))
    cur.insertRow((row[1], row[2], row[3], row[4], row[5], row[6], row[7], xyVal))

# Close file and cursor
f.close()
del cur