+++
title = "SMC Beat tracking Dataset"
date = 2012-05-27T13:30:13-05:00
draft = false

# Tags: can be used for filtering projects.
# Example: `tags = ["machine-learning", "deep-learning"]`
tags = ["Beat tracking","Dataset","Mirex","Open-source"]

# Project summary to display on homepage.
summary = "Este dataset de Beat tracking contiene 217 fragmentos de aproximadamente 40 seg cada uno, de los cuales 19 son *fáciles* y los 198 restantes son *dificiles*. Este conjunto de datos ha sido diseñado para técnicas radicalmente nuevas que pueden lidiar con desafiantes situaciones de beat tracking como: acompañamiento suave, tiempo expresivo, cambios de compás, tempo lento, calidad de sonido pobre, etc. Más detalles en [Selective Sampling for Beat Tracking Evaluation](https://joserzapata.github.io/publication/selectivesampling/)"

# Optional image to display on homepage.
image_preview = ""

# Optional external URL for project (replaces project detail page).
external_link = "http://smc.inescporto.pt/data/SMC_MIREX.zip"

# Does the project detail page use math formatting?
math = false

# Does the project detail page use source code highlighting?
highlight = true

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++
This dataset contains 217 excerpts around 40s each, of which 19 are "easy" and the remaining 198 are "hard". The harder excerpts were drawn from the following musical styles: Romantic music, ﬁlm soundtracks, blues, chanson and solo guitar.

This dataset has been designed for radically new techniques which can contend with challenging beat tracking situations like: quiet accompaniment, expressive timing, changes in time signature, slow tempo, poor sound quality etc. So, if your beat tracker likes a 4/4 time-signature with a steady tempo and needs clear percussive onsets, don't expect it to do very well! But don't be deterred, this is for the good of beat tracking.

This dataset includes:

Beat annotations and supporting meta-data
Audio excerpts

Update 5th August 2014: please note the annotations for excerpts 056, 137, 153, 203 and 257 have been updated to remove the final beat annotations which were out of range. Thanks to Andy Lambert for pointing this out. Please see sub-folder SMC_MIREX_Annotations_05_08_2014 in the .zip file for the latest version of the annotations.

