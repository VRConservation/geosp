# Field Surveys
Your guide to open source field surveys

Coming soon!

## Background
Using field surveys to create geospatial data is a common practice, but can require costly hardware, subscriptions for cloud data and syncing. I've found that QField that syncs with QGIS could be great, but the forms are clunky, and the cloud setup is not easy. I got it to work, but didn't like entering the data. ESRI's Survey 123 is a paid software, part of a subscription to Arc or other software. It is very easy to set up and sync data plus you have instant maps of recorded data in the field. Survey 123 was quickest to pinpoint gps location. It comes at a cost, however, but if you do a lot of field surveys, it may be worth it. The data is accessible, after you send it, in the Portal tab of the catalog window. Very seamless.

Even if you do conduct a lot of surveys, the Kobo Toolbox is brilliant. Survey forms are easy to set up and sync to your phone and filling them out in the field is easy. Plus there does not seem to be any limit to storing data or pricing, which is a huge plus. Kobo is used by many humanitarian organizations in the field throughout the world during crises so the software developers here have made it very easy to use. 

## Quick start
1. Sign up for an account at Kobo Toolbox. Download KoboCollect to your phone and sign in.
2. In Kobo toolbox open the forms and add questions then Deploy once it's ready.
3. Sync the survey to your phone (Download form) and make sure it's uploaded and working.
4. In the field, open the Kobo app, click + Start new form and enter the data.
5. When finished collecting go to Ready to send, select all, and send.
6. Back at the your online Kobo account, click the data tab and all the forms you filled out will be there.
7. Download the data as excel, csv, or geojson. I found the excel download best, then converted that file to csv after modifying unnecessary columns. Note that you don't need add date, unique field, time as fields to the form since they are automatically added.
8. Import the csv into a notebook, QGIS, or Kepler to view it.

## SDI
Stand density index is a measure of forest health. The stand density index (SDI) is the calculation of the size (DBH) and number of trees or trees/acre in a stand and calculated with the following equation:

$$ 
\sum_{i=1}^n TPA (DBH/25.4)^{1.6} 
$$

 and where TPA = trees/acre and DBH = diameter breast height {cite}`north`; {cite}`woodall`; {cite}`reineke`. This SDI formula uses the summation method, sums individual tree diameters rather than the quadratic mean diameter common in the original equation and can be applied to uneven-age stands ({cite}`north`; {cite}`shaw`).

SDI is used by foresters and ecologists and can be used as a relative measure of how crowded a stand is, show competition between trees, or as an overall measure of forest health {cite}`north`.

## Methodology
To examine forest health in a local forest stand, I measured trees > 30 cm in dbh circumference within 500 m<sup>2</sup> plots at the forested areas randomly sampled from the New Forest National Park, United Kingdom. The sample data shown is from the first three measured plots at Norleywood Enclosure.

## Field data
{numref}`start` shows the Kobo Collect start screens. Before you travel to the field, make sure to click on Download Form so you have the survey uploaded to your phone. 

```{figure} /figures/survey/start.png
:height: 400px
:name: start
Kobo Collect start screens.
```

Click + Start new form at the top of the screen, click on the survey name which brings up the first data entry point. I this case it's the location screen shown in {numref}`location`. 

```{figure} /figures/survey/location.png
:height: 400px
:name: location
Location screens.
```
Click Start GeoPoint. The app will start searching for location and give you a confirmation once it gets to 5m or less as shown in the right two screenshots of {numref}`location`. It may take a few seconds. If it's taking some time you may need to point the phone towards open sky. Click next and proceed to the remainder of the data entry ({numref}`forms`).

```{figure} /figures/survey/forms.png
:height: 400px
:name: forms
Survey form screens.
```
It is worth keeping questions and answers brief in each section. Note, that I just put short common names for tree species in the order of their abundance to make filling out the species section easier. Once you've completed the forms you'll be prompted to finalize the form. ({numref}`send`)

```{figure} /figures/survey/send.png
:height: 400px
:name: send
Send screens.
```
You'll be sent back to the home screen each time. Once you're finished with the site or the day's entries, click Ready to send, Select All (at the bottom left), and Send Selected. You'll get an Upload Results/Successful submission message.

Back in the Kobo Toolbox online, click on Data table where you'll be able to view, sort, and edit everything you collected as shown in {numref}`data`.

```{figure} /figures/survey/data.png
:height: 400px
:name: data
KoboToolbox Data/Table tab.
```
If you select the Reports tab you'll get descriptive statistics for each question of the survey. Although this section allows you to create custom reports, it doesn't let you change information, axes, or build in any analysis but it's still pretty useful for an at-a-glance of your data ({numref}`report`).

```{figure} /figures/survey/report.png
:height: 400px
:name: pics
KoboToolbox Data/Report tab.
```

Clicking the Gallery gives you all of the photos you took in sequential order. You can download and save each one by clicking on it. Look at those beautiful tree trunks in the forest ({numref}`pics`)!

```{figure} /figures/survey/pics.png
:height: 400px
:name: pics
KoboToolbox Data/Gallery tab.
```

The Downloads tab does 'exactly what it says on the tin' as some English folks are wont to say. I downloaded the data first as an excel sheet, edited it, then saved as a CSV that's in the repo under /test/norley2.csv. Make sure you change the lat lon columns to a clear name such as Latitude, Longitude to make them easier to pick up with the software you use. 

## Visualization
I didn't completely figure out the geojson download. It was a bit clunky in that it converts the data to geojoson and opens it in a web browser instead of downloading as a geojson file. The coding looked correct, however.

You can then upload and analyze data using Python libraries, QGIS, or other software. If you add via QGIS:

1. Click on the Data Source Manager (or control/command L, or Layer/Add Layer/Add Delimited Text Layer). Make sure the Delimited Text tab to left is selected. Latitude and Longitude should be recognized and show up in the Point coordinate section. Make sure that X is longitude and Y is latitude.
2. Click the three dots next to File name and navigate to where the csv file is stored. 
3. Name the layer under Layer name.
4. At the Geometry CRS make sure the imported table is the same Coordinate Reference System as the QGIS project.
5. You should see a sample table at the bottom. Click add and the points should be added to the project. If you don't see them where they're supposed to be or they ended up in West Africa, you need to reconcile the projections.

Let's look at a simpler/nearly instantaneous way to view and stylize the points. Make sure you have the Geo Data Viewer installed in Visual Studio Code. Right click on the norley2.csv and select view map. This brings up the dataset using kepler.gl. It looks pretty good right away. Here are a couple of quick changes:

1. Click the down arrow on the point layer to expand it. Reduce the Radius size to 8.
2. Click the 3 buttons next Fill Color and in Color Based On replace the default value with Species or Circumference. You can change the coloramp here as well. Color based on circumference gives you a visual on the size distribution.
3. The Label value lets you select any field if you want to add a label to each point.

{numref}`kepler` gives you a rather handsome map, even using the defaults.

```{figure} /figures/survey/kepler.png
:height: 400px
:name: kepler
A fast dash kepler.gl map of the points using Geo Data Viewer and Visual Studio Code.
```

There's your start from collection to visualization. Hopefully this will inspire you to go forth and collect some needed data for your organization, agency, or dissertation! There are some additional resources below.

## Resources
- **[Kobo Toolbox](https://www.kobotoolbox.org)**. Open source data collection platform that's easy to use and setup. It's really a form app that syncs to the cloud so you need export the csv or geojson files then load into your geospatial analysis software of choice.
- **[ODK](https://getodk.org)**. Free if you can self host and support.
- **[QField](https://qfield.org)**. Survey and digitize data mobile app that syncs to QGIS. The QField setup tutorial from [GISGeography](https://gisgeography.com/qfield/) runs you through the basics to get up and running. QField would be amazing if it was easy to set up and use. Unfortunately, I found setup and use not easy to use. The cloud sync works but does not allow much storage. You can pay for increased storage, however. Great idea, but needs a lot more work to be easier to use.
- **[Survey123](https://survey123.arcgis.com/)**. This is a paid software, but it works very well and syncs flawlessly with ArcGIS Online or ArcGIS pro. It does require additional credit purchase to store large amounts of data and add maps but perhaps you can keep that at a minimum by just using the forms. Hopefully over time QField catches up or Kobo provides additional geospatial capabilities.
