import os
import arcpy
import requests

inFC = arcpy.GetParameterAsText(0)
fieldName = arcpy.GetParameterAsText(1)

# Sample URL https://www.latlong.net/dec2utm.php?lat=51.222220&long=-158.511514
_baseURL = r'https://www.latlong.net/dec2utm.php'
sr = arcpy.SpatialReference(4326)

if fieldName in [f.name for f in arcpy.ListFields(inFC)]:
    raise ValueError('Field {} already exists in the feature class provided.'.format(fieldName))
if int(arcpy.GetCount_management(inFC).getOutput(0)) > 50:
    arcpy.AddMessage('A feature class with more than 50 features may slow down performance.')

arcpy.AddField_management(inFC,fieldName,'TEXT',field_length=255)

with arcpy.da.UpdateCursor(inFC,[fieldName,'SHAPE@XY'],spatial_reference=sr) as curs:
    for row in curs:
        urlParams = {'lat':row[1][1],'long':row[1][0]}
        urlReturn = requests.get(_baseURL,params=urlParams).json()
        utmString = '{} {} {}'.format(urlReturn[0]['easting'],urlReturn[0]['northing'],urlReturn[0]['zone'])
        row[0] = utmString
        curs.updateRow(row)
