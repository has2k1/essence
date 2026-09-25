# Workshop data

## Census

The census files contain Uganda's population by tribe. `bad/` reproduces
the provisional report; `good/` contains the corrected final figures.
See [the provisional data notes](bad/README.md) for the known differences.

`census_long.csv` combines both versions for plotting. Each row contains
a tribe, year, population and report version.

Source: [UBOS National Population and Housing Census 2024](https://www.ubos.org/wp-content/uploads/2024/12/National-Population-and-Housing-Census-2024-Final-Report-Volume-1-Main.pdf).

## Gapminder Africa

`gapminder_africa.csv` contains life expectancy, population and GDP per
person for African countries from 1952 to 2007.
`gapminder_africa_2007.csv` contains only the 2007 figures.

We added the `region` column using the
[UN M49 regions](https://unstats.un.org/unsd/methodology/m49/), with
"Middle Africa" renamed "Central Africa".

Source: [Gapminder](https://www.gapminder.org/data/), through the
[gapminder R package](https://github.com/jennybc/gapminder).

## Afrobeats

`afrobeats.csv` contains Spotify monthly listener counts and each artist's
highest recorded count, in millions. The current figures are from
1 October 2026. Countries record the artists' nationalities.

Refresh the listener counts before each workshop. Update the date in
`04-closing.qmd`, both in the column description and in the example table's
subtitle.

Source: [kworb.net](https://kworb.net/spotify/listeners.html), which collects
figures from Spotify artist pages.
