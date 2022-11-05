---
title: 30DayMapChallenge
subtitle:
image: img/30dmc_2022_home.png
features:
    - label: Year:2022
      icon: fa-map
    - label: QGIS
      icon: fa-map
Sort_Position: 01
layout: product
---
<div class="content">
My first "30 Day Map Challenge"
</div>
---
<div class="block">
	<div class="columns">
		<div class="column is-one-third">
			<div class="box" style="width: 300px; height:525px">
			{% include image-modal.html ratio="is-3by4" link="products/30DayMapChallenge/img/01_Final.jpeg" alt="Points" large_link="products/30DayMapChallenge/img/01_Final.jpeg" %}
				<p class="is-size-5">1.Points</p>
				<p></p>
				<p class="is-size-7">Transformed AsterDEM to 10km resolution and then to points shapefile.</p>
			</div>
		</div>
		<div class="column is-one-third">
			<div class="box" style="width: 300px; height:525px">
			{% include image-modal.html ratio="is-3by4" link="products/30DayMapChallenge/img/02_Final.jpeg" alt="Lines" large_link="products/30DayMapChallenge/img/02_Final.jpeg" %}
				<p class="is-size-5">2.Lines</p>
				<p></p>
				<p class="is-size-7">Little play with Taiwan island points and measurements.</p>
			</div>
		</div>
		<div class="column is-one-third">
			<div class="box" style="width: 300px; height:525px">
			{% include image-modal.html ratio="is-3by4" link="products/30DayMapChallenge/img/03_Final.jpeg" alt="Polygons" large_link="products/30DayMapChallenge/img/03_Final.jpeg" %}
				<p class="is-size-5">3.Polygons</p>
				<p class="is-size-7">After my visit to Zwolle, I couldn't stop thinking about its city plan. So I decided to check its open data server and found that they do have an old city cadastre map.</p>
			</div>
		</div>
	</div>
</div>

<div class="block">
	<div class="columns">
		<div class="column is-one-third">
			<div class="box" style="width: 300px; height:525px">
			{% include image-modal.html ratio="is-3by4" link="products/30DayMapChallenge/img/04_Final.jpeg" alt="Green" large_link="products/30DayMapChallenge/img/04_Final.jpeg" %}
				<p class="is-size-5">4.Green</p>
				<p></p>
				<p class="is-size-7">False color combination of Sentinel-2 (B12, B8A, B4) which corresponds to Short-Wave Infrared view by using an amazing Semi-Automatic Classification Plugin for QGIS.</p>
			</div>
		</div>
		<div class="column is-one-third">
			<div class="box" style="width: 300px; height:525px">
			{% include image-modal.html ratio="is-5by4" link="products/30DayMapChallenge/img/05_Final.jpeg" alt="Ukraine" large_link="products/30DayMapChallenge/img/05_Final.jpeg" %}
				<p class="is-size-5">5.Ukraine</p>
				<p></p>
				<p class="is-size-7">Just a simplistic boundary map of Ukraine. </p>
			</div>
		</div>
		<div class="column is-one-third">
			<div class="box" style="width: 300px; height:525px">
			</div>
		</div>
	</div>
</div>


---
<div class="block">
		<h3>Data sources:</h3>
		 <ul>
			<li>AsterDEM - https://gdemdl.aster.jspacesystems.or.jp/</li>
			<li>Taiwan open data - https://data.gov.tw/en/</li>
			<li>Zwolle city open data https://smart-zwolle.opendata.arcgis.com/</li>
			<li>Semi-Automatic Classification Plugin for QGIS https://fromgistors.blogspot.com/p/semi-automatic-classification-plugin.html</li>
			<li>Ukraine boundary from https://geodata.lib.utexas.edu/</li>
		 </ul>
</div>
