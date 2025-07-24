import arcpy
import pandas as pd

data = {  # Some sample data to put into the dataframe for testing
  "parcelID": [420, 380, 390],
  "purchaseDate": ["05/22/2001", "01/01/2000", "02/14/2022"]
}

df = pd.DataFrame(data)  # Create a dataframe to test with


def df_to_table(df, name):
    """Receives a pandas dataframe and returns a GIS table in memory"""
    table = str(arcpy.management.CreateTable("memory", name).getOutput(0))  # Create a blank GIS table in memory
    for field in df.columns:  # Add all the fields from the dataframe
        if pd.api.types.is_datetime64_any_dtype(df[field]):  # If the field type is datetime64, add a Date field
            arcpy.management.AddField(table, field, "DATE")
        else:
            arcpy.management.AddField(table, field, "TEXT")
    inputs = list(list(x) for x in zip(*(df[x].values.tolist() for x in df.columns)))  # Create a list of each df row
    with arcpy.da.InsertCursor(table, df.columns) as cursor:  # Insert these lists into the GIS table
        for row in inputs:
            cursor.insertRow(row)
    return table


memory_table = df_to_table(df, "test")  # This is how you call the function

arcpy.management.CopyRows(memory_table, "C:/Data/Test.gdb/TestTable")  # Save the memory_table to disk just for testing
