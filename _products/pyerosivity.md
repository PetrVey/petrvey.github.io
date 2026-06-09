---
title: pyErosivity
subtitle: Rainfall erosivity calculation in Python
layout: page
show_sidebar: false
sort_position: 2
image: /products/pyerosivity/img/01_fig1.jpg
---

<a class="button is-dark is-small" href="https://github.com/PetrVey/pyErosivity" target="_blank">View on GitHub</a>

<br><br>

<h2>About</h2>

<p>
  <strong>pyErosivity</strong> is a Python package for computing rainfall erosivity (R-factor / EI30) from precipitation time series at <strong>any temporal resolution</strong>. Erosivity quantifies the capacity of rain to detach and transport soil — a key driver in the USLE/RUSLE family of soil erosion models. The package handles the full pipeline from raw precipitation data to per-event and annual erosivity statistics, including temporal resolution correction and bootstrap uncertainty estimation.
</p>

<article class="message is-info">
  <div class="message-body">
    <strong>Note:</strong> The erosivity methodology is based on Wischmeier &amp; Smith (1978), Renard et al. (1997), and DIN 19708:2017-08. The kinetic energy formula defaults to Rogler &amp; Schwertmann (1981), with Brown &amp; Foster (1987) and McGregor et al. (1995) also available. I developed this package as part of my PhD research at the University of Padova.
  </div>
</article>

<hr>

<h2>Pipeline</h2>

<p>The standard call order is:</p>

<ol>
  <li><code>remove_incomplete_years()</code> — removes years exceeding the missing-data tolerance; returns cleaned DataFrame and detected time resolution.</li>
  <li><code>get_events()</code> — separates storms by a minimum dry-spell gap (default <strong>6 hours</strong>, Wischmeier &amp; Smith 1958).</li>
  <li><code>remove_short()</code> — discards events shorter than a minimum duration.</li>
  <li><code>get_events_values()</code> — for each event computes depth, kinetic energy (E_kin), and peak intensities for all accumulation windows supported by the data resolution (imax_5, imax_10, imax_15, imax_30, imax_60).</li>
  <li><code>compute_erosivity()</code> — computes EI30 = E_kin × IMax30 (or IMax60 for hourly data); adds <code>erosivity_EU</code> [kJ m⁻² mm h⁻¹] and <code>erosivity_US</code> [MJ mm ha⁻¹ h⁻¹].</li>
  <li><code>get_only_erosivity_events()</code> — applies the Wischmeier dual criterion to retain erosive events.</li>
  <li><em>[optional]</em> <code>apply_rusle_split()</code> — further splits erosive events using the Renard et al. (1997) 6-hour / 1.27 mm within-storm rule.</li>
</ol>

<hr>

<h2>Event Filtering Criteria</h2>

<p>
  An event is classified as erosive if it satisfies <strong>at least one</strong> of two criteria (OR logic):
</p>

<table class="table is-bordered is-striped is-fullwidth">
  <thead>
    <tr>
      <th>Formulation</th>
      <th>Criterion (i) — depth</th>
      <th>Criterion (ii) — intensity</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Standard RUSLE</strong></td>
      <td>event_depth ≥ 12.7 mm</td>
      <td>IMax15 ≥ 25.4 mm/h</td>
      <td>Wischmeier &amp; Smith (1978); 6.35 mm in 15 min</td>
    </tr>
    <tr>
      <td><strong>Alternative</strong></td>
      <td>event_depth ≥ 12.7 mm</td>
      <td>IMax30 ≥ 12.7 mm/h</td>
      <td>Wider window; looser filter; validated vs RIST</td>
    </tr>
  </tbody>
</table>

<p>Both thresholds derive from the same physical quantity — 6.35 mm concentrated within the accumulation window. The wider 30-min window selects more events than IMax15 on identical data.</p>

<figure>
  <img src="/products/pyerosivity/img/rainfall_intensity_windows.png" alt="Same 6.35 mm burst measured at 15, 30, and 60-min windows" style="max-width:90%;">
  <figcaption><em>The same 6.35 mm rain burst gives IMax15 = 25.4 mm/h, IMax30 = 12.7 mm/h, and IMax60 = 6.35 mm/h. All three erosivity thresholds represent the same physical event at different accumulation windows.</em></figcaption>
</figure>

<hr>

<h2>Kinetic Energy Formulas</h2>

<p><code>get_events_values()</code> accepts a <code>formula</code> argument. All formulas are normalized to [kJ m⁻² mm⁻¹]:</p>

<table class="table is-bordered is-striped is-fullwidth">
  <thead>
    <tr><th>Key</th><th>Formula</th><th>Reference</th><th>Notes</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><code>'rogler'</code> (default)</td>
      <td>e_k = (11.89 + 8.73·log₁₀I) × 10⁻³, capped at 28.33×10⁻³ for I ≥ 76.2 mm/h</td>
      <td>Rogler &amp; Schwertmann (1981) / DIN 19708</td>
      <td>European calibration, log form</td>
    </tr>
    <tr>
      <td><code>'brown_foster'</code></td>
      <td>e_k = 0.029·(1 − 0.72·exp(−0.05I))</td>
      <td>Brown &amp; Foster (1987), RUSLE standard</td>
      <td>Exponential form, natural plateau</td>
    </tr>
    <tr>
      <td><code>'mcgregor'</code></td>
      <td>e_k = 0.029·(1 − 0.72·exp(−0.082I))</td>
      <td>McGregor et al. (1995), RUSLE2</td>
      <td>Steeper decay at low intensities</td>
    </tr>
  </tbody>
</table>

<hr>

<h2>Key Functions</h2>

<table class="table is-bordered is-striped is-fullwidth">
  <thead>
    <tr><th>Function</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr><th colspan="2" style="background:#f5f5f5">Core pipeline</th></tr>
    <tr><td><code>remove_incomplete_years()</code></td><td>Removes years with &gt;10% missing data; auto-detects time resolution</td></tr>
    <tr><td><code>get_events()</code></td><td>Extracts events using a minimum dry-spell gap (default 6 h); removes events near data gaps</td></tr>
    <tr><td><code>remove_short()</code></td><td>Filters events shorter than a minimum duration</td></tr>
    <tr><td><code>get_events_values()</code></td><td>Computes depth, E_kin, and imax_5/10/15/30/60 for each event; supports formula choice</td></tr>
    <tr><td><code>compute_erosivity()</code></td><td>Adds erosivity_EU and erosivity_US (EI30 = E_kin × IMax30/60); auto-detects imax column</td></tr>
    <tr><td><code>get_only_erosivity_events()</code></td><td>Dual-criterion filter: IMax ≥ threshold OR depth ≥ 12.7 mm</td></tr>
    <tr><td><code>apply_rusle_split()</code></td><td>Renard (1997) within-storm splitting: splits where any 6 h window &lt; 1.27 mm, then re-filters</td></tr>
    <tr><th colspan="2" style="background:#f5f5f5">Resolution correction</th></tr>
    <tr><td><code>find_optimal_thr_imax30()</code></td><td>Finds the intensity threshold that minimises the gap in mean annual event count to a reference (Fischer et al. 2018)</td></tr>
    <tr><td><code>compute_sf_annual_r()</code></td><td>Scaling factor from year-by-year annual R comparison (same calendar period required)</td></tr>
    <tr><td><code>compute_sf_clim()</code></td><td>Scaling factor from climatological mean annual R; no year matching — for obs vs CPM</td></tr>
    <tr><td><code>compute_sf_per_event()</code></td><td>Scaling factor from matched per-event EI (inner join on event date)</td></tr>
    <tr><th colspan="2" style="background:#f5f5f5">Statistics &amp; uncertainty</th></tr>
    <tr><td><code>get_mean_annual_stats()</code></td><td>Mean annual event count, R-factor, depth, and intensity from an event table</td></tr>
    <tr><td><code>bootstrapping_erosivity_60min()</code></td><td>Block bootstrap over calendar years for observational data</td></tr>
    <tr><td><code>bootstrapping_erosivity_CPM_60min()</code></td><td>Bootstrap with optional pre-defined year-draw sequence (for CPM ensemble comparisons)</td></tr>
    <tr><th colspan="2" style="background:#f5f5f5">Kinetic energy (unit functions)</th></tr>
    <tr><td><code>E_kin_i_Rogler()</code></td><td>Rogler &amp; Schwertmann (1981) / DIN 19708 — default</td></tr>
    <tr><td><code>E_kin_i_BrFr()</code></td><td>Brown &amp; Foster (1987) — RUSLE standard</td></tr>
    <tr><td><code>E_kin_i_McGregor()</code></td><td>McGregor et al. (1995) — RUSLE2 variant</td></tr>
  </tbody>
</table>

<hr>

<h2>Study 1: Validation against RIST 3.99</h2>

<p>
  pyErosivity was validated against <strong>RIST 3.99</strong> (USDA Rainfall Intensity Summarization Tool) — the reference implementation of RUSLE — using 31 years (1990–2020) of 5-min data from station VE_0091 near Kreuzbergpass, Italy (~1600 m a.s.l.).
</p>

<figure>
  <img src="/products/pyerosivity/img/01_fig1.jpg" alt="Validation scatter and mean annual statistics against RIST" style="max-width:100%;">
  <figcaption><em>Validation against RIST 3.99. pyErosivity recovers 962–966 erosive events (vs RIST 927–962) and matches the mean annual R-factor to within <strong>0.4%</strong> for both IMax30 and IMax15 criteria. The 4-event gap is fully explained by RIST's internal inch rounding at the 12.8 mm threshold.</em></figcaption>
</figure>

<table class="table is-bordered is-striped is-fullwidth">
  <thead>
    <tr><th></th><th>RIST IMax30</th><th>pyEr IMax30</th><th>RIST IMax15</th><th>pyEr IMax15</th></tr>
  </thead>
  <tbody>
    <tr><td>Events (total)</td><td>962</td><td>966</td><td>927</td><td>931</td></tr>
    <tr><td>Events / yr</td><td>31.0</td><td>31.2</td><td>29.9</td><td>30.0</td></tr>
    <tr><td>Mean depth [mm]</td><td>31.4</td><td>31.5</td><td>32.3</td><td>32.3</td></tr>
    <tr><td>R-factor [MJ mm ha⁻¹ h⁻¹ yr⁻¹]</td><td>2027.8</td><td>2019.7</td><td>1993.0</td><td>1985.6</td></tr>
  </tbody>
</table>

<hr>

<h2>Study 2: Effect of Temporal Resolution</h2>

<p>
  At coarser temporal resolution (15, 30, 60 min), IMax30 is underestimated because the sliding window straddles fixed clock bins. Two distinct problems arise:
</p>

<figure>
  <img src="/products/pyerosivity/img/rainfal_bining_resolution.jpeg" alt="Sketch showing how coarse binning merges events or creates false dry spells" style="max-width:85%;">
  <figcaption><em>Coarse binning can both lose events (a short burst straddles a bin boundary and never reaches the intensity threshold) and merge events (the inter-storm gap shrinks below the 6-hour separation threshold).</em></figcaption>
</figure>

<p>
  At 60-min resolution the IMax-only zone empties completely for any threshold: an event intense enough to exceed 12.7 mm/h in one hour automatically accumulates ≥ 12.7 mm and satisfies the depth criterion instead. The R-factor drops by <strong>~43%</strong> relative to 5-min.
</p>

<figure>
  <img src="/products/pyerosivity/img/02_fig4.jpg" alt="Event classification scatter at all resolutions and criteria" style="max-width:100%;">
  <figcaption><em>Event depth vs peak intensity at 5, 15, 30, and 60-min resolution for three selection criteria. At 60-min the IMax-only zone (steelblue) disappears entirely; all selected events are in the depth-only zone (tomato).</em></figcaption>
</figure>

<hr>

<h2>Study 3: Threshold Calibration &amp; Scaling Factor Correction</h2>

<p>
  Coarser resolution introduces two independent biases: (1) <strong>event selection bias</strong> — the intensity criterion selects fewer events; (2) <strong>intensity underestimation bias</strong> — EI30 is lower even for the same storm. Two correction steps address them:
</p>

<ol>
  <li><strong>Threshold calibration:</strong> <code>find_optimal_thr_imax30()</code> sweeps all unique IMax values and finds the cut-off that recovers the 5-min event count. For 60-min data the optimal threshold is ~6.8 mm/h (vs the naive 12.7 mm/h).</li>
  <li><strong>Scaling factor:</strong> a multiplicative SF removes the remaining within-event intensity bias. Three approaches are available — <code>compute_sf_annual_r</code> (year-by-year), <code>compute_sf_per_event</code> (matched events), and <code>compute_sf_clim</code> (climatological mean; required when obs and CPM cover different periods).</li>
</ol>

<figure>
  <img src="/products/pyerosivity/img/03_fig3.jpg" alt="Annual R-factor before and after scaling factor correction" style="max-width:100%;">
  <figcaption><em>Annual R-factor scatter (5-min reference vs 60-min target) before and after applying each scaling factor approach. After correction, all three approaches align the mean annual R with the 5-min reference.</em></figcaption>
</figure>

<hr>

<h2>Study 4: Bootstrap Uncertainty &amp; OBS vs CPM Comparison</h2>

<p>
  <code>bootstrapping_erosivity_60min()</code> and <code>bootstrapping_erosivity_CPM_60min()</code> estimate uncertainty by block-resampling calendar years (default 1000 iterations). The CPM variant accepts a pre-defined year-draw array (<code>randy</code>) so that different ensemble members are compared on identical samples.
</p>

<figure>
  <img src="/products/pyerosivity/img/04_fig1.jpg" alt="Bootstrap distributions for OBS and CPM" style="max-width:100%;">
  <figcaption><em>Bootstrap distributions (boxplots) for mean annual events, mean IMax, mean depth, and mean annual R-factor. OBS = 31 years (VE_0091, 1990–2020); CPM = ETH convection-permitting model, historical run (10 years, 1996–2005). The shorter CPM record produces substantially wider uncertainty boxes.</em></figcaption>
</figure>

<p>
  The comparison highlights that threshold calibration and scaling factor correction address <em>temporal resolution bias</em> but do not replace a full bias correction of the underlying precipitation field. The CPM's ~95% wet bias at this Alpine station propagates directly into erosive event counts and R-factor even after resolution correction.
</p>

<hr>

<h2>References</h2>

<p>
  Wischmeier, W. H. &amp; Smith, D. D. (1978).<br>
  <em>Predicting Rainfall Erosion Losses.</em> USDA Agricultural Handbook 537.
</p>

<p>
  Renard, K. G. et al. (1997).<br>
  <em>Predicting Soil Erosion by Water (RUSLE).</em> USDA Agricultural Handbook 703.
</p>

<p>
  Rogler, H. &amp; Schwertmann, U. (1981).<br>
  <em>Erosivität der Niederschläge und Isoerodentkarte Bayerns.</em><br>
  Journal of Rural Engineering and Development, 22, 99–112.
</p>

<p>
  Fischer, F. K., Winterrath, T. &amp; Auerswald, K. (2018).<br>
  <em>Temporal- and spatial-scale and positional effects on rain erosivity.</em><br>
  Hydrology and Earth System Sciences, 22, 6505–6518.<br>
  <a href="https://doi.org/10.5194/hess-22-6505-2018" target="_blank">https://doi.org/10.5194/hess-22-6505-2018</a>
</p>

<p>
  Brown, L. C. &amp; Foster, G. R. (1987).<br>
  <em>Storm erosivity using idealized intensity distributions.</em><br>
  Transactions of the ASAE, 30(2), 379–386.
</p>

<p>
  van Dijk, A. I. J. M., Bruijnzeel, L. A. &amp; Rosewell, C. J. (2002).<br>
  <em>Rainfall intensity–kinetic energy relationships: a critical literature appraisal.</em><br>
  Journal of Hydrology, 261(1), 1–23.<br>
  <a href="https://doi.org/10.1016/S0022-1694(02)00020-3" target="_blank">https://doi.org/10.1016/S0022-1694(02)00020-3</a>
</p>
