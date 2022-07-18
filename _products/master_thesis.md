---
title: Master Thesis
subtitle: at National Cheng Kung University
image: img/master_thesis_home.png
features:
    - label: Year:2020
      icon: fa-map
    - label: Hec-Ras
      icon: fa-map
    - label: ArcMap
      icon: fa-map
    - label: Python
      icon: fa-map
Sort_Position: 04
layout: product
---
<div class="content">
<h2>Thesis title:</h2>
<em>Residential Flood Risk Mapping Based on Social Vulnerability Weighted by Analytical Hierarchy Process and Machine Learning Methods</em>
</div>
---
<div class="block">
	The flood risk maps are important tools for the state government authorities to provide information to residents about potential flooding dangers. This study aimed to develop a flood risk map as a combination of vulnerability and hazard maps. The influence of different return period discharge, vulnerability resolution, and vulnerability weighting on the final risk of single buildings was studied in the area of Shanhua district located in Tainan city.
	{% include image-modal.html ratio="is-128x128" link="products/master_thesis/img/01_study_area.jpg" alt="Merge grids" large_link="products/master_thesis/img/01_study_area.jpg" %}
	<figcaption>
	Figure 1: Study Area
	</figcaption>
</div>
---
<div class="block">
	<h2>Flood Hazard:</h2>
	<p>
		The fluvial flood hazard component was based on the simulated water depth by HEC-RAS hydraulic model in 2D (with diffusion wave approximation). 
		Return period flood peaks for 50, 100 and 200 year return period (RP) at upstream bridge station were equaled to 9280, 10630 and 12000 cms, respectively, and were obtained from local Water Resources Agency analysis. Designed hydrographs were prepared based on the United Nations-SPIDER advisory portal (United Nations 2020). Known flood event hydrographs and flood return periods were used for the calculation.
	</p>
	<p>
		River bed elevation reconstruction in digital elevation model (DEM) was performed in preprocessing in HEC-RAS as the original DEM was derived from LIDAR which cannot penetrate water surface.
		To obtain the proper Mannings n for river channel, The HEC-RAS 2D model was calibrated based on the upstream discharges of 5 typhoons according to the discharge that was measured downstream. The exported water depth raster in 5m spatial resolution was later rescaled to 25m and 100m.
	</p>
	<div class="columns">
		<div class="column">
			{% include image-modal.html ratio="is-128x128" link="products/master_thesis/img/02a_river_bed_reconstruction.jpg" alt="River bed" large_link="products/master_thesis/img/02a_river_bed_reconstruction.jpg" %}
			<figcaption>
			Figure 2: DEM before and after river bed reconstruction.
			</figcaption>
		</div>
		<div class="column">
			{% include image-modal.html ratio="is-128x128" link="products/master_thesis/img/02_hydrographs.jpg" alt="hydrographs" large_link="products/master_thesis/img/02_hydrographs.jpg" %}
			<figcaption>
			Figure 3: Designed hydrographs
			</figcaption>
		</div>
		<div class="column">
			{% include image-modal.html ratio="is-128x128" link="products/master_thesis/img/03_Q100.jpg" alt="Q100 RP" large_link="products/master_thesis/img/03_Q100.jpg" %}
			<figcaption>
				Figure 4: Q100 RP flood hazard map
			</figcaption>
		</div>
	</div>

</div>
---
<div class="block">
	<h2>Flood vulnerability:</h2>
	Three different vulnerability importance weightings were applied to generate flood vulnerability maps. Two machine learning models, classification and regression tree (CART) and random forest (RF), were selected for feature importance calculation in this study. The machine learning results were compared with the weighted importance obtained from an Analytical hierarchy process (AHP) procedure for performance evaluation, where a total of 16 questionnaire respondents participated in the survey. The vulnerability indexes were selected based on literature review and data availability in the study area. 
	The flood vulnerability was as well produced in two different spatial resolutions 20m and 100m based on the positions of houses.
	<div class="columns">
		<div class="column">
			{% include image-modal.html ratio="is-128x128" link="products/master_thesis/img/04_Households.jpg" alt="Households" large_link="products/master_thesis/img/04_Households.jpg" %}
			<figcaption>
			Figure 5: Households data transfered to 25m and 100m grids. 
			</figcaption>
		</div>
		<div class="column">
			{% include image-modal.html ratio="is-128x128" link="products/master_thesis/img/05_vulnerability_AHP_100m.jpg" alt="Vulnerability" large_link="products/master_thesis/img/05_vulnerability_AHP_100m.jpg" %}
			<figcaption>
				Figure 6: Flood vulnerability from AHP in 100m resolution
			</figcaption>
		</div>
	</div>
</div>
---
<div class="block">
<h2>Flood risk:</h2>
In total 30 different flood risk maps were generated covering different flood vulnerability methods, flood vulnerability resolution, and flood model resolution.
<div class="columns">
		<div class="column">
			{% include image-modal.html ratio="is-128x128" link="products/master_thesis/img/06_risk_matrix.jpg" alt="risk_matrix" large_link="products/master_thesis/img/06_risk_matrix.jpg" %}
			<figcaption>
			Figure 7: Risk matrix
			</figcaption>
		</div>
		<div class="column">
			{% include image-modal.html ratio="is-128x128" link="products/master_thesis/img/07_risk_mesh25Q200_ahp.jpg" alt="risk_mesh25Q200" large_link="products/master_thesis/img/07_risk_mesh25Q200_ahp.jpg" %}
			<figcaption>
			Figure 8: Flood risk of Q200 RP in 25m
			</figcaption>
		</div>
		<div class="column">
			{% include image-modal.html ratio="is-128x128" link="products/master_thesis/img/08_risk_mesh100Q200_ahp.jpg" alt="risk_mesh100Q200" large_link="products/master_thesis/img/08_risk_mesh100Q200_ahp.jpg" %}
			<figcaption>
				Figure 9: Flood risk of Q200 RP in 100m
			</figcaption>
		</div>
	</div>

</div> 
---
<div class="block">
	<h2>Findings:</h2>
	Fist, findings from vulnerability maps indicated that CART model tended to small overestimate, and RF, on the other hand, tended to largely overestimate AHP result. Second, the vulnerability resolution had a much larger impact due to fact that rougher resolution accommodated more households. Lastly, finer flood model resolution provided more precise results in urban areas and extended risk zones.
</div>
---
<div class="block">
	<h2>Data sources:</h2>
	 <ul>
		<li>Central Weather Bureau, Taiwan</li>
		<li>Shanhua Household Registration Office</li>
		<li>Water Resources Agency, Taiwan</li>
		<li>National Science and Technology Center for Disaster Reduction, Taiwan</li>
	 </ul>
</div>
