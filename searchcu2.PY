# A script to list district in botswana in ascending order of area
#the list will contain the NAME_1, VARNAME_1 and Shape_Area columns
#from the BWA_amd1 atribute table
#immport the arcpy module
import arcpy
#create a workspace, this is where the data resides
arcpy.env.workspace="C:\Users\cse20-018\Downloads\arcPy_BWA\BWA"
# create variables
shapefile='BWA_adm1.shp'
'''use the searchcursor method. The method has the following syntax
SearchCursor (dataset, {where_clause}, {spatial_reference}, {fields}, {sort_fields})'''
rows=arcpy.SearchCursor(shapefile,"","","NAME_1; VARNAME_1;SHAPE_AREA","SHAPE_AREA A")
# iterate on the list and print the contents of column NAME_1
for row in rows:
	print("{0:10}\t{1:30}\t{2:8.4f}".format(row.NAME_1,row.VARNAME_1,row.Shape_Area))

