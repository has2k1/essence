# Data

## Census data (`good/`, `bad/`, `census_long.csv`)

Uganda 2024 Census tribal population, as published in the provisional report
(`bad/`) and the corrected final report (`good/`). See `bad/README.md` for
details of the swap.

`census_long.csv` combines both into long format —
`tribe, year, population, version` (60 rows) — for plotting.

Source: [UBOS National Population and Housing Census 2024](https://www.ubos.org/wp-content/uploads/2024/12/National-Population-and-Housing-Census-2024-Final-Report-Volume-1-Main.pdf)

## Gapminder Africa

Country-level life expectancy, population, and GDP per capita for 52 African
countries, 1952–2007 (`gapminder_africa.csv`) and the 2007 snapshot
(`gapminder_africa_2007.csv`).

The `region` column is not from Gapminder: it assigns each country to one
of five regions following the
[UN M49 sub-regions](https://unstats.un.org/unsd/methodology/m49/), with
"Middle Africa" renamed "Central Africa".

Source: [Gapminder](https://www.gapminder.org/data/), via the
[gapminder R package](https://github.com/jennybc/gapminder)

## Afrobeats

Spotify monthly listeners, now and at their all-time peak, in millions,
for 13 artists, as of 1 October 2026. Monthly listeners change daily, so
refresh the figures before each workshop, then update the date in
`04-closing.qmd` (the column description and the table subtitle).

Source: [kworb.net, Spotify top artists by monthly listeners](https://kworb.net/spotify/listeners.html),
which collects the figures from Spotify artist pages. Countries are the
artists' nationalities.
