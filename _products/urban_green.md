---
title: Urban green mapping
subtitle: 
image: img/urban_green_home.jpg
features:
    - label: Year:2022
      icon: fa-map
    - label: QGIS
      icon: fa-map
    - label: Python
      icon: fa-map

Sort_Position: 01
layout: product
---
---
<div class="content">
Little for fun project :)
</div>
---

<div class="content">
	<h3>Problem statment:</h3>
	<p>In 2019, The city of Prague (capital of the Czech Republic) set a goal of planting a million trees on its territory within eight years</p>
	<p>Details here: <a href="https://www.zastromujprahu.cz" target="_blank">zastromujprahu.cz</a> and <a href="https://adaptacepraha.cz" target="_blank">adaptacepraha.cz</a>
	<p>Out of curiosity, I want to map how total % urban green has improved after this policy was implemented.</p>
	<p>It's best to use satellite observations for such task as it's very similar to landuse change mapping.</p>
	<p>Altought, in this case, the simpler method based on normalized difference vegetation index <a href="https://doi.org/10.3390/land11030351" target="_blank"><b>(NDVI)</b></a> can be used. This method utilized the Sentinel-2 satellite imagery.</p>
	<p></p>
	
	<h3>How I did it:</h3>
	<p><b>1.) Download:</b></p>
	<p>Shapefile of <a href="https://www.geoportalpraha.cz/en/data/opendata" target="_blank">municipality districts of Prague city</a>.</p>
	<p>Cloudless Sentinel-2 satellite imagery from 2020 to 2021. Probably the easiest option for this is to use <a href="https://fromgistors.blogspot.com/p/semi-automatic-classification-plugin.html" target="_blank">Semi-Automatic Classification Plugin for QGIS</a> by amazing Luca Congedo.</p>
	<p>Note: Sentinel-2 images were downloaded for summer period (June to August) from 2015 to 2021. This mostly corresponded to only one cloudless image only for each year.</p>
	<div class="columns">
		<div class="column">
			{% include image-modal.html ratio="is-128x128" link="products/urban_green/img/01_321RGB.jpg" alt="Sentinel-2 RBG" large_link="products/urban_green/img/01_321RGB.jpg" %}
			<figcaption>
			Figure 1: Sentinel-2 Natural Color (combination of (B4, B3, B2))
			</figcaption>
		</div>
		<div class="column">
			{% include image-modal.html ratio="is-128x128" link="products/urban_green/img/00_prague.jpg" alt="Sentinel-2 RBG Prague" large_link="products/urban_green/img/00_prague.jpg" %}
			<figcaption>
			Figure 2: Zoomed to Prague city centre
			</figcaption>
		</div>
		<div class="column">
			{% include image-modal.html ratio="is-128x128" link="products/urban_green/img/02_732RGB.jpg" alt="Sentinel-2 Color infrared" large_link="products/urban_green/img/02_732RGB.jpg" %}
			<figcaption>
			Figure 3: Sentinel-2 Color Infrared (combination of B8, B4, B3)
			</figcaption>
		</div>
	</div>
	<p></p>
	<p><b>2.) Calculate NDVI</b></p>
	<p>Equation for NDVI goes as: <i>NDVI = (NIR-RED) / (NIR+RED)</i>.</p>
	<p>These refers to: <i>NDVI = (B8 - B4) / (B8 + B4)</i> of Sentinel-2.</p>
	<p>In my case, I did this by raster calculator in QGIS.</p>
	<div class="columns">
		<div class="column">
			{% include image-modal.html ratio="is-128x128" link="products/urban_green/img/03_ndvi20200806.jpg" alt="NDVI" large_link="products/urban_green/img/03_ndvi20200806.jpg" %}
			<figcaption>
			Figure 4: Sentinel-2 NDVI 
			</figcaption>
		</div>
		<div class="column">
			{% include image-modal.html ratio="is-128x128" link="products/urban_green/img/05_ndvi20200806_zoom.jpg" alt="NDVI Prague centre" large_link="products/urban_green/img/05_ndvi20200806_zoom.jpg" %}
			<figcaption>
			Figure 5: NDVI, Zoomed to Prague city centre
			</figcaption>
		</div>
	</div>
	
	<p><b>3.) Divide image to non-vegetation and vegetation</b></p>
	<p>Again, I used raster calculator with conditional statments where NDVI>0.19 was vegetation and NDVI<0.19 was non-vegetation.</p>
	<div class="columns">
		<div class="column">
			{% include image-modal.html ratio="is-128x128" link="products/urban_green/img/07_UG.jpg" alt="Urban green" large_link="products/urban_green/img/07_UG.jpg" %}
			<figcaption>
			Figure 6: Vegetation and non-vegetation urban map
			</figcaption>
		</div>
	</div>
	
	<p><b>4.) Calculate percentage of urban green in each municipality district</b></p>
	<p>There are many ways how to handle this task. I used zonal statistics where raster values were summed to each polygon.</p>
	<p>Lastly, to obtain percentage of vegatation the sum was divided by count.</p>
	<p></p>
<div class="content">
	<h3>Result:</h3>
	<figure class="image is-320x240">
		<img src="img/08_result_gif.gif">
			<figcaption>
				Figure 8: Animation of  urban green percentage in each satellite image
		</figcaption>
	</figure>
	<p></p>
	<p>Also, let's have a look how Prague city centre vegetation has changed since 2015.</p>
	<p>There was a positive trend in development. Altought, this result also highligted a seasonality changes in summer during wet/dry periods. The drop in 2020 was probably caused by unusual drought summer, thus, low-vegetatation (grass+shrub) died or has too low NDVI.</p>
	<figure class="image is-320x240">
		<img src="img/09_prg_time.JPEG">
			<figcaption>
				Figure 9: Temporal change of vegetation in Prague 1, 2, and 3
		</figcaption>
	</figure>
	<p>There was a positive trend in development. Altought, this result also highligted a seasonality changes in summer during wet/dry periods. The drop in 2020 was probably caused by unusual drought summer, thus, low-vegetatation (grass+shrub) died or has too low NDVI.</p>
	<p></p>
	
---
	<p>Note:</p>
	<p>The results of this project cannot be interpreted as the absolute truth. It is always necessary to do further analysis. </p>
	<p>There is also possibility to detect only trees, so more accurate analysis can be done in future.</p>
</div>
---
<div class="block">
	<h3>Data sources:</h3>
	 <ul>
		<li><a href="https://www.geoportalpraha.cz/en/data/opendata" target="_blank">Open data in Prague</a></li>
		<li><a href="https://scihub.copernicus.eu/" target="_blank">Copernicus Open Access Hub</a></li>
	 </ul>
</div>
