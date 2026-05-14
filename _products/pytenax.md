---
title: pyTENAX
subtitle: Temperature-dependent extreme precipitation modeling in Python
layout: page
show_sidebar: false
sort_position: 1
image: /products/pytenax/img/fig_returnlevels.jpg
---

<div class="content">

<a class="button is-dark is-small" href="https://github.com/PetrVey/pyTENAX" target="_blank">View on GitHub</a>
&nbsp;
<a class="button is-light is-small" href="https://pytenax.readthedocs.io/en/latest/" target="_blank">Documentation</a>

<br><br>

## About

**pyTENAX** is a Python implementation of the TENAX model — a non-stationary, non-asymptotic statistical framework for estimating extreme sub-hourly precipitation return levels using temperature as a covariate, grounded in Clausius–Clapeyron physics.

I am the main maintainer of this repository. Beyond the core implementation, I built the full [ReadTheDocs documentation](https://pytenax.readthedocs.io/en/latest/) including background theory, API reference, and Jupyter notebook tutorials. The package also includes a **SMEV** (Simplified Metastatistical Extreme Value) class and a **Weibull tail hypothesis test**.

> **Note:** The TENAX methodology was developed and published by Marra et al. (2024). A MATLAB reference implementation is available on Zenodo (DOI: [10.5281/zenodo.8332232](https://doi.org/10.5281/zenodo.8332232)). This Python package is a collaborative project — full details in the documentation.

---

## How It Works

The model integrates three components:

**1. Magnitude model W(x; T)** — a left-censored Weibull distribution with temperature-dependent parameters, capturing the Clausius–Clapeyron scaling of precipitation intensities.

<figure>
  <img src="/products/pytenax/img/fig_magnitude.jpg" alt="Magnitude model" style="max-width:100%;">
  <figcaption><em>Fitted Weibull quantiles (85th–99.9th percentile) against observed 10-minute precipitation as a function of temperature. Dashed line: left-censoring threshold.</em></figcaption>
</figure>

**2. Temperature model g(T)** — a generalized Gaussian distribution fitted to temperatures preceding peak intensities.

<figure>
  <img src="/products/pytenax/img/fig_temperature.jpg" alt="Temperature model" style="max-width:75%;">
  <figcaption><em>Fitted generalized Gaussian (blue) against observed event temperature distribution (red dashed).</em></figcaption>
</figure>

**3. Return level estimation** — the two models are integrated via Monte Carlo sampling to produce return level curves with bootstrap uncertainty.

<figure>
  <img src="/products/pytenax/img/fig_returnlevels.jpg" alt="Return level curve" style="max-width:100%;">
  <figcaption><em>TENAX return level curve with bootstrap uncertainty envelope against observed annual maxima for 10-minute precipitation (station Aadorf).</em></figcaption>
</figure>

For the full API reference and step-by-step tutorials, see the [documentation](https://pytenax.readthedocs.io/en/latest/).

---

## Methodology Citation

Marra, F., Koukoula, M., Canale, A., and Peleg, N. (2024).
*Predicting extreme sub-hourly precipitation intensification based on temperature shifts.*
Hydrology and Earth System Sciences, 28, 375–389.
[https://doi.org/10.5194/hess-28-375-2024](https://doi.org/10.5194/hess-28-375-2024)

</div>