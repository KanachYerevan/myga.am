+++
title = "Species Diversity"
date = "2026-01-26"
+++
**What is it?**
It is important that the city has a diverse ecosystem, without a few tree species dominating it.
This not only has aesthetic value but also guarantees that the urban forest is less vulnerable to pests.

**The Standard.**
The widely accepted standard is the [10/20/30 Santamour rule][2], which states that no single species should make up more than 10% of the population, no single genus should make up more than 20%, and no single family should make up more than 30%.
This corresponds to a [Gini-Simpson Index][1] value of 0.9 to 1.0.
Values this high are rarely found in real-life cities, but the closer we get, the better.

**Current Status.**
Yerevan currently has a Gini-Simpson index value of **{{ simpson_index() }}**, which is good.
There is much room for improvement, but Yerevan is not a "green desert," and it is unlikely that any single pest outbreak will have a catastrophic effect on the city's greenery.

{{ simpson_chart() }}

Please note that we calculate this index based on the trees [inspected by volunteers][3].
While we only have data on around 10k trees, this is enough to calculate the diversity.

Also, please note that this value is currently city-wide.
While the city as a whole is not in danger, individual districts might very well be green deserts.

[1]: https://en.wikipedia.org/wiki/Diversity_index#Gini%E2%80%93Simpson_index
[2]: https://www.semanticscholar.org/paper/TREES-FOR-URBAN-PLANTING-%3A-DIVERSITY-UNIFORMITY-%2C-Santamour/26a24c5361ce6d6e618a9fa307c4a34a3169e309
[3]: https://yerevan.treemaps.app/
