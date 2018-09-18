+++
# Custom widget.
# An example of using the custom widget to create your own homepage section.
# To create more sections, duplicate this file and edit the values below as desired.
widget = "custom"
active = true
date = "2018-01-04T00:00:00"

# Note: a full width section format can be enabled by commenting out the `title` and `subtitle` with a `#`.
title = "Phd Thesis"
subtitle = ""

tags = ["Comparative-evaluation","Beat-tracking","Tempo"]
# Order that this section will appear in.
weight = 70

+++
# Comparative evaluation and combination of automatic rhythm description systems
Zapata, Jose R. (2013). [Comparative evaluation and combination of automatic rhythm description systems](http://www.tdx.cat/bitstream/handle/10803/123822/tjrzg2.pdf?sequence=5&isAllowed=y). Ph.D. thesis (Information and Communication Technologies), Universitat Pompeu Fabra, Barcelona, Spain, 2013.

- [[TDX.cat]](http://www.tdx.cat/handle/10803/123822)
[[PDF](http://www.tdx.cat/bitstream/handle/10803/123822/tjrzg2.pdf?sequence=5&isAllowed=y)]
[[MTG](http://mtg.upf.edu/node/3115)]
[[Slides](https://goo.gl/vDJxCN)]


### Thesis advisor
- Dr. [Emilia Gómez](https://emiliagomez.com/), Universitat Pompeu Fabra ([MTG](https://www.upf.edu/web/mtg), [UPF](https://www.upf.edu/en/))

### Defense board
- Dr. [Xavier Serra](https://www.upf.edu/web/xavier-serra),  Universitat Pompeu Fabra ([MTG](https://www.upf.edu/web/mtg), [UPF](https://www.upf.edu/en/))
- Dr. [Fabien Gouyon](http://www.fabiengouyon.org/), Institute for Systems and Computer Engineering of Porto ([SMC](http://smc.inescporto.pt/), [INESC Porto](https://www.inesctec.pt/en))
- Dr. [Juan Pablo Bello](https://wp.nyu.edu/jpbello/), New York University ([MARL](https://steinhardt.nyu.edu/marl/), [NYU](http://www.nyu.edu/))


## Abstract

The automatic analysis of musical rhythm from audio, and more specifically tempo and beat tracking, is one of the fundamental open research problems
in Music Information Retrieval (MIR) research. Automatic beat tracking is a valuable tool for the solution of other MIR problems, because enables the
beat-synchronous analysis of music for tasks such as: structural segmentation, chord detection, music similarity, cover song detection, automatic remixing and interactive music systems. Even though automatic rhythm description is a relatively mature research topic in MIR and various algorithms have been proposed, tempo estimation and beat tracking remain an unsolved problem.
Recent comparative studies of automatic rhythm description systems suggest that there has been little improvement in the state of the art over the last few years. In this thesis, we describe a new method for the extraction of beat times with a confidence value from music audio, based on the measurement of mutual agreement between a committee of beat tracking systems. Additionally, we present an open source approach which only requires a single beat tracking model and uses multiple onset detection functions for the mutual agreement.
The method can also be used to identify music samples that are challenging for beat tracking without the need for ground truth annotations. Using the proposed method, we compiled a new dataset that consist of pieces that are difficult for state-of-the-art beat tracking algorithms. Through an international evaluation framework we show that our method yields the highest AMLc and AMLt accuracies obtained in this evaluation to date. Moreover, we compare our method to 20 reference systems using the largest existing annotated dataset for beat tracking and show that it outperforms all of the other systems under all the evaluation criteria used. In the thesis we also conduct an extensive comparative evaluation and combination of automatic rhythm description systems. We evaluated 32 tempo estimation and 16 beat tracking state-of-the-art systems in order to identify their characteristics and investigated how they can be combined to improve performance. Finally, we proposed and evaluated the use of voice suppression algorithms in music signals with predominant vocals in order to improve the performance of existing beat tracking methods.

[//]: <> (The automatic analysis of musical rhythm from audio, and more specifically tempo and beat tracking, is one of the fundamental open research problems in Music Information Retrieval (MIR) research. Automatic beat tracking is a valuable tool for the solution of other MIR problems, as it enables beat- synchronous analysis of different music tasks. Even though automatic rhythm description is a relatively mature research topic in MIR tempo estimation and beat tracking remain an unsolved problem. We describe a new method for the extraction of beat times with a confidence value from music audio, based on the measurement of mutual agreement between a committee of beat tracking systems. The method can also be used identify music samples that are challenging for beat tracking without the need for ground truth annotations. we also conduct an extensive comparative evaluation of 32 tempo estimation and 16 beat tracking systems.)


