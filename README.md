# GetUTMZone
ArcGIS Script Tool to find the UTM coordinates for all of the features in a feature class and write them into a new column in the same feature class.

### The Tool accepts 2 parameters:
+ The feature class that you want to add the UTM coordinates to
+ The name of the column that will be created to house the UTM coordinates

**NOTE: This script makes a GET request for every record in the feature class that was provided so performance for features class with over 50 features is slowed down.**
