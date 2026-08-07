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

## Mobile money

Percentage of adults (15+) with a mobile money account, by country, 2021.

Source: [World Bank Global Findex Database 2021](https://www.worldbank.org/en/publication/globalfindex)

## Afrobeats

Monthly Spotify listeners for top Afrobeats artists, approximate figures as
of early 2025. Verify before the workshop.

Source: Spotify artist pages
