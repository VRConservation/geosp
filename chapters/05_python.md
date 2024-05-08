# Python

Python is widely applicable and used in the geospatial community. ArcGIS Pro has a Python package called Arcpy, and QGIS has a package named PYQGIS. However, even though Arcpy is a Python package, it is not easy or intuitive to use. I tried it, read an entire book on it, and struggled using the notebooks, which are slow to load and not easy to link to VS Code.

Then I found Geemap and Leafmap—incredible, user-friendly Python packages developed by Qiusheng Wu and available on GitHub at GISWQS. There are also clear tutorials at leafmap.org and geemap.org and videos at [Open Geospatial Solutions](https://www.youtube.com/@giswqs). Many analyses require only one line of code. Here, geospatial analysis using scripts just clicked for me, and it opened up another world to using Python to analyze data rapidly.

## Getting Started

See the 5.4 Resources for more information.

## Sentinel-2 Data

Let's look at a simple example from a GitHub [gist](https://gist.github.com/alexgleith/dc49156aab4b9270b0a0f145bd7fa0ce) posted by Alex Leith. Open [colab](https://colab.research.google.com/) and click the blue 'New notebook' button.

```{note} 'Uncommenting' a line in Python means removing the hashtag before the command or clicking on the line then clicking control or command plus backslash (/).
```

Install the dependencies:

```python
# Uncomment the line below to install pystac and odc
# pip install pystac-client odc-stac odc-geo
```
Access data and create a bounding box:

```python
# Earth search is managed by Element-84 and provides access to a wide range of data sources
client = Client.open("https://earth-search.aws.element84.com/v1")
collection = "sentinel-2-l2a"

# Create a bounding box centered near New River Lagoon in Tasmania
# The bounding box is lower-left x, lower-left y, upper-right x, upper-right y
bbox = [146.5, -43.6, 146.7, -43.4]
```
Search and load the data:

```python
# Datetime can be a single date, like YEAR, YEAR-MONTH or YEAR-MONTH-DAY
# or a range, like YEAR-MONTH/YEAR-MONTH
datetime = "2023-12"

# Run a lazy-loaded search of the STAC API
search = client.search(collections=[collection], bbox=bbox, datetime=datetime)

# Pass the search results to the load function, which will lazy-load the data
data = load(search.items(), bbox=bbox, groupby="solar_day", chunks={}, crs="EPSG:8857", resolution=10)
```
Visualize it:

```python
# Visualize the data
# Time=2 is an arbitrary time slice picked because there's few clouds
data[["red", "green", "blue"]].isel(time=2).to_array().plot.imshow(vmin=0, vmax=1500)

# Alternately, we could visualise using odc.geo.xr's explore function
# data.isel(time=2).explore(bands=["red", "green", "blue"], vmin=0, vmax=1500)
```
Sentinel-2 true color image:

![](https://i.imgur.com/ea6GCzY.png)

The access and sharing of this code are another example of why free and open-source software is special. The community is willing to share it, and it is reproducible and easily modified to meet your needs. Thanks to Alex Leith for sharing this.

## Geemap
Compared to Javascript, Geemap is a much easier way to access, analyze, and visualize Earth Engine data all within a Python package environment developed by [Quisheng Wu](https://github.com/giswqs).

```{admonition} Getting Started
Watch this [installation video](https://www.youtube.com/watch?v=gyQ6wBqYGks&list=PLAxJ4-o7ZoPeXzIjOJx3vBF0ftKlcYH9J&index=3) followed by this [vs code and github](https://www.youtube.com/watch?v=gyQ6wBqYGks&list=PLAxJ4-o7ZoPeXzIjOJx3vBF0ftKlcYH9J&index=3) video. If you already have an IDE, miniconda, and virtual env's installed, go to the Geemap [installation](https://geemap.org/installation/) page.
```

Let's look at how to visualize the same map from Chapter 2 using Geemap. Open a Jupyter notebook and add the following code block:

```python
# Import geemap and create an interactive map
import ee
import geemap
geemap.ee_initialize()
m = geemap.Map()
m
```
That will give you a generic world map with map widgets:

![](https://i.imgur.com/hKl0roO.png)

In the upper right corner of the map, click the wrench icon, then click the two encircling arrows box (bottom row, middle) to open the Javascript to Python code converter:

![](https://i.imgur.com/XXdWssh.png)

Go to your Earth Engine [code editor](https://code.earthengine.google.com/), open the script from Chapter 2, select all, and paste it into the converter. Click the convert button. The code is copied to the clipboard. Paste it into a new code block and comment out the definition function on lines 4-6:

```python
# Add global carbon density map
dataset = ee.ImageCollection('NASA/ORNL/biomass_carbon_density/v1')

# def func_rif(image)return image.clip(bbox)};: \
#                     .map(function(image){return image.clip(bbox)} \
#                     .map(func_rif)

# Add visual parameter variables
vis_a = {
  'bands': ['agb'],
  'min': -50.0,
  'max': 80.0,
  'palette': ['d9f0a3', 'addd8e', '78c679', '41ab5d', '238443', '005a32']
}

vis_b = {
  'bands': ['bgb'],
  'min': -50.0,
  'max': 80.0,
  'palette': ['D6BCB1', 'AB8574', '784E3D', '3D2216', '26140C', '000000']
}

# Center map and add layers
m.setCenter(-120.2348, 38.8744, 9)
m.addLayer(dataset, vis_a, 'Aboveground biomass carbon')
m.addLayer(dataset, vis_b, 'Belowground biomass carbon')
```
Running that block will give you the following:

![](https://i.imgur.com/uAQ9wBz.jpeg)

If you return to the wrench icon and select the layers icon to the left, you can switch layers on and off

![](https://i.imgur.com/RzJfVjV.png)

Add a new code block and add an area of interest called bbox, short for bounding box:

```{tip} To run the code in a code block, click ctrl/command + enter. To run the code and add a new code block, click alt + enter.
```

```python
# Add an area of interest
bbox = [-121.1874, 38.2931, -119.5262, 39.2884]
bbox = ee.Geometry.Rectangle(bbox)
```
Then clip the carbon raster to the AOI:

```python
# Clip the dataset to the area of interest
aoi = dataset.map(lambda image: image.clip(bbox))
```
Now add the clipped rasters:
```python
# Add the clipped dataset to the map
m.addLayer(aoi, vis_b, 'AOI belowground biomass carbon')
m.addLayer(aoi, vis_a, 'AOI aboveground biomass carbon')
m
```
If you turn off the aboveground and belowground maps, your map will now look like the following, with only the clipped aboveground biomass carbon layer showing:

![](https://i.imgur.com/DDRJeDF.png)

Delete the function from the javascript conversion that you commented out previously in lines 4-6. If you need to keep running and test the map you can turn off the original biomass layers added for the entire globe by changing the center map add map layers to code block to

```python
# Center map and add layers
m.setCenter(-120.2348, 38.8744, 9)
m.addLayer(dataset, vis_a, 'Aboveground biomass carbon', False)
m.addLayer(dataset, vis_b, 'Belowground biomass carbon', False)
```
Adding 'False' after the layer name still adds the layers to the map but turns them off by default. 

```{admonition} Lambda Function
Let's take another look at the lambda function to clip the raster. Lambda functions are similar to other Python functions but are not bound to a name when run. Known as anonymous functions, they are used when you need a one-off function that isn't separately defined. In our case, the Lamda function takes an image, clips it to the bounding box, and returns the clipped image. The map() function, not to be confused with the Map function in Javascript, applies the function to every image in the ImageCollection.
```

## Leafmap
A related Python package worth exploring is [Leafmap](https://leafmap.org/), also developed by Quisheng Wu. Like Geemap, the site has extensive documentation and tutorials. I highly recommend attending one of the workshops, which will guide you through installation, examples, and many use cases.

The tutorials and workshops are supported by notebooks and videos to thoroughly walk you through this fantastic software package. Click on the links provided to run the code in Binder or Colab. If you wanted to run a workshop in VS Code:

1. Click workshops in leafmap.org
2. Select the workshop
3. Select GitHub in the upper right, select examples, then notebooks
4. Click on the notebook you want (*.ipynb)
5. Below history in the upper right of your browser, click on the download raw file button, save it, then click to open it in VS Code. 
6. Alternatively, go straight to the workshop notebooks, such as the [FOSS4G Workshop](https://github.com/opengeos/leafmap/blob/master/examples/workshops/FOSS4G_2021.ipynb).

Before running the code cells, ensure you have Leafmap installed in your environment. For a quick starter guide on how to do this, see the Miniconda/Anaconda section of the FOSS4G workshop.

## Resources

- [Geemap](https://geemap.org/) has a webpage, book, tutorials, API, and much more to support this excellent Python package.
- [Leafmap](https://leafmap.org/) is a Python package for geospatial analysis in a Jupyter environment. It has superb documentation, tutorials, and ease of use.
- [Open Geospatial Solutions](https://github.com/opengeos) hosts many open-source geospatial software projects and datasets.
[Spatial Thoughts](https://spatialthoughts.com), run by Ujaval Gandhi, offers a free course called [Python Foundation for Spatial Analysis](https://courses.spatialthoughts.com/python-foundation.html). The site also offers many other free and paid courses and tutorials for geospatial analysis.
- [Geocomputation with Python](https://py.geocompx.org/) is an open source book inspired by the FOSS4G movement. 
