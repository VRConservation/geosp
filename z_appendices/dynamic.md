---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.4
  kernelspec:
    display_name: spatial
    language: python
    name: python3
---

# Dynamic World
Use Dynamic World to compare land cover change over time.

## Dynamic World, Party Time, Excellent
Dynamic World is a worldwide dataset for landcover at 10m resolution. Using the broad land types from the dataset is an excellent way to examine land use change. The code is adapted from geemap [tutorial 114](https://geemap.org/notebooks/114_dynamic_world/). Bonus!

![Party on](https://cdn.apollo.audio/one/media/620a/4546/edd3/6b2c/268c/2a6b/waynes-world-header.jpg?quality=80&format=jpg&crop=41,0,603,1000&resize=crop)

```python
# Import earth engine geemap and create a map
import ee
import geemap
m = geemap.Map()
m.add_basemap("TERRAIN")
```
Here, we've used the [Polyline tool](https://www.keene.edu/campus/maps/tool/) to create a bounding box in the Chaco region of southeastern Bolivia. Remember, the bbox coordinates require lower left lat lon and upper right lat lon to make a rectangular box.

```python
# Create a region of interest. 
region = m.user_roi
if region is None:
    region = ee.Geometry.BBox(-64.6523439, -25.9007305, -63.1115113, -24.8390856)
m.centerObject(region)
```
Then we'll set the date ranges for before and after image.

```python
# Set the 1st date range
start_date = "2016-01-01"
end_date = "2017-01-01"

# Set the 2nd date range
start_date2 = "2023-01-01"
end_date2 = "2024-01-01"
```

And then create Sentinel and Dynamic World composites.

```python
# Create a Sentinel-2 image composite
image = geemap.dynamic_world_s2(region, start_date, end_date)
vis_params = {"bands": ["B4", "B3", "B2"], "min": 0, "max": 3000}
m.addLayer(image, vis_params, "Sentinel-2 image")

# Create a Sentinel-2 image composite2
image2 = geemap.dynamic_world_s2(region, start_date2, end_date2)
vis_params = {"bands": ["B4", "B3", "B2"], "min": 0, "max": 3000}
m.addLayer(image2, vis_params, "Sentinel-2 image2")
```

```python
# Create Dynamic World land cover composite
landcover = geemap.dynamic_world(region, start_date, end_date, return_type="hillshade")
m.addLayer(landcover, {}, "Land Cover")

# Create Dynamic World land cover composite2
landcover2 = geemap.dynamic_world(region, start_date2, end_date2, return_type="hillshade")
m.addLayer(landcover2, {}, "Land Cover2")
```
To compare the 2016 to the 2024 composite we'll add a swipe split panel.

```python
# Add split panel. Zooming with the split panel sometimes doesn't work
left_layer = geemap.ee_tile_layer(landcover, {}, "Land Cover")
right_layer = geemap.ee_tile_layer(landcover2, {}, "Land Cover2")

m = geemap.Map()
m.split_map(left_layer, right_layer)
```
And then a legend and text.

```python
# Add legend and explanatory text
m.add_legend(title="Dynamic World Land Cover", builtin_legend="Dynamic_World")
text = "2017 (left) and 2024 (right) land cover"
m.add_text(text, fontsize=14, position='bottomleft')
m.centerObject(region)
m
```

![schwing](https://i.imgur.com/jMFTsrB.jpeg)

Schwing! To export the first map as a geotiff use this codeblock:

```python
# Save Dynamic World data in GeoTIFF format
output_path = "landcover.tif"
landcover = geemap.dynamic_world(region, start_date, end_date, return_type="class")
geemap.ee_export_image(landcover, filename=output_path, scale=10, region=region, file_per_band=False)
```

**HALRIGHT!** <br>

![wayne](https://variety.com/wp-content/uploads/2017/02/mike-myers-1.jpg?w=700)
