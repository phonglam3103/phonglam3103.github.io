---
title: "Phong Lam - Useful scripts"
layout: gridlay2
excerpt: "Phong Lam - Useful scripts"
sitemap: false
permalink: /teaching/
---

# Scripts

These are useful scripts I usually  used in my research. Will try to update the list regularly.
<div class="row">
<div class="well">
  #### ROC curve and enrichment curve plotting
  **Purpose:** To evaluate the capibility of a virtual screening method in enrichment actives among the pool of actives and inactives.
  ** Script:** <a href="https://colab.research.google.com/github/phonglam3103/Cheminformatics/blob/main/Multiple_ROC_AUC_generalized.ipynb"> Google Colab</a>
</div>
</div>

{% for course in site.data.teaching %}

<div class="row">
<div class="well">

#### {{ course.title }} 

**Level:** {{course.level}}

**Term:** {{course.term}}

**Location:** {{course.location}}

with **Teachers:** {{course.teachers}}

<a data-toggle="collapse" href="#{{key}}-about" class="btn-about" role="button">**Course Content**</a>
<div class="collapse" id="{{key}}-about">
<div class="well-about">
{{course.about}}
</div> </div>
</div>
</div>

{% endfor %}
