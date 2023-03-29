# pandas-dataframe-to-gis-table
Takes a pandas dataframe and converts it to an arcpy GIS table entirely in memory

arcpy currently does not allow you to import a dataframe into GIS using arcpy.managment.CopyRows or any other method so we need to get creative. This is a simple function that you can drop right into your code without needing to import anything extra or save anything (like a CSV file) to a disk. If the word 'date' is within a field name it will use the "DATE" field type instead of "TEXT", you can add if statements for "LONG" or "DOUBLE" or any other type you require.
