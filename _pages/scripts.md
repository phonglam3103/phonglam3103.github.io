---
title: "Phong Lam - Useful scripts"
layout: gridlay2
excerpt: "Phong Lam - Useful scripts"
sitemap: false
permalink: /scripts/
---

# Scripts

These are useful scripts I usually  used in my research. Will try to update the list regularly.

<div class="row">
<div class="well"> 
  
#### ROC curve and enrichment curve plotting
  
  **Purpose:** To evaluate the capability of a virtual screening method in enrichment actives among the pool of actives and inactives.
  
  **Script:** <a href="https://colab.research.google.com/github/phonglam3103/Cheminformatics/blob/main/Multiple_ROC_AUC_generalized.ipynb"> Google Colab</a>
</div>
</div>

<div class="row">
<div class="well"> 
  
#### AutoDock Vina batch screening and analysis
  
  **Purpose:** Automate the molecular docking process using AutoDock Vina. The script was written in Bash therefore natively compatible with Linux. For Windows, I recommend installing and setting up a path to cygwin64/bash.exe to implement the script. 
  
  **Scripts:** <a href="https://github.com/phonglam3103/Cheminformatics/tree/main/Molecular%20docking%20scripts"> GitHub repository</a>
 
</div>
</div>

<div class="row">
<div class="well"> 
  
#### GROMACS MD trajectory analysis
  
  **Purpose:** I wrote this notebook to automate the visual analysis of MD trajectories from the GROMACS program. The script assumes that you put it in the parent folder in which the subfolders are different protein-ligand complexes that have undergone MD simulation and have generated the necessary .xvg files for visualization.
  
  **Scripts:** <a href="https://github.com/phonglam3103/Cheminformatics/blob/main/Visuallization%20notebooks/plot.ipynb"> GitHub repository</a>
 
</div>
</div>
