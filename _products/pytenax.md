---
title: pyTENAX
subtitle: Temperature-dependent extreme precipitation modeling in Python
layout: page
show_sidebar: false
sort_position: 1
image: /products/pytenax/img/fig_returnlevels.jpg
---

<a class="button is-dark is-small" href="https://github.com/PetrVey/pyTENAX" target="_blank">View on GitHub</a>
&nbsp;
<a class="button is-light is-small" href="https://pytenax.readthedocs.io/en/latest/" target="_blank">Documentation</a>

<br><br>

<h2>About</h2>

<p>
  <strong>pyTENAX</strong> is a Python implementation of the TENAX model — a non-stationary, non-asymptotic statistical framework for estimating extreme sub-hourly precipitation return levels using temperature as a covariate, grounded in Clausius–Clapeyron physics.
</p>

<p>
  I am the main maintainer of this repository. Beyond the core implementation, I built the full <a href="https://pytenax.readthedocs.io/en/latest/" target="_blank">ReadTheDocs documentation</a> including background theory, API reference, and Jupyter notebook tutorials. The package also includes a <strong>SMEV</strong> (Simplified Metastatistical Extreme Value) class and a <strong>Weibull tail hypothesis test</strong>.
</p>

<article class="message is-info">
  <div class="message-body">
    <strong>Note:</strong> The TENAX methodology was developed and published by Marra et al. (2024). A MATLAB reference implementation is available on Zenodo (DOI: <a href="https://doi.org/10.5281/zenodo.8332232" target="_blank">10.5281/zenodo.8332232</a>). This Python package is a collaborative project — full details in the documentation.
  </div>
</article>

<hr>

<h2>How It Works</h2>

<p>The model integrates three components to estimate return levels:</p>

<h3>1. Magnitude Model W(x; T)</h3>

<p>
  A left-censored <strong>Weibull distribution</strong> characterizes precipitation event intensities at temperature T. The scale parameter follows exponential Clausius–Clapeyron dependence: λ(T) = λ₀·e<sup>aT</sup>. The shape parameter κ(T) = κ₀ + bT captures how scaling varies across quantiles.
</p>

<figure>
  <img src="/products/pytenax/img/fig_magnitude.jpg" alt="Magnitude model" style="max-width:100%;">
  <figcaption><em>Fitted Weibull quantiles (85th–99.9th percentile) against observed 10-minute precipitation as a function of temperature. Dashed line: left-censoring threshold.</em></figcaption>
</figure>

<h3>2. Temperature Model g(T)</h3>

<p>
  A <strong>generalized Gaussian distribution</strong> (β=4) fitted to temperatures preceding peak intensities, estimated via maximum likelihood.
</p>

<figure>
  <img src="/products/pytenax/img/fig_temperature.jpg" alt="Temperature model" style="max-width:75%;">
  <figcaption><em>Fitted generalized Gaussian (blue) against observed event temperature distribution (red dashed). μ = 9.82°C, σ = 12.36.</em></figcaption>
</figure>

<h3>3. Return Level Estimation</h3>

<p>
  The marginal distribution F(x) = ∫W(x; T)·g(T)dT is computed by <strong>Monte Carlo integration</strong>, producing return level curves with bootstrap uncertainty.
</p>

<figure>
  <img src="/products/pytenax/img/fig_returnlevels.jpg" alt="Return level curve" style="max-width:100%;">
  <figcaption><em>TENAX return level curve with bootstrap uncertainty envelope against observed annual maxima for 10-minute precipitation (station Aadorf).</em></figcaption>
</figure>

<p>For the full API reference and step-by-step tutorials, see the <a href="https://pytenax.readthedocs.io/en/latest/" target="_blank">documentation</a>.</p>

<hr>

<h2>Methodology Citation</h2>

<p>
  Marra, F., Koukoula, M., Canale, A., and Peleg, N. (2024).<br>
  <em>Predicting extreme sub-hourly precipitation intensification based on temperature shifts.</em><br>
  Hydrology and Earth System Sciences, 28, 375–389.<br>
  <a href="https://doi.org/10.5194/hess-28-375-2024" target="_blank">https://doi.org/10.5194/hess-28-375-2024</a>
</p>