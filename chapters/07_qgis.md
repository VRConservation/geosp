# QGIS
A powerful desktop GIS software infinitely customizable with plugins

## Background
QGIS is a fantastic alternative to ArcGIS Pro, especially since it's free, updated regularly, and has a supportive community srruonding it. It is a desktop package and has additional packages that come with it for the download such as GRASS GIS that are worth checking out. In fact, QGIS is a challenging tutorial to put together because there are so many resources available to learn its use. This chapter assumes you have downloaded QGIS and have basic knowledge of how to use it. If you do not, see the Introduction to QGIS and Map Academy tutorials listed in the Resources section of this chapter. 

## Sierra species richness
For this tutorial, we'll examine species richness by hexagon, known as tessellation, in the Sierra Nevada, California. Make sure you are regularly saving the project by typing control/command S or Project/Save.

### Workflow
We will follow the following workflow to examine species richness:

1. Add data
2. Style layers
3. Create and clip grid: Processing toolbox
4. Run summary statistics and style
5. Create layout or export to web

### Add data
1. If you haven't already installed the QuickMapServices plugin, go to Plugins/Not installed, look for QuickMapServices and select Install Plugin. In QMS search for Dark Matter and click Add to add it as a basemap.
2. Go to the [Biodiviersity Conservation](https://rrk.sdsc.edu/sierra.html#bio_conserv) dataset for the California Wildfire Task Force Regional Resource Kits. Under Species Diversity/Wildlife Species Richness click the pull down menu for Raw Data, download then unzip the tif file.
3. Add your downloads folder to favorites in the browser panel by navigating to your downloads, right clicking, and selecting add to favorites. In the favorites at the top of the panel, open downloads, the species richness file, then draft the tif onto the map canvas. It should appear on the map and in your layers:

![wsr_gray](https://i.imgur.com/4mzQ5OI.png)

Let's change the gray color of the raster to something easier to view. In the layers panel click on the Open Layer Styling panel in the upper left corner (or F7) after clicking on the wildlife species richness layer to make it active.

![layers](https://i.imgur.com/E17z13S.png)

This opens the styling panel. Underneath the layer name, click the Singleband gray to Singleband pseudocolor. Then select magma (when you're selecting magma say MAGMA to yourself in a loud, authoritarian Dr. Evil kind of voice).

![pseudocolor](https://i.imgur.com/Kek44Zz.png)

Close the layer styling panel and go back to the Browser locating the ArcGIS Rest Server. Right click and select New Connection. Under name enter Task Force Regions and for url paste: https://services1.arcgis.com/gGHDlz6USftL5Pau/arcgis/rest/services/Forest_Management_Task_Force_Regions/FeatureServer. Click ok to activate.

![task force regions](https://i.imgur.com/VK0e3pM.png)

The url comes from the ArcGIS online metadata page for [Forest Management Task Force Regions](https://www.arcgis.com/home/item.html?id=781f25e4b1a1419d8939b4b54b25433e&sublayer=0). On the page you will see a URL and a copy sign. If you get to the Map Viewer instead of the metadata, click on Information and then paper arrow icon to get to the page to copy the REST server url.

![agol](https://i.imgur.com/duABhsL.jpeg)

For some reason, some links to REST servers do not work at all or do not work the first time you create the connection. It's worth trying to delete and add the server again. 

### Style layers
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

### Attribute table edit
You may notice that there's a polygon to the west in Marin County covering some of Point Reyes National Seashore near Drake's Estero. This seems to be an error in the vector layer from the Task Force. Let's delete it so it doesn't show up in the subsequent analysis. 

Zoom into the polygon by pressing the + icon in the attribute toolbar and using the hand to the left to pan to the location (hover over the icons to get the name of the icon). In the same toolbar click on the info circle with the arrow. This is the Identify Features icon and is useful for clicking on any area of the map to show the layers and information about the pixel you've clicked. Once you've selected Identify Features, click inside the polygon on the map.

The polygon will change color to show it's selected and an Identify Results box will open.

![identify results](https://i.imgur.com/oj9k64N.png)

Values from the attribute table will appear showing the fid, id, polygon values, row and column indices. Note the fid and id numbers are 201. Close that pane and then click the Open Attribute Table (F6) to the right of the Toolbox icon on the attribute toolbar that looks like a table. Make sure the Sierra Clip layer is selected in the Layers panel before clicking the Attribute Table icon.

![attribute table](https://i.imgur.com/EUwvAiw.png)

In the attribute table you will see the different fields for the layer. This is a simple table since it is a series of polygons. Try selecting other layers in your project to see how each attribute table is different. Note the species richness layer will not have an attribute table sine it is a raster layer. However, the richness layer will show you values if you click the Identify Features and show values stored by pixel in the raster. Opening attribute tables is often the best way to get a quick understanding of the data you are analyzing.

Click on the pencil icon in the upper left of the layer to activate editing mode then select the 201 fid/id row by clicking on the row number to the left. It should be row 6.

![attribute table edit mode](https://i.imgur.com/v01H9Lr.png)

Click the delete button on your keyboard, de-select the pencil editor, accept save changes, and close the attribute table. You'll notice the Marin hexagon is gone.

### Summary statistics
Zoom back to Sierra Clip by right clicking the layer and selecting Zoom to layer(s). This will center the map to the the Sierra Clip layer. Select the Sierra Clip layer by left clicking it. Open the Toolbox and start typing Zonal then select Zonal Statistics and make the following changes:

1. Input layer: leave as Sierra Clip.
2. Raster layer: click the arrow and select wildlife species richness.
3. Statistics to calculate: click the 3 dot box to the right and make sure Count, Sum, Mean, and Maximum are checked.
4. Click on the blue arrow in the upper right to go back and then click run.
5. The process may take ~ one minute to run depending on your computer speed. Close the Zonal Stats tool when completed.

A new layer called Zonal Statistics will appear in your layers with a scratch box to the right. Click the box to save the scratch layer:

1. File name: navigate to your project folder and save as Richness Stats.
2. Layer name: Richness Stats and click ok.
3. You should get a layer saved success notification at the top of the map and the gray scratch layer box is gone.
4. You may need to right click on the layer and change the name to Richness Stats to change the name in the Layer panel.

Close the processing toolbox and with the layer selected open the Layer Styling pane:

1. Change Single Symbol to Graduated.
2. Click the arrow next to Value and scroll down to select _mean.
3. Towards the bottom of the panel click the classify button and turn off the Sierra Clip and Sierra Nevada layers in the layers panel

![classify](https://i.imgur.com/z4a2UXp.png)

4. Click on the color ramp and change to Viridis (or if you're feeling the Dr. Evil thing, select Magma!). You're map should look like the following:

![viridis](https://i.imgur.com/ZJK7lOK.png)

If you want more or less classes click the arrows next to Classes below the Symbol/Values/Legend box. To change the type of classification, click next to the Mode button. The default is Equal Count (Quantile) but Natural Breaks (Jenks) or Standard Deviation are often used depending on the data. Try these out with different numbers of classes and see how the map changes. Don't forget to type Save S or Project/Save. Also check out what happens when you select a different field Value from mean. 

In this map you'll notice that higher species richness is aggregated by hexagon in the foothills regions on either side of the Sierra Nevada and the lowest richness is at higher elevations. In the Styling panel under Rendering you can use the slider to decrease the opacity and look underneath the layer. It might be interesting to import a hillshade layer to get a better idea of where each hexagon lies or a lighter OSM basemap to see more reference cities and geography.

Go back to QMS and type hillshade in the search function and add the ESRI world hillshade. With Richness Stats selected, open the Styling pane and try different selections for the Layer blending mode. Multiply and Hard Light seem to back the layer into hillshade best so you can see both layers. This can be an effective visualization tool. If the layer disappears you may need to click on Classify again to re-classify the layer.

### Layout/webmap
We won't go into depth to create a layout for exporting your map but generally the steps are as follows:

1. Go to the Project menu and select New Print Layout.
2. Enter a name for the new layout and click OK.
3. A new window will open with a blank layout.
4. Go to the Layout menu and select Add Map. Click and drag on the layout where you want the map to be.
5. Adjust the scale and position of the map in the layout using the Item Properties panel.
6. To add other elements like a title, legend, scale bar, north arrow etc., use the Add menu on the left side of the layout window.
7. Once you are satisfied with your layout, you can export it as an image, PDF, or SVG using the Layout menu.

Instead of a static layout you may want to export as a web map:

1. Go to the Plugins menu and select Manage and Install Plugins.
2. Search for qgis2web and click Install Plugin.
3. Go to the Web menu, select qgis2web and then Create a web map.
4. Select OpenLayers as the format.
5. Adjust any other settings as needed.
6. Click Export to export the project as an OpenLayers map.
7. The project should open as an html file in your default browser.

## Resources
The Sierra species richness tutorial should give you a flavor of QGIS' capabilities and processing algorithms. To go deeper in your learning and geospatial practice, here are some additional QGIS resources:

- **[QGIS Training Manual](https://docs.qgis.org/3.34/en/docs/training_manual/index.html)**. A comprehensive resource for all use cases of QGIS plus contributed chapters and tutorials. Always a great place to search to find specific answers to problems you face or find a how to.
- **[Spatial Thoughts](https://spatialthoughts.com)**. Free or paid options available with comprehensive [Introduction to QGIS](https://courses.spatialthoughts.com/introduction-to-qgis.html), [Advanced QGIS](https://courses.spatialthoughts.com/advanced-qgis.html), or [Spatial Data Visualization with QGIS](https://courses.spatialthoughts.com/spatial-data-viz.html). The course materials and tutorials are free and have clear instructions and figures to follow each tutorial. 
- **[Map Academy](https://www.youtube.com/@automaticknowledge)**. Everything you need to know about QGIS, usually in short, digestible snippets. Also includes excellent videos on using Aerialod, a path tracing map visualizer using DEM and other data.
- **[Hans Van der Kwast](https://www.youtube.com/@HansvanderKwast)**. Particularly good for QGIS hydrological applications, but also has Lidar, image analysis, and raster analysis.
- **[Burd GIS](https://www.youtube.com/@burdGIS)**. Many practical videos on QGIS.
- **[Geospatial School](https://www.youtube.com/@geospatialschool)**. Great combination of Python and QGIS. They offer full courses at [geospatialschool.com](https://geospatialschool.com/).
