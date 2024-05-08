# Google Earth Engine

**Your intro to geospatial analysis in the cloud**.

## TL;DR
- See the [Cloud-Based Remote Sensing with Google Earth Engine](https://www.eefabook.org/go-to-the-book.html) book or the [GEE Course](https://spatialthoughts.com/courses/google-earth-engine/) from Spatial Thoughts to get started.
GEE's strength is cloud-based analysis, not visualization. For better visualization/cartographic tools, see Chapters 4, 5, and 8.
- See Chapter 4 and [Geemap](https://geemap.org/) for a way to deploy GEE using Python.

## Scenario
You need to do a quick exploratory data analysis of above and below-ground carbon biomass for an area of interest near Lake Tahoe in the Central Sierra, California. A donor has asked you to do this by the end of the week. You go down the hall to the right where the map plotters are, and ask the GIS guy. He peers up above his array of screens, says he's busyworking on a dozen other projects, he might be able to get you something in 2 weeks. He suggests you check out Google Earth Engine.

Yes! You've heard of this, and you think Google Earth will be easy. But when you check out Earth Engine and find a console with an empty map, the required Javascript coding is another universe, let alone language. 

## DIY
This scenario is even if you have a GIS guy down the hall with the defunct plotter. Many of you are too small and can't afford to pay someone or a consultant to conduct your geospatial analysis. How do you DIY it? Free and open source software (FOSS), or FOSS4G when it refers to free and open source geospatial, is readily available, and, much better than a costly yearly subscription fee, it is free. Contrary to popular opinion, it's not that difficult to start. The full code for this example can be found [here](https://code.earthengine.google.com/609ec9275c6c686b4ddd394f520a27a2).

Here's how:

Once you log into [Earth Engine](https://code.earthengine.google.com/), search for 'carbon' in the search bar at the top of the page. Select Global Aboveground and Belowground Carbon Density Maps. In the lower left of the page, select see example: 

![aboveground | 500](https://i.imgur.com/z3xt9WD.png)

That will open a new code editor with the following javascript code:

```javascript
var dataset = ee.ImageCollection('NASA/ORNL/biomass_carbon_density/v1');

var visualization = {
  bands: ['agb'],
  min: -50.0,
  max: 80.0,
  palette: ['d9f0a3', 'addd8e', '78c679', '41ab5d', '238443', '005a32']
};

Map.setCenter(-60.0, 7.0, 4);

Map.addLayer(dataset, visualization, 'Aboveground biomass carbon');
```

 Clicking run will gives you a basic map of aboveground biomass:
 
![](https://i.imgur.com/m7dOCRr.png)

You can zoom in or out and click the layer on or off. Selecting the inspector in the upper right panel will allow you to click on any pixel in the map and get the information from the raster displayed:

![](https://i.imgur.com/LZcLWWh.png)

In this case the Mosaic image has 4 bands related to above and belowground carbon, the latitude, longitude of a point clicked is (-68.16, 1.83) and the pixel size is 10km. Add in the belowground (bgb) carbon with

```javascript
var vis_b = {
  bands: ['bgb'],
  min: -50.0,
  max: 80.0,
  palette: ['D6BCB1', 'AB8574', '784E3D', '3D2216', '26140C', '000000']
};
Map.addLayer(dataset, vis_b, 'Belowground biomass carbon');
```

You can zoom the map out and center to approximately world level by changing line 10 of the code:

```javascript
Map.setCenter(-24.83, 19.88, 2)
```

Hit run or control + enter (windows) or command + enter (mac) to run the new code. Cleaning up the code and adding comments with // to explain what each section does and standard coding practice (the double back slash allows you to add a comment that does not run when the code executes and is equivalent to the hash tag for python). You can comment out any line of code by clicking on the line and typing control/command enter on your keyboard. Reorganization will give you the following code and image:

```javascript
// Add global carbon density map
var dataset = ee.ImageCollection('NASA/ORNL/biomass_carbon_density/v1');

// Add visual parameter variables
var vis_a = {
  bands: ['agb'],
  min: -50.0,
  max: 80.0,
  palette: ['d9f0a3', 'addd8e', '78c679', '41ab5d', '238443', '005a32']
};

var vis_b = {
  bands: ['bgb'],
  min: -50.0,
  max: 80.0,
  palette: ['D6BCB1', 'AB8574', '784E3D', '3D2216', '26140C', '000000']
};

// Center map and add layers
Map.setCenter(-24.83, 19.88, 2);
Map.addLayer(dataset, vis_a, 'Aboveground biomass carbon');
Map.addLayer(dataset, vis_b, 'Belowground biomass carbon');
```
![](https://i.imgur.com/7hkdrV0.png)

Note the belowground now shows up on top--turn it off by clicking the checkmark in the layers tab, or to view it first, reverse the order of the code, e.g., line 22 moved to 21. You can also control visible layers by altering the Map.addLayer function to add the layer but it won't be visible when you run the code:

```javascript
Map.addLayer(dataset, vis_b, 'Belowground biomass carbon', false);
```

## AOI Clip
Getting back to the original request: clip the dataset to an area of interest, in this case around Lake Tahoe. You can clip the map to existing datasets such as Tiger Lines for states or by country. Clipping by specific shape files requires you to upload the vector as a shape file into Earth Engine. This is fiddly and not as easy as dragging/dropping into Arc or QGIS or online resources such as Felt or Earth Blox. We'll keep this to a simple box.

Turn off the map layers and zoom into your area of interest AOI, in this case near Lake Tahoe:

![](https://i.imgur.com/wqAZ3bC.png)

Enter a search in the box at the top of Earth Engine such as 'South Lake Tahoe, CA, USA'. In the map pane, click on the square 'Draw a Rectangle' button highlighted and draft a square in the area

![](https://i.imgur.com/Il9YmB4.png)

This will add a layer in the imports section of the top of your code called geometry (var geometry: Polygon, 4 vertices). I have changed the name by double-clicking the layer name in the code editor to rename it 'bbox' (double-click geometry, type in bbox and hit enter), but you can use the name geometry, remember to change the name from the code offered below from bbox to geometry. Under the dataset variable change the code to the ImageCollection as follows:

```javascript
// Add global carbon density map
var dataset = ee.ImageCollection('NASA/ORNL/biomass_carbon_density/v1')
                    .map(function(image){return image.clip(bbox)});
```

Note the end of the dataset line no longer has a semicolon since the end of the code line is now following the bbox clip. Change the map center and zoom into your bounding box by changing the Map.setCenter function (line 21):

```javascript
// Center map and add layers
Map.setCenter(-120.2348, 38.8744, 9);
```

Alternatively, change the line to Map.centerObject(bbox, 9) for more memorable way to center. In the map pane, hover over Geometry Imports, and unclick bbox. Run the code again to get

![](https://i.imgur.com/u320Y7K.png)

Given the clash of colors for the brown and green carbon, it might help to change the basemap. This can be relatively simple or complicated in Earth Engine. Going to [Snazzy Maps](https://snazzymaps.com/), selecting a basemap you like and copying the javascript can make your work easier. In Snazzy we'll choose simple gray. Adding it to the map adds about 130 lines of code to your map, but don't be scared, just paste it below everything and add a couple of code lines as follows

```javascript
// Change basemap to snazzymaps.com subtle gray
var gray = [
'paste in the lines of javascript code from Snazzy'
]
Map.setOptions('Gray', {gray: gray});
```

Once you hit, enter you will have 'gray' as an additional map option in the middle right portion of your screen to go along with the default 'Map' and 'Satellite' options. Earth Engine has other defaults you can add without a lot of code and can be found [here](https://developers.google.com/earth-engine/tutorials/community/customizing-base-map-styles). Here is what the basemap bar in the upper right of the map pane looks like after adding the gray basemap:

![](https://i.imgur.com/X16YsFz.png)

All together the map now looks like the following (with the belowground layer turned off):

![](https://i.imgur.com/uoXwumv.png)

The full code is [here](https://code.earthengine.google.com/609ec9275c6c686b4ddd394f520a27a2). Congratulations, you've made your first Earth Engine map. Selecting the inspector pane in the top right allows you to click anywhere in the map to get coordinates and carbon values at the pixel level. 

## Geospatial EDA
This type of exploratory data analysis (EDA) is extraordinarily useful to quickly look at large datasets of multiple types of biotic and abiotic data that the Earth Engine Catalog offers. You can search for any set in the catalog, click on sample and get an instantaneous view of the data. In reality, this is almost akin to no-code. It also computes and adds any layer in the cloud, so it doesn't matter how old or slow your computer is, you can run the geospatial computations in the cloud. This is a tremendous advantage, especially for more complex analyses.

For the map we just made, you would likely want to add some additional functionality such as a legend showing carbon levels for each raster dataset and a graph with the range of carbon levels for the bounding box area.

## Resources
There are many resources for getting started to advanced use of Google Earth Engine:

- **Spatial Thoughts, Ujaval Gandhi**. [End-to-End Google Earth Engine](https://courses.spatialthoughts.com/end-to-end-gee.html) provides full course materials starts with setting up the Earth Engine environment and moves into more advanced topics such machine learning and change detection.
- **Remote Sensing with GEE**. If you want to get serious about Google Earth Engine, I highly recommend you read the free online Cloud-Based Remote Sensing with Google Earth Engine [book](https://www.eefabook.org/) by Rebecca Moore et al. This book is worth reading as a remote sensing textbook and guides you through nearly everything from basic to complex using Earth Engine.
- **Awesome-GEE**. An incredible curated list of GEE resources can be found in at the opengeos [Awesome-GEE](https://github.com/opengeos/Awesome-GEE) github repo. This incredible resource has everything from getting started to courses, papers, datasets, and much more. You could lose yourself for days in here!
- **GEE Google Group**. For answers to many other questions the Google Earth Engine Developers [listserv](https://groups.google.com/g/google-earth-engine-developers) is quite useful.
- **Awesome-GEE-Community-Catalog**. Not to be confused with Awesome-GEE is the equally awesome 'treasure-trove' of datasets at [awesome-gee-community-catalog](https://gee-community-catalog.org/). 
