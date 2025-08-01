---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.4
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# AI
Can artificial intelligence revolutionize the geospatial world? 

![ai](/figures/ai.png)
credit: brave.com

## Future edition
Whether AI can revolutionize the geospatial world is a good question. {cite:t}`aiscan` concluded that AI will lead to beneficial outcomes, however, it is not a panacea, and measures must be put into place for equitable access and deployment. In a review of the same paper, Frank van der Most points out that only two of the 21 applications cited as significant are focused on implementing solutions {cite}`fvdm`.

There have been many attempts and big claims in the geospatial world, but as of 2024, I have to conclude it isn't quite ready for primetime (although this is rapidly changing)! Machine learning (ML) is well developed in the free and open source (cf. chapters or tutorials from Leafmap and the R geocomputation book). ML is often conflated with AI, but it's not the same. Artificial intelligence for geospatial is at the gee-whiz stage, but it's not amazing. One recent example showed prompt engineering with GeoGPT to produce some ok chloropleth maps that would take the same amount of time to assemble using the appropriate dataset and software highlighted in this book. Plus, taking a little time to run the code and do exploratory data analysis always allows you to know the data, which is something that doesn't happen when you ask a question and get a map. Also, GeoGPT is not free, nor is it open source!

An exception to the usefulness side I've seen with AI is [Bunting Lab's](https://buntinglabs.com/) autocomplete for map digitization, which installs as a QGIS plugin. This isn't a free tool, but it seems like it would certainly be worth its weight in gold if you needed to do a lot of map digitizing, taking much of the tedious manual labor out of this task. Another exception is where AI generates cut-and-paste codeblocks that throw fewer errors than the nonsense generated from prompts a few months ago or get you unstuck when an approach is not working.

Due to AI's underwhelming but promising status to date, I will wait another year to see if more compelling examples arise. I've provided a few promising links. Overall, AI could help democratize geospatial analysis by lowering the cost of entry to both data and coding.

## Resources
- [Autonomous GIS](https://github.com/gladcolor/LLM-Geo). This repo and LLM are pretty cool and hopefully will receive further development over time. Unfortunately, there was a lot of activity from commits when it came out, but not much since.
- [Jupyter generative AI](https://blog.jupyter.org/generative-ai-in-jupyter-3f7174824862). Generative AI coding in Jupyter notebooks.
- [human brain edge over ai article](https://www.linkedin.com/pulse/where-human-brain-still-has-edge-over-ai-fast-company-j2jpe/)
- [A Beginner's Guide to Prompt Engineering with GitHub Copilot](https://dev.to/github/a-beginners-guide-to-prompt-engineering-with-github-copilot-3ibp). This is an extensive guide on how to engineer your prompts to code better and best use AI. It is also applicable to prompts in other platforms such as Gemini or ChatGPT.
- [Open source MLOps: Platforms, frameworks, and tools](https://neptune.ai/blog/best-open-source-mlops-tools). Thoughtful piece on pros and cons of open source machine learning tools.
- [Awesome Machine Learning](https://github.com/josephmisiti/awesome-machine-learning). A curated list of resources, tools, frameworks, articles, and projects related to Machine Learning Operations (MLOps).
- [GeoGPT: An assistant for understanding and processing geospatial tasks](https://doi.org/10.1016/j.jag.2024.103976). Paper by Zhang et al (2024) on the GeoGPT model that can conduct geospatial data collection, processing, and analysis in an autonomous manner.
- [Aino AI plugin](https://plugins.qgis.org/plugins/aino-qgis-plugin-main/). QGIS plugin Aino converts natural language prompts such as "parks in Barcelona" into vector layers containing relevant OSM data.
- [Clay Foundation Model](https://clay-foundation.github.io/model/index.html). Does it only work on Linux devices with CUDA GPUs? What the?




<!-- 

 It could be that AI helps to democratize geospatial analysis by lowering the cost of entry to geospatial data and software. Democratization of data medium article 
 
From Josep Ferrer (@rfeers on twitter): In multiple linear regression, imagine you're baking. You've got different ingredients or variables. You need the perfect recipe (model) for your cake (prediction). Each ingredient's quantity (coefficient) affects the taste (outcome).
-->
