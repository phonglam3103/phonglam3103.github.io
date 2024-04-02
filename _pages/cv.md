---
title: "Phong Lam - CV"
layout: cv
excerpt: "Phong Lam - CV"
sitemap: false
permalink: /cv/
---

<embed src="{{ site.url }}{{ site.baseurl }}/assets/PhongLam_CV.pdf" width="500px" height="600px" />

<div class="row">

<div class="col-sm-2 clearfix vcenter">
<img src="{{ site.url }}{{ site.baseurl }}/images/logopic/UU_logo_4f125px.png" style="width: 125px">

</div>

<div class="col-sm-2 clearfix vcenter">
<img src="{{ site.url }}{{ site.baseurl }}/images/logopic/KAW_Logotype_Large.png" style="width: 125px">

</div>

<div class="col-sm-2 clearfix vcenter">
<img src="{{ site.url }}{{ site.baseurl }}/images/logopic/svart_fyrkant_eng.png" style="width: 120px">

</div>

<div class="col-sm-2 clearfix vcenter">
<img src="{{ site.url }}{{ site.baseurl }}/images/logopic/ssf_gb_rgb-300x247.png" style="width: 124px">
</div>
</div>

<div class="row">

<div class="col-sm-2 clearfix vcenter">
<img src="{{ site.url }}{{ site.baseurl }}/images/logopic/energimyndigheten_engelsklogo_rgb.png" style="width: 120px">
</div>

<div class="col-sm-2 clearfix vcenter">
<img src="{{ site.url }}{{ site.baseurl }}/images/logopic/Vinnova_green_payoff_ENG_RGB.png" style="width: 120px">
</div>

<div class="col-sm-2 clearfix vcenter">
<img src="{{ site.url }}{{ site.baseurl }}/images/logopic/LOGO_essence.png" style="width: 120px">
</div>


</div>

Their funding supports our work in research, education, and outreach, not the least through our scientific projects.

### Ongoing projects

{% for project in site.data.project %}

{% if project.ongoing == 1 %}
<div class="row">
<div class="well">

#### {{ project.title }} ({{ project.period}})

**Call:** {{project.category}}, *funded by the* {{ project.agency}}

**Awarded to:** {{project.lead}}

**USLC Members:** {{project.member}}

<a data-toggle="collapse" href="#{{project.key}}-bib"  class="btn-abstract" style="text-decoration:none; color:#ebebeb; hover:#ebebeb;" role="button" aria-expanded="false">**Popular Abstract**</a>
<div class="collapse" id="{{project.key}}-bib"><div class="well-abs">
{{ project.summary }}
</div></div>
</div>
</div>

{% endif %}

{% endfor %}


<h4><a href="{{ site.url }}{{ site.baseurl }}/allprojects.html">... see all Projects</a></h4>
