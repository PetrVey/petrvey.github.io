---
title: pyErosivity
subtitle: Rainfall erosivity calculation in Python
layout: page
show_sidebar: false
sort_position: 2
image: /products/pyerosivity/img/fig00_Re_comparison.jpeg
github: https://github.com/PetrVey/pyErosivity
---

<div class="content">

<a class="button is-dark is-small" href="https://github.com/PetrVey/pyErosivity" target="_blank">View on GitHub</a>

<br><br>

## About

**pyErosivity** is a Python package for calculating rainfall erosivity (Re) from high-resolution precipitation time series at **5-minute** and **60-minute** temporal resolutions. Erosivity quantifies the potential of rainfall to detach and transport soil — a key input for soil erosion risk assessments using the RUSLE/USLE framework.

> **Note:** The erosivity methodology and underlying theory were developed and published by Rogler & Schwertmann (1981) and Fischer et al. (2018). This repository provides a Python implementation of those methods. I developed this codebase as part of my PhD research at the University of Padova.

---

## How It Works

Erosivity events are identified using the **maximum 30-minute rainfall intensity (Imax30)** threshold:

| Resolution | Imax30 threshold | Temporal scaling factor |
|---|---|---|
| 5 min | 12.7 mm/h | — |
| 60 min | 5.79 mm/h | t = 1.9 |

The package computes per-event kinetic energy (Ekin) and erosivity indices in both **EU units** (N/h) and **US units** (MJ·mm/ha·hr), following the DIN 19708 methodology for kinetic energy, with an alternative Brown & Foster (1987) formulation also available.

---

## Key Functions

| Function | Description |
|---|---|
| `remove_incomplete_years()` | Removes years with >10% missing data |
| `get_events()` | Identifies independent precipitation events (min. 24 h separation) |
| `get_events_Renard_RUSLE()` | Event detection following the Renard/RUSLE methodology |
| `remove_short()` | Filters events by minimum duration |
| `get_only_erosivity_events()` | Selects events exceeding erosivity thresholds |
| `get_events_values()` | Computes Imax30, depth, Ekin, and Re for each event |
| `E_kin_i()` | Per-interval kinetic energy (DIN 19708) |
| `E_kin_i_BrFr()` | Per-interval kinetic energy (Brown & Foster 1987) |
| `boostrapping_erosivity_60min()` | Bootstrap resampling of annual erosivity metrics |

---

## Validation

The package was validated against RIST software output (the reference for 5-min erosivity) over 73–74 filtered events.

<figure>
  <img src="/products/pyerosivity/img/fig00_Re_comparison.jpeg" alt="Erosivity comparison across methods and resolutions" style="max-width:100%;">
  <figcaption><em>Comparison of erosivity Re [MJ·mm/ha·hr] across methods for station VE_0091. Left: pyErosivity 5-min vs. RIST reference (R²=1.00, MBR=1.01) — near-perfect agreement. Top-right: uncorrected 60-min underestimates (MBR=0.50). Bottom-right: corrected 60-min with temporal scaling (MBR=0.95, R²=0.93).</em></figcaption>
</figure>

<figure>
  <img src="/products/pyerosivity/img/fig00_RE_datasets_lenght.jpeg" alt="Dataset sizes used in validation" style="max-width:60%;">
  <figcaption><em>Number of erosive events identified per method. The German 60-min threshold (5.79 mm/h) yields more events (149) than the 5-min threshold (74) due to its lower sensitivity.</em></figcaption>
</figure>

---

## Current Limitations

Erosivity events are currently identified **only** via the Imax30 threshold. Future work will also incorporate the accumulated precipitation criterion (>12.7 mm per event) following the full RUSLE definition.

---

## Methodology Citations

Rogler, H. and Schwertmann, U. (1981).
*Erosivität der Niederschläge und Isoerodentkarte Bayerns.*
Zeitschrift für Kulturtechnik und Flurbereinigung, 22, 99–112.

Fischer, F. K., Winterrath, T., and Auerswald, K. (2018).
*Temporal- and spatial-scale and positional effects on rain erosivity derived from point-scale and contiguous rain data.*
Hydrology and Earth System Sciences, 22, 6505–6518.
[https://doi.org/10.5194/hess-22-6505-2018](https://doi.org/10.5194/hess-22-6505-2018)

</div>