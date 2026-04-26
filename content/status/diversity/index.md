+++
title = "Species Diversity"
date = "2026-01-26"
+++

**What is it?**
A diverse urban ecosystem is crucial to prevent the dominance of just a few tree species.
This not only enhances aesthetic value but also ensures the urban forest is more resilient to pests and diseases.

**The Standard**
The widely accepted standard is the [10/20/30 Santamour rule][2], which states that no single species should make up more than 10% of the population, no single genus more than 20%, and no single family more than 30%.
This corresponds to a [Gini-Simpson Index][1] value of 0.9 to 1.0.
While such high values are rare in urban environments, striving for them improves ecological resilience.

**Current Status**
Yerevan's current Gini-Simpson index is **{{ simpson_index() }}** which indicates a healthy level of diversity.
While there is room for improvement, Yerevan is avoiding the "green desert" trap, making it unlikely that a single pest outbreak would catastrophically impact the city's greenery.

{{ simpson_chart() }}

> **Note:** This index is calculated based on trees [inspected by volunteers][3]. Although the dataset currently covers approximately 10,000 trees, this sample size is sufficient for a reliable diversity estimate.

> **Important:** This value reflects the city-wide average. While the city's aggregate diversity is robust, individual districts may still lack diversity and remain vulnerable.

[1]: https://en.wikipedia.org/wiki/Diversity_index#Gini%E2%80%93Simpson_index
[2]: https://www.semanticscholar.org/paper/TREES-FOR-URBAN-PLANTING-%3A-DIVERSITY-UNIFORMITY-%2C-Santamour/26a24c5361ce6d6e618a9fa307c4a34a3169e309
[3]: https://yerevan.treemaps.app/stats/species
