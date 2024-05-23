# SQL

The language you must learn for geospatial analysis!

## New

I have to admit I'm very new to using SQL for geospatial analysis but I am amazed at how easy it is to learn, how fast it analyzes large datasets, and how critical it is for data analysis. SQL really is the universal database management language, so geospatial aside, if you work with data, you need to learn how to use it.

```{tip}
When you perform a definition query in ArcGIS Pro or a data query in QGIS, SQL runs in the background. In fact, if you use ArcGIS Pro, open it up, double-click on a layer, open the def query function, and note that there's a little switch to convert the GUI to SQL. Create a query, then switch it to SQL to see the translation.
```

Add photo of a def query before and after in Arc (with and w/o SQL)

## DuckDB

We'll use [DuckDB](https://duckdb.org/) for examples in this chapter. The software is easy to install (takes seconds), fast, works seamlessly with many programming languages, including Python, R, and Javascript, and works without fuss. DuckDB also has a spatial extension to perform queries and analysis of geospatial data that we will look at in this chapter.

A special thank you to Quisheng Wu for the DuckDB tutorials/lectures from his [Geog-414 course](https://geog-414.gishub.org/), which has superb tutorials on Python, Earth Engine, DuckDB, and PostGIS.

## Installation

Installation is straightforward: follow the instructions for the command line or Python at the DuckDB installation [page](http://gg.gg/1at9tp).

## Wood processing

Let's move to an example from the University of California's Woody Biomass Utilization Group's Biomass Power Plant [Database](http://gg.gg/1as7ti). First, import the dependencies.

```python
# import dependencies
import duckdb
import leafmap
import pandas as pd
```

Then, connect to the duckdb database and install httpfs and spatial extensions.

```python
# Connect database install httpfs, spatial
con = duckdb.connect()
con.install_extension("httpfs")
con.load_extension("httpfs")
con.install_extension("spatial")
con.load_extension("spatial")
```

Read the sawmill .shp file and create the sawmill table.

```python
# Create sawmill table from shp file and show
con.sql('''
    CREATE TABLE IF NOT EXISTS sawmill as
    SELECT * FROM ST_Read('C:/Users/vance/Downloads/CurrentSawmill/Current_Wood_Facility_Database_Primary_Wood_Processing.shp')
''')
con.table('sawmill')
```

```{tip} Duckdb sql can be run in the command line and through Python as we are doing here. There are several ways to do this, but wrapping the commands in con.sql with parenthesis and two sets of double or single quotes is easier to code and read.

```

![sawmill-all](https://i.imgur.com/ptLCP0F.png)

View the sawmill table schema, then sum # sawmills by county

```python
# View sawmill table schema
con.sql('''
    DESCRIBE sawmill
''')
```

![sawmill-schema](https://i.imgur.com/gM9AJtB.png)

```python
# Sum sawmills by county
con.sql('''
    SELECT County, COUNT(*) as Count
    FROM sawmill
    GROUP BY County
    ORDER BY count DESC
''')
```

![sawmill-county](https://i.imgur.com/GeX2mE6.png)

Import the biomass database, then create the biomass table and show

```python
# Import the Biomass dataset
con.sql("SELECT * FROM ST_Read('C:/Users/vance/Downloads/CurrentBiomass/Current_Wood_Facility_Database_Biomass.shp')")
```

```python
# Create biomass table from the shp file and show
con.sql('''
    CREATE TABLE IF NOT EXISTS biomass as
    SELECT * FROM ST_Read('C:/Users/vance/Downloads/CurrentBiomass/Current_Wood_Facility_Database_Biomass.shp')
''')
con.table('sawmill')
```

View the biomass table schema, then sum the total megawatts of the plants by county, rounding the total to 1 decimal.

```python
# View biomass table schema
con.sql('''
    DESCRIBE biomass
''')
```

```python
# Sum the total MW_Grid by county round to 1 decimal

con.sql('''
    SELECT County, ROUND(SUM(CAST(MW_Grid AS FLOAT)), 1) as Total_MW_Grid
    FROM biomass
    GROUP BY County
    ORDER BY Total_MW_Grid DESC
    LIMIT 15
''')
```

## Large datasets
An advantage of DuckDB is its speed processing large datasets

Examples soon!

## Geospatial datasets
Examples soon!

## Resources

- **[GEOG-414](https://geog-414.gishub.org/book/duckdb/01_duckdb_intro.html)**. The DuckDB portion of the Geography 414 course from Quisheng Wu, UT Knoxville, is a definitive and recommended way to start with DuckDB.
- **[Spatial SQL](https://spatial-sql.com/)**. Matt Forrest's text on using SQL in modern GIS is an excellent reference and starter for using SQL within a spatial context. Although the book could use an edit (many spelling errors) and better organization (figures disconnected from text), everything is in the book that you will need to become a spatial SQL expert.
- **[SQL-QGIS Tip](https://twitter.com/spatialthoughts/status/1774833044396081189)**. You can use the 'Execute SQL' processing algorithm to run SQL queries on ANY vector layer within QGIS. Here's an example of calculating group statistics on a vector layer. This also allows you to run SQL queries in a model.
- **[Mark Litwintschik](https://tech.marksblogg.com/duckdb-gis-spatial-extension.html)**. Mark has a great data and geospatial blog featuring several tutorials running the DuckDB spatial extension.

<!-- 
## Notes
[lonboard](https://github.com/developmentseed/lonboard)

[overture map data](https://docs.overturemaps.org/) is mostly buildings and infrastructure

[query data and load to kepler.gl](https://docs.overturemaps.org/examples/kepler-gl/) using duckdb

[examples page](https://docs.overturemaps.org/examples/#13/47.6/-122.33/0/45) has more with duck

[open geospatial](https://github.com/opengeos/geospatial-data-catalogs) datasets
use the cleaned LEWO sets and upload them to a GitHub page

youtube course from Freecode camp, note the outline: https://www.youtube.com/watch?v=mXW7JHJM34k

[analyze millions of points](https://www.youtube.com/watch?v=ljzpm3Mrw-I) has nice duckdb analysis using h3 and connecting code to cli -->
