# SQL
The language you must learn for geospatial analysis!

## New
I have to admit I'm very new to using SQL for geospatial analysis, but am amazed at how easy it is to learn, how fast it analyzes large datasets, and how critical it is for data analysis. SQL really is the universal database management language, so, geospatial aside, if you work with data, you need to learn how to use it. 

```{tip}
Any time you perform a definition query in ArcGIS Pro or a data query in QGIS, SQL is running in the background. In fact, if you use ArcGIS Pro, open it up, double click on a layer, open the def query function and note that there's a little switch to conver the GUI to SQL. Create a query then switch it to SQL to see the translation.
```
Add photo of a def query before and after in Arc (with and w/o SQL)

## DuckDB
We'll use [DuckDB](https://duckdb.org/) for examples in this chapters. The software is easy to install (takes seconds), fast, works seamlessly with many programming languages, including Python, R, and Javascript and just works. DuckDB also has a spatial extension to perform queries and analysis of geospatial data that we will look at in this chapter.

A special thank you to Quisheng Wu for DuckDB tutorials/lectures from his [Geog-414 course](https://geog-414.gishub.org/) that has superb tutorials on Python, Earth Engine, DuckDB and PostGIS.

## Installation
Adapt the installation from the [geog414 duck db page](https://geog-414.gishub.org/book/duckdb/01_duckdb_intro.html#installation)?

## Penguins
OK, we're going to shift to penguins but use Ducks to analyze them. The repo is at the [palmerpenguins](https://github.com/allisonhorst/palmerpenguins/blob/main/README.md) repo on Github. We'll use this in the R chapter as well.

csv files are at inst/extdata/penguins_raw.csv

Maybe not? Get another dataset from Marin? or Canada forests? Might be better to forests.

[lonboard](https://github.com/developmentseed/lonboard)
[overture map data](https://docs.overturemaps.org/) is mostly buildings and infrastructure
    [query data and load to kepler.gl](https://docs.overturemaps.org/examples/kepler-gl/) using duckdb
    [examples page](https://docs.overturemaps.org/examples/#13/47.6/-122.33/0/45) has more with duck


[open geospatial](https://github.com/opengeos/geospatial-data-catalogs) datasets
use the cleaned LEWO sets and upload to a github page

youtube course from freecode camp, note the outline: https://www.youtube.com/watch?v=mXW7JHJM34k