# Future
Where your geospatial journey may lead and the future of open-source geospatial software.


## Future
There's a lot to learn in the geospatial world, and open source usually requires more knowledge and troubleshooting but ultimately greater control over your data, analysis, outcomes, and visualization. It's a high-risk/high-gain situation! This chapter provides thoughts on where free and open-source software may go and, more importantly, where your learning may lead. Future predictions are always wrong, except where you determine your future. So, take my futuristic suggestions lightly.

Nevertheless, given where the field seems to be headed, I will take a crack at it with a few ideas. Most of these are already happening, but they may not be fully adopted in the mainstream. Luckily for me, executable books are easily updated, so here we go.

1. **Cloud native**. Geocomputation in the cloud is faster than on your own machine and requires fewer storage resources. It's likely that all data, processing, and analysis will go to the cloud or something similar.
2. **Geospatial files**. This is an exciting one, yet despite being mundane, it is necessary. The file structure was changed to geoparquet or more portable, quick indexing files.
3. **Visualization**. Visualization will be Easier, more creative, and possible with fewer lines of code. It's great how flexible R and Python are for creating maps and graphic visualizations, but a scatterplot with 10-20 lines of code (or more) could be much simpler.
4. **Lidar everywhere**. Plus, higher resolution imagery all around, but at a cost
5. **Open-source hardware & software**. Given the pressing biodiversity and climate change crises, there is a growing movement in the tech4wildlife world calling for open-source software and hardware. Accelerating new technology by coupling these will be crucial to resolving pernicious issues such as poaching, emissions reductions, and illegal logging.
6. **Geo data atlas**. Comprehensive, standardized, and regularly updated datasets are available in online libraries. They are centrally located and in a decade-long time series, and they can be imported to your analysis with a link.
7. **Map something mobile**. The most commonly used maps are on your phone, used to drive, locate cafes, and locate your friends. Spatial-based apps that billions of people use will continue to evolve. Open crowd sourcing of data already happens through iNaturalist and Seek, what more could be brought to bear in this realm and bring geospatial analysis to more people, e.g., beyond the niche crowd of geospatial data scientists?
8. **Integration**. Better integration across platforms, languages, and tools.

## Hybrid workflows
Hybrid workflows between paid and open-source software are common, especially where paid offerings fall short or charge too much for analyses or imagery you use infrequently. Analog to geospatial workflows, such as the Marin Forest Health Strategy (see box below), are critical to combine qualitative and quantitative information and maximize the usefulness of geospatial data. Some hybrid workflows are common, e.g., data queries in SQL followed by further analysis or visualization in Leafmap.

```{admonition} Marin Forest Health Strategy
:class: tip
The Marin Forest Health Strategy developed county-wide approaches for all public lands in the Northern California locale. Overarching situation analyses of ecosystems related to Douglas Fir, Bishop Pine, Coast Redwood, Sargent Cypress, and Oak Woodlands initiated the strategy and informed geospatial analyses and strategic restoration initiatives. A complete fire history was developed from historical data and newspaper information then digitized into a series of fire dynamic maps. A fine-scale vegetation map developed by Tukman Geospatial was a critical foundation for nearly all the geospatial analysis and project planning. The strategy is available at One Tam's [Forest Health page](https://www.onetam.org/forest-health) and the geospatial analyses at the [Forest Health Web Map](https://parksconservancy.maps.arcgis.com/apps/instant/media/index.html?appid=283456ad496e4a999e74f9501468261c).
```

## Online
There are several emerging free and open-source online mapping options, some code-based, others allowing you to upload datasets, and others still having an entire system for analysis and planning based on predefined visualization tools. Here are several that are worth checking out:

- [rapid editor](https://rapideditor.org/edit). Rapid editor integrates advanced mapping tools, authoritative geospatial open data, and cutting-edge technology to empower OpenStreetMap mappers at all levels.
- [kepler.gl](https://kepler.gl/). Open-source geospatial analysis tool for large-scale datasets.
- [py.cafe](https://py.cafe/). Run, edit, and share Python apps in your browser.
- [marxan](https://marxansolutions.org). Conservation analysis using Marxan's tried and tested approach to conservation planning. Strong community

## GDAL/PDAL
I didn't cover the Geospatial Data Abstraction Library, or GDAL, in this version because I have only used it a couple of times, one of which completely broke my coding setup and required deleting and reinstalling a Python environment, QGIS, and Anaconda. Hopefully, I won't make the same or use the same scorched earth fix again. Below are several resources to explore these tools.

- Robert Simmon shared an excellent six-part series called [A Gentle Introduction to GDAL](https://medium.com/planet-stories/a-gentle-introduction-to-gdal-part-1-a3253eb96082). In Part 1, the author answers why GDAL and GIS systems are great for analyzing geospatial data. However, most GIS software is expensive, difficult to learn, and won't run on his OS. He says the good news is that GDAL is a free and open-source alternative, broadly supported, constantly updated, and runs on almost any OS. But it is difficult to learn, especially if you're terrified of command lines.
- Joshua Stevens has a convincing deck on using the command line for cartographic workflows [here](https://speakerdeck.com/jscarto/commanding-cartography-take-control-of-faster-more-elegant-workflows-from-the-command-line?slide=39).
- Open Source Options has a [GDAL Python Tutorial](https://www.youtube.com/watch?v=bK-eCFUFgkQ) on YouTube that shows how to use Python and GDAL to read, create, and display raster data.
- [PDAL Tutorial](https://sites.google.com/thewatershedcenter.com/caflclanding/code-tutorials/pdal-tutorials?authuser=0) from the Watershed Research and Training Center. This helps you install the Point Data Abstraction Library, or PDAL, and run it from a container. It does not run you through a sample dataset.
- [pdal.io](https://pdal.io/en/2.7-maintenance/) will help get you started with PADL.
- Spatialised has a nice tutorial on [Lidar processing with PDAL, WMTS, and geobash](https://www.spatialised.net/lidar-and-geobash/) and also a video from FOSS4G Bucharest on [Exploiting PDAL and Entwine in the Wild](https://media.ccc.de/v/bucharest-267-exploiting-pdal-entwine-in-the-wild#t=34).

## Go forth and geospatialify!
The bottom line is to keep learning and practicing your geospatial skills. Try something out, share it, get feedback, and learn! I'm curious to hear about your journeys. Please let me know what you think about the book, what could be added, and your journey in the GitHub discussion connected to the repo where FOSS Geospatial tools are hosted. Thanks!
