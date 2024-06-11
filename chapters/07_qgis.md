# QGIS
A powerful desktop GIS software infinitely customizable with plugins

## Sierra Nevada Species Richness
QGIS is a challenging tutorial to put together because there are so many resources available. This chapter assumes you have downloaded QGIS and have basic knowledge of how to use it. If you do not, see the Introduction to QGIS and Map Academy tutorials listed in the Resources section of this chapter.

### Workflow
1. Add data


### Add data
1. If you haven't already installed the QuickMapServices plugin, go to Plugins/Not installed, look for QuickMapServices and select Install Plugin. In QMS search for Dark Matter and click Add to add it as a basemap.
2. Go to the [Biodiviersity Conservation](https://rrk.sdsc.edu/sierra.html#bio_conserv) dataset for the California Wildfire Task Force Regional Resource Kits. Under Species Diversity/Wildlife Species Richness click the pull down menu for Raw Data, download then unzip the tif file.
3. Add your downloads folder to favorites in the browser panel by navigating to your downloads, right clicking, and selecting add to favorites. In the favorites at the top of the panel, open downloads, the species richness file, then draft the tif onto the map canvas. It should appear on the map and in your layers:

![wsr_gray](https://i.imgur.com/tJMG7w1.png)

Let's change the gray color of the raster to something easier to view. In the layers panel click on the Open Layer Styling panel in the upper left corner (or F7) after clicking on the wildlife species richness layer to make it active.

![layers](https://i.imgur.com/E17z13S.png)

This opens the styling panel. Underneath the layer name, click the Singleband gray to Singleband pseudocolor. Then select magma (when you're selecting magma say MAGMA to yourself in a loud, authoritarian Dr. Evil kind of voice).

![pseudocolor](https://i.imgur.com/Kek44Zz.png)

Close the layer styling panel and go back to the Browser locating the ArcGIS Rest Server. Right click and select New Connection. Under name enter Task Force Regions and for url paste: https://services1.arcgis.com/gGHDlz6USftL5Pau/arcgis/rest/services/Forest_Management_Task_Force_Regions/FeatureServer. Click ok to activate.

![task force regions](https://i.imgur.com/VK0e3pM.png)

The url comes from the ArcGIS online metadata page for [Forest Management Task Force Regions](https://www.arcgis.com/home/item.html?id=781f25e4b1a1419d8939b4b54b25433e&sublayer=0). On the page you will see a URL and a copy sign. If you get to the Map Viewer instead of the metadata, click on Information and then paper arrow icon to get to the page to copy the REST server url.

![agol](https://i.imgur.com/duABhsL.jpeg)

For some reason, some links to REST servers do not work at all or do not work the first time you create the connection. It's worth trying to delete and add the server again. 

### Layer styling
Now that the Task Force REgions have been added, click the arrow to the left of the new connection and drag the vector layer onto the map window or down to the layers panel. Turn off the species richness raster layer by clicking the eye to the left of the layer name in the layers panel. The task force regions should show up with a random color and outlined in black. The layer should be selected when added, so click on the Open the Layer Styling Panel icon in the upper left of the layer panel (or F7) to re-open the symbology or styling panel.

![tf regions styling](https://i.imgur.com/KKp5U2a.png)

Under Single Symbol click Simple Fill under Fill. Click the arrow next to fill color and select the box for Transparent Fill. You can also play around with the colors to see how they change. In the lower right of the Layer Styling box the box for Live update should be checked and the changes are instantaneous. When you click the Transparent Fill the layer will seem to disappear since the basemap is black. Never fear, it's still there. Click the arrow next to Stroke Color and under Standard colors select white and the regions will appear in white.

![task force white](https://i.imgur.com/V6mgBV5.png)

### Processing toolboxes
Head back to the Layers panel and right click the Task Force Regions layer and select Filter. We're going to filter the vector layer to only show the Sierra Nevada and Cascade Region. This will bring up the Query Builder window:

1. Double click Region in the Fields box in the upper left. "Region" will appear in the Expression box below.
2. Click the = sign in the operators box just above the Expression box. 
3. In the upper right Values box click on Sample bringing up the possible names
4. Double click Sierra - Cascade - Inyo
5. 'Sierra - Cascade - Inyo' will appear in the Expression window below.
6. To make sure the expression is valid click test and the Query Result will say the where clause returned 1 row. Congratulations you just completed a data query. 

![region query](https://i.imgur.com/DrVABtI.png)

Click ok to complete the query and close the box and now only the Sierra Nevada region will show. Right click the layer in the Layers panel, select properties and in the window that opens re-name the layer to Sierra Nevada.

At the top of the QGIS window below the Project, Edit, View windows there is an attribute toolbar:

![attributes toolbar](https://i.imgur.com/qEzv3Gn.png)

Click on the cog icon to open the Processing Toolbox. If you left the Layers Styling panel open, close that to maximize the Toolbox pane. In the search panel type grid and double click on create grid to open the grid tool.

![create grid](https://i.imgur.com/QnOBylo.png)

Fill out the tool with the following:

1. Grid type: Hexagon
2. Grid extent: Click arrow, select Calculate from Layer, select Sierra Nevada

![grid extent](https://i.imgur.com/dYOZL20.png)

3. Horizontal and Vertical spacing enter 10000 meters. If you see degrees as the option change the CRS projection to EPSG:3310 NAD83/California Albers. You may need to change the QGIS settings to default to this projection, which can be a fiddle.
4. Click run. It should take a short time to create and a tessellated grid of hexagons will appear over the area of the Sierra Nevada region. Close the tool window and the processing toolbox.

Open the Layer Styling Pane>Simple Fill>Fill color>Transparent>Stroke Color>Light Blue. Make sure to click on the light blue in the circle and within the triangle click on the corner of the triangle for the color (in this case lower left).

![grid color light blue](https://i.imgur.com/QdizHlz.png)

We need to clip the hexagons outside the Sierra region. Close the Layer Styling Pane and open the Processing Toolbox. Start typing Select by location and double click the toolbox with the same name. Fill out the toolbox with Select features from Grid, Where the features Intersect, By comparing to features from Sierra Nevada.

![select by location](https://i.imgur.com/8Pqf61k.png)

Click run

![select by location map](https://i.imgur.com/tqomvq6.png)

Right click the grid layer>Export>Save Selected features as (not in my screenshot that I have a copy of the grid layer that appears below)

![save selected features as](https://i.imgur.com/qsqCaw2.png)

In the save dialog box enter Format: Geopackage, File Name Sierra Clip (click the 3 dots to right and navigate to the folder where you've saved the project), Layer name: Sierra Clip and click ok. You should get a Layer Export success message at the top of the map window. 

### Attribute table deletion
You may notice that there's a polygon to the west in Marin County covering some of Point Reyes National Seashore near Drake's Estero. This seems to be an error in the vector layer from the Task Force. Let's delete it so it doesn't show up in the subsequent analysis.




## Resources
- **[QGIS Training Manual](https://docs.qgis.org/3.34/en/docs/training_manual/index.html)**. A comprehensive resource for all use cases of QGIS plus contributed chapters and tutorials. Always a great place to search to find specific answers to problems you face or find a how to.
- **Spatial Thoughts**. Free or paid options available with comprehensive [Introduction to QGIS](https://courses.spatialthoughts.com/introduction-to-qgis.html), [Advanced QGIS](https://courses.spatialthoughts.com/advanced-qgis.html), or [Spatial Data Visualization with QGIS](https://courses.spatialthoughts.com/spatial-data-viz.html). The course materials and tutorials are free and have clear instructions and figures to follow each tutorial. 
- **[Map Academy](https://www.youtube.com/@automaticknowledge)**. Everything you need to know about QGIS, usually in short, digestible snippets. Also includes excellent videos on using Aerialod, a path tracing map visualizer using DEM and other data.
- **[Hans Van der Kwast](https://www.youtube.com/@HansvanderKwast)**. Particularly good for QGIS hydrological applications, but also has Lidar, image analysis, and raster analysis.
- **[Burd GIS](https://www.youtube.com/@burdGIS). Many practical videos on QGIS.
- **[Geospatial School](https://www.youtube.com/@geospatialschool). Great combination of Python and QGIS. Also full courses at [geospatialschool.com](https://geospatialschool.com/).
