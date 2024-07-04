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
Stand density index is a measure of forest health. The stand density index (SDI) is the calculation of the size (DBH) and number of trees or trees/acre in a stand and calculated with the formula

$$ 
\sum_{i=1}^n TPA (DBH/25.4)^{1.6} 
$$

Where TPA = trees/acre and DBH = diameter breast height ({cite}[`north`; `woodall`; `reineke`]). SDI is used by foresters and ecologists and can be used as a relative measure of how crowded a stand is, show competition between trees, or as an overall measure of forest health (North et al., 2022).

## Methodology
To start measuring forest health in a local forest stand, I measured trees > 30 cm in dbh circumference within 500 m<sup>2</sup> plots at the Norleywood Enclosure in the New Forest National Park. The dataset shown is the first three plots measured.

## Resources
- **[Kobo Toolbox](https://www.kobotoolbox.org)**. Open source data collection platform that's easy to use and setup. It's really a form app that syncs to the cloud so you need export the csv or geojson files then load into your geospatial analysis software of choice.
- **[ODK](https://getodk.org)**. Free if you can self host and support.
- **[QField](https://qfield.org)**. Survey and digitize data mobile app that syncs to QGIS. The QField setup tutorial from [GISGeography](https://gisgeography.com/qfield/) runs you through the basics to get up and running. QField would be amazing if it was easy to set up and use. Unfortunately, I found setup and use not easy to use. The cloud sync works but does not allow much storage. You can pay for increased storage, however. Great idea, but needs a lot more work to be easier to use.
