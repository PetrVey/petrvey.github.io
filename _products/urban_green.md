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
Sort_Position: 02
layout: product
---
---
<div class="content">
Little for fun project :)
</div>
---

<div class="content">
	<h3>Problem statment:</h3>
	<p>In 2019, the city of Prague (capital of the Czech Republic) set a goal of planting one million trees within eight years on its territory.</p> 
	<p>Details can be found at <a href="https://www.zastromujprahu.cz" target="_blank">zastromujprahu.cz</a> and <a href="https://adaptacepraha.cz" target="_blank">adaptacepraha.cz</a>.</p> 
	<p>Out of curiosity, I aim to map how the total percentage of urban green areas has changed since this policy was implemented.</p> 
	<p>Satellite observations are ideal for this task, as it is very similar to land-use change mapping.</p> 
	<p>Alternatively, a simpler approach based on the normalized difference vegetation index (<a href="https://doi.org/10.3390/land11030351" target="_blank"><b>NDVI</b></a>) can be used. This method utilizes Sentinel-2 satellite imagery.</p>
	<p></p>
		
	<h3>How I did it:</h3>
	<p><b>1.) Download:</b></p>
	<p>Shapefile of the <a href="https://www.geoportalpraha.cz/en/data/opendata" target="_blank">municipality districts of Prague city</a>.</p> 
	<p>Cloud-free Sentinel-2 satellite imagery from 2020 to 2021. The easiest approach for processing is likely the <a href="https://fromgistors.blogspot.com/p/semi-automatic-classification-plugin.html" target="_blank">Semi-Automatic Classification Plugin for QGIS</a>, developed by Luca Congedo.</p> 
	<p>Note: Sentinel-2 images were downloaded for the summer period (June to August) from 2015 to 2021. In most cases, only a single cloud-free image was available per year.</p>
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
	<p>In my case, this was done using the Raster Calculator in QGIS.</p>
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
	<p>I used the Raster Calculator with conditional statements, classifying pixels with NDVI > 0.19 as vegetation and NDVI ≤ 0.19 as non-vegetation.</p>
	<div class="columns">
		<div class="column">
			{% include image-modal.html ratio="is-128x128" link="products/urban_green/img/07_UG.jpg" alt="Urban green" large_link="products/urban_green/img/07_UG.jpg" %}
			<figcaption>
			Figure 6: Vegetation and non-vegetation urban map
			</figcaption>
		</div>
	</div>
	
	<p><b>4.) Calculate the percentage of urban green areas in each municipal district.</b></p>
	<p>There are several approaches to accomplish this task. I used zonal statistics, summing raster values within each polygon.</p> 
	<p>Finally, the percentage of vegetation was calculated by dividing the sum of vegetation pixels by the total number of pixels in the polygon.</p>
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
	<p>Next, I examined how vegetation in the Prague city centre has changed since 2015.</p> 
	<p>Overall, there was a positive trend in vegetation development. However, this analysis also highlighted seasonal variations during the summer months associated with wet and dry periods. The drop in 2020 was likely caused by an unusually dry summer, which led to low vegetation (grass and shrubs) dying or exhibiting very low NDVI values.</p>
	<figure class="image is-320x240">
		<img src="img/09_prg_time.JPEG">
			<figcaption>
				Figure 9: Temporal change of vegetation in Prague 1, 2, and 3
		</figcaption>
	</figure>
	<p></p>
	
---
	<p>Note:</p>
	<p>The results of this project should not be interpreted as absolute truth; further analysis is always necessary.</p> 
	<p>It is also possible to focus specifically on detecting trees, which would allow for a more accurate analysis in the future.</p>
</div>
---
<div class="block">
	<h3>Data sources:</h3>
	 <ul>
		<li><a href="https://www.geoportalpraha.cz/en/data/opendata" target="_blank">Open data in Prague</a></li>
		<li><a href="https://scihub.copernicus.eu/" target="_blank">Copernicus Open Access Hub</a></li>
	 </ul>
</div>
