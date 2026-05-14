---
title: pyErosivity
subtitle: Rainfall erosivity calculation in Python
layout: page
show_sidebar: false
sort_position: 2
image: /products/pyerosivity/img/fig00_Re_comparison.jpeg
---

<a class="button is-dark is-small" href="https://github.com/PetrVey/pyErosivity" target="_blank">View on GitHub</a>

<br><br>

<h2>About</h2>

<p>
  <strong>pyErosivity</strong> is a Python package for calculating rainfall erosivity (Re) from high-resolution precipitation time series at <strong>5-minute</strong> and <strong>60-minute</strong> temporal resolutions. Erosivity quantifies the potential of rainfall to detach and transport soil — a key input for soil erosion risk assessments using the RUSLE/USLE framework.
</p>

<article class="message is-info">
  <div class="message-body">
    <strong>Note:</strong> The erosivity methodology and underlying theory were developed and published by Rogler &amp; Schwertmann (1981) and Fischer et al. (2018). This repository provides a Python implementation of those methods. I developed this codebase as part of my PhD research at the University of Padova.
  </div>
</article>

<hr>

<h2>How It Works</h2>

<p>Erosivity events are identified using the <strong>maximum 30-minute rainfall intensity (Imax30)</strong> threshold:</p>

<table class="table is-bordered is-striped is-fullwidth">
  <thead>
    <tr>
      <th>Resolution</th>
      <th>Imax30 threshold</th>
      <th>Temporal scaling factor</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>5 min</td><td>12.7 mm/h</td><td>—</td></tr>
    <tr><td>60 min</td><td>5.79 mm/h</td><td>t = 1.9</td></tr>
  </tbody>
</table>

<p>
  The package computes per-event kinetic energy (Ekin) and erosivity indices in both <strong>EU units</strong> (N/h) and <strong>US units</strong> (MJ·mm/ha·hr), following the DIN 19708 methodology, with an alternative Brown &amp; Foster (1987) formulation also available.
</p>

<hr>

<h2>Key Functions</h2>

<table class="table is-bordered is-striped is-fullwidth">
  <thead>
    <tr><th>Function</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr><td><code>remove_incomplete_years()</code></td><td>Removes years with &gt;10% missing data</td></tr>
    <tr><td><code>get_events()</code></td><td>Identifies independent precipitation events (min. 24 h separation)</td></tr>
    <tr><td><code>get_events_Renard_RUSLE()</code></td><td>Event detection following the Renard/RUSLE methodology</td></tr>
    <tr><td><code>remove_short()</code></td><td>Filters events shorter than minimum duration</td></tr>
    <tr><td><code>get_only_erosivity_events()</code></td><td>Selects events exceeding erosivity thresholds</td></tr>
    <tr><td><code>get_events_values()</code></td><td>Computes Imax30, depth, Ekin, and Re for each event</td></tr>
    <tr><td><code>E_kin_i()</code></td><td>Per-interval kinetic energy (DIN 19708)</td></tr>
    <tr><td><code>E_kin_i_BrFr()</code></td><td>Per-interval kinetic energy (Brown &amp; Foster 1987)</td></tr>
    <tr><td><code>boostrapping_erosivity_60min()</code></td><td>Bootstrap resampling of annual erosivity metrics</td></tr>
  </tbody>
</table>

<hr>

<h2>Validation</h2>

<p>The package was validated against RIST software output (the reference for 5-min erosivity) over 73–74 filtered events.</p>

<figure>
  <img src="/products/pyerosivity/img/fig00_Re_comparison.jpeg" alt="Erosivity comparison across methods and resolutions" style="max-width:100%;">
  <figcaption><em>Comparison of erosivity Re [MJ·mm/ha·hr] for station VE_0091. Left: pyErosivity 5-min vs. RIST reference (R²=1.00, MBR=1.01) — near-perfect agreement. Top-right: uncorrected 60-min underestimates (MBR=0.50). Bottom-right: corrected 60-min with temporal scaling (MBR=0.95, R²=0.93).</em></figcaption>
</figure>

<br>

<figure>
  <img src="/products/pyerosivity/img/fig00_RE_datasets_lenght.jpeg" alt="Dataset sizes used in validation" style="max-width:55%;">
  <figcaption><em>Number of erosive events identified per method. The German 60-min threshold (5.79 mm/h) yields more events (149) than the 5-min threshold (74) due to its lower sensitivity.</em></figcaption>
</figure>

<hr>

<h2>Event Detection Methods</h2>

<p>
  Two event detection approaches are implemented, both combining the Imax30 intensity threshold with an accumulated precipitation criterion (&gt;12.7 mm per event) using OR logic:
</p>
<ul>
  <li><strong>Wischmeier (1959)</strong> — <code>get_only_erosivity_events()</code>: event qualifies if hourly intensity ≥ 12.7 mm/h <em>or</em> total accumulation ≥ 12.7 mm.</li>
  <li><strong>Renard/RUSLE (1997)</strong> — <code>get_only_erosivity_events_Renard()</code>: event qualifies if peak Imax30 depth ≥ 12.7 mm <em>or</em> total accumulation ≥ 12.7 mm.</li>
</ul>

<hr>

<h2>Methodology Citations</h2>

<p>
  Rogler, H. and Schwertmann, U. (1981).<br>
  <em>Erosivität der Niederschläge und Isoerodentkarte Bayerns.</em><br>
  Zeitschrift für Kulturtechnik und Flurbereinigung, 22, 99–112.
</p>

<p>
  Fischer, F. K., Winterrath, T., and Auerswald, K. (2018).<br>
  <em>Temporal- and spatial-scale and positional effects on rain erosivity derived from point-scale and contiguous rain data.</em><br>
  Hydrology and Earth System Sciences, 22, 6505–6518.<br>
  <a href="https://doi.org/10.5194/hess-22-6505-2018" target="_blank">https://doi.org/10.5194/hess-22-6505-2018</a>
</p>