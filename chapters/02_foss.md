---
jupyter:
  jupytext:
    cell_metadata_filter: -all
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.1
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

# FOSS
Free and open-source geospatial tools and software are essential for data democratization, equitable planning, and preserving natural resources because they provide accessible and transparent ways to analyze and visualize spatial data. These tools enable individuals and communities to access, analyze, and share geospatial information regardless of their financial resources. By harnessing these tools, users can make informed decisions about land use planning, resource management, and environmental conservation. Additionally, the open nature of these tools fosters collaboration and innovation among diverse stakeholders, leading to more inclusive and sustainable solutions for our communities and the environment. Ultimately, free and open-source geospatial tools are crucial in promoting transparency, equity, and sustainability in decision-making processes related to our natural resources and the built environment.

## Participatory Rural Appraisal
For a portion of my graduate school research, I did community-based mapping, working with indigenous villages in a community-run reserve called Chimalapas in Oaxaca, Mexico using participatory rural appraisal (PRA) tools. PRA involves local community members in the assessment process, enabling them to actively contribute their knowledge, experiences, and perspectives regarding natural resources. This inclusive approach ensures that the assessment reflects the needs and priorities of the community, leading to more relevant and sustainable resource management decisions. Secondly, PRA fosters community empowerment by building local capacity, enhancing collective decision-making, and promoting ownership of development initiatives. 

![pra](/figures/pra.jpg)

The tools are simple; mapping can be drawing a diagram in the dirt or sand or working with villagers to create an elaborate model of how they perceive their local landscape. Other tools can involve using rocks or beans to evaluate resources and crops. The point of the exercises were to develop the spatial perception of how communities perceived their geography and determine what was important to them in managing and living in the natural world.

My point here, is mapping can be as simple and free as you want, especially to create something that is meaningful to your audience and you should use the right tools for the analysis in question. I learned as much from developing maps in dirt as I have from analyzing rasters for land use change or running regressions with multiple variables to develop machine learning models.

## Modern GIS
Geographic information systems (GIS) have changed substantially in the past four decades from simple, but clunky map layers to complex software able to process thousands of datapoints in multiple dimensions. Even the term GIS has started to shift toward geospatial data and data analysis and data analysis nearly always has a spatial component.

An explosion in data science during the past decade from big data to <a href="https://motherduck.com/blog/big-data-is-dead/" target="_blank">big data is dead</a> has not only seen data have its <a href="https://www.youtube.com/watch?v=DqVcDV5kGcg" target="_blank">long live rock/rock is dead</a> moment it has also seen proliferation in software and cost to geospatial analysis.

```{admonition} Modern GIS
"...the process, systems, and technology used to derive insights from geospatial data. Modern GIS
uses open, interoperable, and standards-based technology. It can be run locally or in the cloud and can scale to work with different types, velocities, and data scales." {cite}`forrest2023`
```

Modern GIS is open and run locally or in the cloud {cite}`forrestmod`. This shift from desktop and enterprise systems to cloud-native systems is a quantum leap from past geospatial analysis. Not only does this make use of efficient and serverless processing, it allows analysis at multiple scales and different users {numref}`cloud`.

```{figure} /figures/cloud.png
:height: 300px
:name: cloud
Modern cloud GIS infrastructure {cite}`forrestmod`.
```

## Data Democratization
Imagine a nonprofit NGO focused on wildlife conservation in a remote corner of the world, striving to protect endangered species and fragile ecosystems amidst mounting challenges. In today's digital age, data is inundating our world at an unprecedented rate, offering valuable insights crucial for informed decision-making. 

However, not all data is readily accessible, and the software required to analyze it often comes with a hefty price tag. This unfortunate reality creates a significant barrier, preventing organizations and communities in need from harnessing the power of data-driven solutions. Regrettably, the areas most in peril, facing the looming threats of destruction and extinction, are often located in developing regions where resources are scant.

Data democratization is essential to bridge this gap, ensuring that vital information is accessible, empowering conservation efforts, and safeguarding our natural world for future generations. Accessible data and imagery depends on free and open source software. The challenge with free and open source software is it usually requires knowledge of coding, a barrier for some without a computer science background.

## Challenges/Solutions
The solution is to learn how to code and fortunately there are a vast number of resources available to learn from youtube to online tutorials and blogs. However, there are still challenges. I offer a few along with suggested solutions:

1. **Coding language**. There are four main languages in this book. Which one should you learn first? We recommend starting with Python. <a href="https://geog-414.gishub.org/book/python/01_getting_started.html" target="_blank">Python basics</a> provides an excellent foundation for starting in Python and freeCodeCamp has many tutorials to complement this resource.
2. **Resources are everywhere**. This is true and you need to sort through what works, what is high quality, and find answers when you encounter errors. This book is meant to centralize some key resources for geospatial analysis. Don't forget that you can always do a search for an error online or ask large language models such as chatgpt, gemini, and copilot to help solve errors. The models don't always work, nor do the online resources such as Stack Exchange, but they will often get you 'unstuck'. One bonus of many open source softwares is their associated communities. QGIS has an incredible community connected to it and Earth Engine has a large google chat group where you can often search and find answers to questions you may have.
3. **Directions don't make sense**. Sadly this is a frustrating aspect in a world of coders that all seem to understand the lingo and jargon and you do not. We try to translate some of that here, but sometimes you may need to try things many times or just contact the developers and ask what they really mean. I've also found that if you can get to a video that can help translate the instructions or commands to what is really happening.
4. **Errors**. Sometimes stuff just doesn't work. Sometimes you're just not doing it right. My only suggestion is keep trying. Leave the work for a while then come back to it. Search for solutions then try them out. TRy out different code in a separate file. Jupyter notebooks are really great for isolating code blocks to help you see where errors occur. Github Copilot, although it does require a subscription, is getting much better at helping fix errors. If you're a student, Copilot is free. If not, try other engines, some of them are now open source and local so you can install them on your computer and try for free.
