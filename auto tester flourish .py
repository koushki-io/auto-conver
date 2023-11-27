import json
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import os
import time
from bs4 import BeautifulSoup


# input the directory which the .html files are located
directory = fr"C:\Users\pro ai\Desktop\sample flurish\sample flurish"

# if tring to duplicate a certan project set test value true and enter the flourish id in sample - example id.html
test = False
sample = "12770886"










apiKey = 'xd1bVlrOnIz9kEjO_9J07NINIPyhxWWGdftkKJqm-aRtraQT'


plotsetChartIds = [ { "id": "funnel-chart", "name": "Funnel", "revision": 46, "isPremium": False }, { "id": "heatmap-2", "name": "Heatmap", "revision": 80, "isPremium": False }, { "id": "chord", "name": "Chord", "revision": 93, "isPremium": False }, { "id": "treemap", "name": "Stock Market Map", "revision": 34, "isPremium": False }, { "id": "sankey", "name": "Sankey", "revision": 104, "isPremium": False }, { "id": "force-directed", "name": "Force-directed Graph", "revision": 56, "isPremium": False }, { "id": "curve-radar-chart", "name": "Radar Chart", "revision": 44, "isPremium": False }, { "id": "parliament-chart", "name": "Parliament Chart", "revision": 32, "isPremium": False }, { "id": "timeline-bubble-chart", "name": "Hans Rosling Chart", "revision": 29, "isPremium": False }, { "id": "dot-plot", "name": "Connected Dots", "revision": 80, "isPremium": False }, { "id": "table", "name": "Table", "revision": 66, "isPremium": False }, { "id": "usa-states", "name": "USA (states) Choropleth", "revision": 151, "isPremium": False }, { "id": "donut-chart", "name": "Donut Chart", "revision": 109, "isPremium": False }, { "id": "sunburst", "name": "Sunburst", "revision": 72, "isPremium": False }, { "id": "scatter-plot-with-groups", "name": "Scatter Plot", "revision": 88, "isPremium": False }, { "id": "bubble-chart-new", "name": "Bubble Chart", "revision": 61, "isPremium": False }, { "id": "india-provinces", "name": "India (states) Choropleth", "revision": 43, "isPremium": False }, { "id": "germany-states", "name": "Germany (states) Choropleth", "revision": 34, "isPremium": False }, { "id": "china-porvinces", "name": "China (provinces) Choropleth", "revision": 33, "isPremium": False }, { "id": "japan-provinces", "name": "Japan (prefectures) Choropleth", "revision": 32, "isPremium": False }, { "id": "uk", "name": "UK (districts) Choropleth", "revision": 28, "isPremium": False }, { "id": "france-departments-new", "name": "France (departments) Choropleth", "revision": 33, "isPremium": False }, { "id": "europe", "name": "Europe (countries) Choropleth", "revision": 46, "isPremium": False }, { "id": "brazil", "name": "Brazil (states) Choropleth", "revision": 30, "isPremium": False }, { "id": "italy", "name": "Italy (provinces) Choropleth", "revision": 29, "isPremium": False }, { "id": "world", "name": "World (countries) Choropleth", "revision": 103, "isPremium": False }, { "id": "africa-countries-new", "name": "Africa (countries) Choropleth", "revision": 49, "isPremium": False }, { "id": "world-continents", "name": "World (continents) Choropleth", "revision": 35, "isPremium": False }, { "id": "asia", "name": "Asia (countries) Choropleth", "revision": 36, "isPremium": False }, { "id": "north-america", "name": "North America (countries) Choropleth", "revision": 25, "isPremium": False }, { "id": "south-america", "name": "South America (countries) Choropleth", "revision": 26, "isPremium": False }, { "id": "sweden-new", "name": "Sweden (counties) Choropleth", "revision": 25, "isPremium": False }, { "id": "south-korea", "name": "South Korea (provinces) Choropleth", "revision": 26, "isPremium": False }, { "id": "russia-federal-subjects", "name": "Russia (federal subjects) Choropleth", "revision": 29, "isPremium": False }, { "id": "canada-states", "name": "Canada (provinces and territories) Choropleth", "revision": 30, "isPremium": False }, { "id": "australia-states", "name": "Australia (states) Choropleth", "revision": 29, "isPremium": False }, { "id": "indonesia-provinces", "name": "Indonesia (provinces) Choropleth", "revision": 25, "isPremium": False }, { "id": "mexico-states", "name": "Mexico (states) Choropleth", "revision": 28, "isPremium": False }, { "id": "turkey-provinces", "name": "Turkey (provinces) Choropleth", "revision": 23, "isPremium": False }, { "id": "circle-packing-2", "name": "Circles", "revision": 83, "isPremium": False }, { "id": "saudi-arabia", "name": "Saudi Arabia (provinces) Choropleth", "revision": 27, "isPremium": False }, { "id": "ukraine", "name": "Ukraine (regions) Choropleth", "revision": 30, "isPremium": False }, { "id": "netherlands", "name": "Netherlands (provinces) Choropleth", "revision": 26, "isPremium": False }, { "id": "pie-chart-new", "name": "Pie Chart", "revision": 88, "isPremium": False }, { "id": "argentina-provinces", "name": "Argentina (provinces) Choropleth", "revision": 31, "isPremium": False }, { "id": "belgium-provinces", "name": "Belgium (provinces) Choropleth", "revision": 25, "isPremium": False }, { "id": "poland-provinces", "name": "Poland (provinces) Choropleth", "revision": 24, "isPremium": False }, { "id": "qatar-municipalities", "name": "Qatar (municipalities) Choropleth", "revision": 26, "isPremium": False }, { "id": "thailand-provinces", "name": "Thailand (provinces) Choropleth", "revision": 24, "isPremium": False }, { "id": "switzerland-cantons", "name": "Switzerland (cantons) Choropleth", "revision": 24, "isPremium": False }, { "id": "iran-provinces", "name": "Iran (provinces) Choropleth", "revision": 61, "isPremium": False }, { "id": "area-charttest", "name": "Area Chart", "revision": 69, "isPremium": False }, { "id": "racebar", "name": "Racing Bars", "revision": 158, "isPremium": False }, { "id": "latin-america", "name": "Latin America (countries) Choropleth", "revision": 25, "isPremium": False }, { "id": "middle-east", "name": "Middle East (countries) Choropleth", "revision": 26, "isPremium": False }, { "id": "oceania", "name": "Oceania (countries) Choropleth", "revision": 24, "isPremium": False }, { "id": "mediterranean-sea", "name": "Mediterranean Sea (countries) Choropleth", "revision": 26, "isPremium": False }, { "id": "central-america", "name": "Central America (countries) Choropleth", "revision": 26, "isPremium": False }, { "id": "south-east-asia", "name": "South East Asia (countries) Choropleth", "revision": 25, "isPremium": False }, { "id": "west-africa", "name": "West Africa (countries) Choropleth", "revision": 25, "isPremium": False }, { "id": "austria-states", "name": "Austria (states) Choropleth", "revision": 30, "isPremium": False }, { "id": "line-chart2", "name": "Line Chart", "revision": 212, "isPremium": False }, { "id": "norway-counties", "name": "Norway (counties) Choropleth", "revision": 25, "isPremium": False }, { "id": "uaeemirates", "name": "UAE (emirates) Choropleth", "revision": 27, "isPremium": False }, { "id": "nigeria-states", "name": "Nigeria (states) Choropleth", "revision": 26, "isPremium": False }, { "id": "israel-districts", "name": "Israel (districts) Choropleth", "revision": 26, "isPremium": False }, { "id": "south-africa-provinces", "name": "South Africa (provinces) Choropleth", "revision": 25, "isPremium": False }, { "id": "ireland-counties", "name": "Ireland (counties) Choropleth", "revision": 25, "isPremium": False }, { "id": "denmark-provinces", "name": "Denmark (provinces) Choropleth", "revision": 26, "isPremium": False }, { "id": "singapore-regions", "name": "Singapore (regions) Choropleth", "revision": 25, "isPremium": False }, { "id": "malaysia-states", "name": "Malaysia (states) Choropleth", "revision": 27, "isPremium": False }, { "id": "colombia-departments", "name": "Colombia (departments) Choropleth", "revision": 27, "isPremium": False }, { "id": "philippines-provinces", "name": "Philippines (provinces) Choropleth", "revision": 27, "isPremium": False }, { "id": "pakistan-provinces", "name": "Pakistan (provinces) Choropleth", "revision": 25, "isPremium": False }, { "id": "histogram", "name": "Histogram", "revision": 40, "isPremium": False }, { "id": "new-york-boroughs", "name": "New York (boroughs) Choropleth", "revision": 27, "isPremium": False }, { "id": "alabama-counties", "name": "Alabama (counties) Choropleth", "revision": 29, "isPremium": False }, { "id": "alaska-boroughs", "name": "Alaska (boroughs) Choropleth", "revision": 29, "isPremium": False }, { "id": "stacked-area-charttest", "name": "Stacked Area Chart", "revision": 49, "isPremium": False }, { "id": "arizona-counties", "name": "Arizona (counties) Choropleth", "revision": 30, "isPremium": False }, { "id": "stacked-area-chart-percentage-test", "name": "Stacked Area Chart (prop)", "revision": 29, "isPremium": False }, { "id": "arkansas-counties", "name": "Arkansas (counties) Choropleth", "revision": 29, "isPremium": False }, { "id": "usa-counties", "name": "USA (counties) Choropleth", "revision": 39, "isPremium": False }, { "id": "violin-chart", "name": "Violin Chart", "revision": 27, "isPremium": False }, { "id": "ridge-plot", "name": "Ridgeline Plot", "revision": 28, "isPremium": False }, { "id": "california-counties", "name": "California (counties) Choropleth", "revision": 29, "isPremium": False }, { "id": "colorado-counties", "name": "Colorado (counties) Choropleth", "revision": 29, "isPremium": False }, { "id": "connecticut-counties", "name": "Connecticut (counties) Choropleth", "revision": 29, "isPremium": False }, { "id": "delaware-counties", "name": "Delaware (counties) Choropleth", "revision": 28, "isPremium": False }, { "id": "florida-counties", "name": "Florida (counties) Choropleth", "revision": 28, "isPremium": False }, { "id": "georgia-counties", "name": "Georgia (counties) Choropleth", "revision": 28, "isPremium": False }, { "id": "hawaii-counties", "name": "Hawaii (counties) Choropleth", "revision": 28, "isPremium": False }, { "id": "idaho-counties", "name": "Idaho (counties) Choropleth", "revision": 28, "isPremium": False }, { "id": "beeswarm", "name": "Beeswarm", "revision": 28, "isPremium": False }, { "id": "illinois-counties", "name": "Illinois (counties) Choropleth", "revision": 27, "isPremium": False }, { "id": "indiana-counties", "name": "Indiana (counties) Choropleth", "revision": 27, "isPremium": False }, { "id": "iowa-counties", "name": "Iowa (counties) Choropleth", "revision": 27, "isPremium": False }, { "id": "kansas-counties", "name": "Kansas (counties) Choropleth", "revision": 27, "isPremium": False }, { "id": "kentucky-counties", "name": "Kentucky (counties) Choropleth", "revision": 27, "isPremium": False }, { "id": "louisiana-counties", "name": "Louisiana (counties) Choropleth", "revision": 27, "isPremium": False }, { "id": "maine-counties", "name": "Maine (counties) Choropleth", "revision": 26, "isPremium": False }, { "id": "maryland-counties", "name": "Maryland (counties) Choropleth", "revision": 27, "isPremium": False }, { "id": "massachusetts-counties", "name": "Massachusetts (counties) Choropleth", "revision": 27, "isPremium": False }, { "id": "michigan-counties", "name": "Michigan (counties) Choropleth", "revision": 27, "isPremium": False }, { "id": "minnesota-counties", "name": "Minnesota (counties) Choropleth", "revision": 28, "isPremium": False }, { "id": "mississippi-counties", "name": "Mississippi (counties) Choropleth", "revision": 28, "isPremium": False }, { "id": "missouri-counties", "name": "Missouri (counties) Choropleth", "revision": 26, "isPremium": False }, { "id": "montana-counties", "name": "Montana (counties) Choropleth", "revision": 27, "isPremium": False }, { "id": "nebraska-counties", "name": "Nebraska (counties) Choropleth", "revision": 27, "isPremium": False }, { "id": "nevada-counties", "name": "Nevada (counties) Choropleth", "revision": 28, "isPremium": False }, { "id": "new-hampshire-counties", "name": "New Hampshire (counties) Choropleth", "revision": 26, "isPremium": False }, { "id": "new-jersey-counties", "name": "New Jersey (counties) Choropleth", "revision": 27, "isPremium": False }, { "id": "new-mexico-counties", "name": "New Mexico (counties) Choropleth", "revision": 28, "isPremium": False }, { "id": "new-york-counties", "name": "New York (counties) Choropleth", "revision": 27, "isPremium": False }, { "id": "north-carolina-counties", "name": "North Carolina (counties) Choropleth", "revision": 28, "isPremium": False }, { "id": "north-dakota-counties", "name": "North Dakota (counties) Choropleth", "revision": 27, "isPremium": False }, { "id": "ohio-counties", "name": "Ohio (counties) Choropleth", "revision": 27, "isPremium": False }, { "id": "oklahoma-counties", "name": "Oklahoma (counties) Choropleth", "revision": 28, "isPremium": False }, { "id": "oregon-counties", "name": "Oregon (counties) Choropleth", "revision": 27, "isPremium": False }, { "id": "pennsylvania-counties", "name": "Pennsylvania (counties) Choropleth", "revision": 27, "isPremium": False }, { "id": "rhode-island-counties", "name": "Rhode Island (counties) Choropleth", "revision": 25, "isPremium": False }, { "id": "south-carolina-counties", "name": "South Carolina (counties) Choropleth", "revision": 26, "isPremium": False }, { "id": "south-dakota-counties", "name": "South Dakota (counties) Choropleth", "revision": 26, "isPremium": False }, { "id": "tennessee-counties", "name": "Tennessee (counties) Choropleth", "revision": 27, "isPremium": False }, { "id": "texas-counties", "name": "Texas (counties) Choropleth", "revision": 27, "isPremium": False }, { "id": "utah-counties", "name": "Utah (counties) Choropleth", "revision": 26, "isPremium": False }, { "id": "vermont-counties", "name": "Vermont (counties) Choropleth", "revision": 26, "isPremium": False }, { "id": "virginia-counties", "name": "Virginia (counties) Choropleth", "revision": 26, "isPremium": False }, { "id": "washington-counties", "name": "Washington (counties) Choropleth", "revision": 26, "isPremium": False }, { "id": "west-virginia-counties", "name": "West Virginia (counties) Choropleth", "revision": 26, "isPremium": False }, { "id": "wisconsin-counties", "name": "Wisconsin (counties) Choropleth", "revision": 25, "isPremium": False }, { "id": "wyoming-counties", "name": "Wyoming (counties) Choropleth", "revision": 26, "isPremium": False }, { "id": "histogram-kde", "name": "Histogram with KDE", "revision": 36, "isPremium": False }, { "id": "population-pyramid", "name": "Split Bars", "revision": 209, "isPremium": False }, { "id": "barchart-d3", "name": "Bar Chart", "revision": 435, "isPremium": False }, { "id": "columnchart-d3", "name": "columnchart-d3", "revision": 181, "isPremium": False }, { "id": "stacked-columnchart-d3", "name": "Stacked Column Chart", "revision": 134, "isPremium": False }, { "id": "stacked-barchart-d3", "name": "Stacked Bar Chart", "revision": 173, "isPremium": False }, { "id": "reaceline", "name": "Racing Lines", "revision": 83, "isPremium": False }, { "id": "stacked-barchart-percentage-d3", "name": "Stacked Bar (prop)", "revision": 124, "isPremium": False }, { "id": "stacked-columnchart-persentage-d3", "name": "Stacked Column (prop)", "revision": 100, "isPremium": False }, { "id": "word-cloud", "name": "Word Cloud", "revision": 72, "isPremium": False }, { "id": "grouped-columnchart-d3", "name": "Grouped Column Chart", "revision": 86, "isPremium": False }, { "id": "grouped-barchart-d3", "name": "Grouped Bar Chart", "revision": 105, "isPremium": False }, { "id": "mixed-barline-chart-d3", "name": "stacked grouped column Line Chart", "revision": 56, "isPremium": False }, { "id": "voronoi-treemap", "name": "Voronoi treemap", "revision": 101, "isPremium": False }, { "id": "usa-points", "name": "USA (events)", "revision": 5, "isPremium": False }, { "id": "usa-symbols", "name": "USA Symbols", "revision": 63, "isPremium": False }, { "id": "racing-bars", "name": "Racing Columns", "revision": 27, "isPremium": False }, { "id": "ploar-bar", "name": "Polar Bar", "revision": 66, "isPremium": False }, { "id": "radial-polarbar-d3", "name": "Radial Polar Bar", "revision": 53, "isPremium": False }, { "id": "boxplot-vertical", "name": "Boxplot Vertical", "revision": 29, "isPremium": False }, { "id": "stacked-polar-bar", "name": "Stacked Polar Bar", "revision": 63, "isPremium": False }, { "id": "boxplot-horizontal", "name": "Boxplot Horizontal", "revision": 32, "isPremium": False }, { "id": "bump-chart", "name": "Bump Chart", "revision": 39, "isPremium": False }, { "id": "image-pie", "name": "Image Pie chart", "revision": 50, "isPremium": False }, { "id": "life-expectancy", "name": "Curved Line Distribution", "revision": 22, "isPremium": False }, { "id": "usa-hexagons", "name": "USA (hexagons)", "revision": 3, "isPremium": False }, { "id": "premium-line-chart", "name": "Premium Line Chart", "revision": 60, "isPremium": False }, { "id": "simple-treemap", "name": "Simple Treemap", "revision": 68, "isPremium": False }, { "id": "andalusia-provinces", "name": "Andalusia (provinces) Choropleth", "revision": 24, "isPremium": False }, { "id": "spain-provinces", "name": "Spain (provinces) Choropleth", "revision": 20, "isPremium": False }, { "id": "portugal-subdivisions", "name": "Portugal (subdivisions) Choropleth", "revision": 20, "isPremium": False }, { "id": "czech-republic-regions", "name": "Czech Republic (regions) Choropleth", "revision": 20, "isPremium": False }, { "id": "finland-regions", "name": "Finland (regions) Choropleth", "revision": 19, "isPremium": False }, { "id": "greece-regions", "name": "Greece (regions) Choropleth", "revision": 19, "isPremium": False }, { "id": "hungary-regions", "name": "Hungary (regions) Choropleth", "revision": 20, "isPremium": False }, { "id": "taiwan-municipalities", "name": "Taiwan (municipalities) Choropleth", "revision": 19, "isPremium": False }, { "id": "bangladesh-districts", "name": "Bangladesh (districts) Choropleth", "revision": 19, "isPremium": False }, { "id": "chile-regions", "name": "Chile (regions) Choropleth", "revision": 23, "isPremium": False }, { "id": "romania-regions", "name": "Romania (regions) Choropleth", "revision": 19, "isPremium": False }, { "id": "peru-regions", "name": "Peru (regions) Choropleth", "revision": 19, "isPremium": False }, { "id": "treemap-with-category", "name": "Treemap with category", "revision": 41, "isPremium": False }, { "id": "world-countries", "name": "World (countries) Bubbles", "revision": 40, "isPremium": False }, { "id": "aniamted-bar-chart", "name": "Animated Bar Chart", "revision": 23, "isPremium": False }, { "id": "swarm", "name": "Swarm", "revision": 27, "isPremium": False }, { "id": "population", "name": "Population Pyramid", "revision": 46, "isPremium": False }, { "id": "polar-with-image", "name": "Polar bar (with change prop)", "revision": 32, "isPremium": False }, { "id": "heatmap-bar-chart", "name": "Heatmap List", "revision": 92, "isPremium": False }, { "id": "spiral-bubble", "name": "Spiral Bubble", "revision": 21, "isPremium": False }, { "id": "africa-countries-symbols", "name": "Africa (countries) Symbols", "revision": 16, "isPremium": False }, { "id": "argentina-provinces-symbols", "name": "Argentina (provinces) Symbols", "revision": 15, "isPremium": False }, { "id": "asia-countries-symbols", "name": "Asia (countries) Symbols", "revision": 14, "isPremium": False }, { "id": "australia-states-symbols", "name": "Australia (states) Symbols", "revision": 15, "isPremium": False }, { "id": "austria-states-symbols", "name": "Austria (states) Symbols", "revision": 14, "isPremium": False }, { "id": "bangladesh-districts-symbols", "name": "Bangladesh (districts) Symbols", "revision": 13, "isPremium": False }, { "id": "belgium-provinces-symbols", "name": "Belgium (provinces) Symbols", "revision": 13, "isPremium": False }, { "id": "brazil-states-symbols", "name": "Brazil (states) Symbols", "revision": 13, "isPremium": False }, { "id": "canada-provinces-and-territories-symbols", "name": "Canada (provinces and territories) Symbols", "revision": 13, "isPremium": False }, { "id": "central-america-countries-symbols", "name": "Central America (countries) Symbols", "revision": 13, "isPremium": False }, { "id": "chile-regions-symbols", "name": "Chile (regions) Symbols", "revision": 13, "isPremium": False }, { "id": "china-provinces-symbols", "name": "China (provinces) Symbols", "revision": 13, "isPremium": False }, { "id": "colombia-departments-symbols", "name": "Colombia (departments) Symbols", "revision": 13, "isPremium": False }, { "id": "circle-force-d3", "name": "Circle Force", "revision": 27, "isPremium": False }, { "id": "czech-republic-regions-symbols", "name": "Czech Republic (regions) Symbols", "revision": 13, "isPremium": False }, { "id": "denmark-provinces-symbols", "name": "Denmark (provinces) Symbols", "revision": 13, "isPremium": False }, { "id": "europe-countries-symbols", "name": "Europe (countries) Symbols", "revision": 14, "isPremium": False }, { "id": "finland-regions-symbols", "name": "Finland (regions) Symbols", "revision": 13, "isPremium": False }, { "id": "france-departments-symbols", "name": "France (departments) Symbols", "revision": 13, "isPremium": False }, { "id": "germany-states-symbols", "name": "Germany (states) Symbols", "revision": 13, "isPremium": False }, { "id": "greece-regions-symbols", "name": "Greece (regions) Symbols", "revision": 13, "isPremium": False }, { "id": "hungary-regions-symbols", "name": "Hungary (regions) Symbols", "revision": 13, "isPremium": False }, { "id": "india-states-symbols", "name": "India (states) Symbols", "revision": 13, "isPremium": False }, { "id": "indonesia-provinces-symbols", "name": "Indonesia (provinces) Symbols", "revision": 13, "isPremium": False }, { "id": "iran-provinces-symbols", "name": "Iran (provinces) Symbols", "revision": 16, "isPremium": False }, { "id": "ireland-counties-symbols", "name": "Ireland (counties) Symbols", "revision": 13, "isPremium": False }, { "id": "israel-districts-symbols", "name": "Israel (districts) Symbols", "revision": 13, "isPremium": False }, { "id": "italy-provinces-symbols", "name": "Italy (provinces) Symbols", "revision": 13, "isPremium": False }, { "id": "japan-prefectures-symbols", "name": "Japan (prefectures) Symbols", "revision": 13, "isPremium": False }, { "id": "latin-america-countries-symbols", "name": "Latin America (countries) Symbols", "revision": 13, "isPremium": False }, { "id": "malaysia-states-symbols", "name": "Malaysia (states) Symbols", "revision": 14, "isPremium": False }, { "id": "mediterranean-sea-countries-symbols", "name": "Mediterranean Sea (countries) Symbols", "revision": 13, "isPremium": False }, { "id": "mexico-states-symbols", "name": "Mexico (states) Symbols", "revision": 13, "isPremium": False }, { "id": "middle-east-countries-symbols", "name": "Middle East (countries) Symbols", "revision": 13, "isPremium": False }, { "id": "netherlands-provinces-symbols", "name": "Netherlands (provinces) Symbols", "revision": 13, "isPremium": False }, { "id": "nigeria-states-symbols", "name": "Nigeria (states) Symbols", "revision": 13, "isPremium": False }, { "id": "north-america-countries-symbols", "name": "North America (countries) Symbols", "revision": 13, "isPremium": False }, { "id": "norway-counties-symbols", "name": "Norway (counties) Symbols", "revision": 13, "isPremium": False }, { "id": "oceania-countries-symbols", "name": "Oceania (countries) Symbols", "revision": 13, "isPremium": False }, { "id": "pakistan-provinces-symbols", "name": "Pakistan (provinces) Symbols", "revision": 13, "isPremium": False }, { "id": "peru-regions-symbols", "name": "Peru (regions) Symbols", "revision": 13, "isPremium": False }, { "id": "philippines-provinces-symbols", "name": "Philippines (provinces) Symbols", "revision": 12, "isPremium": False }, { "id": "poland-provinces-symbols", "name": "Poland (provinces) Symbols", "revision": 12, "isPremium": False }, { "id": "portugal-subdivisions-symbols", "name": "Portugal (subdivisions) Symbols", "revision": 12, "isPremium": False }, { "id": "qatar-municipalities-symbols", "name": "Qatar (municipalities) Symbols", "revision": 12, "isPremium": False }, { "id": "romania-regions-symbols", "name": "Romania (regions) Symbols", "revision": 12, "isPremium": False }, { "id": "russia-federal-subjects-symbols", "name": "Russia (federal subjects) Symbols", "revision": 12, "isPremium": False }, { "id": "saudi-arabia-provinces-symbols", "name": "Saudi Arabia (provinces) Symbols", "revision": 12, "isPremium": False }, { "id": "singapore-regions-symbols", "name": "Singapore (regions) Symbols", "revision": 12, "isPremium": False }, { "id": "south-africa-provinces-symbols", "name": "South Africa (provinces) Symbols", "revision": 12, "isPremium": False }, { "id": "south-america-countries-symbols", "name": "South America (countries) Symbols", "revision": 12, "isPremium": False }, { "id": "south-east-asia-countries-symbols", "name": "South East Asia (countries) Symbols", "revision": 12, "isPremium": False }, { "id": "south-korea-provinces-symbols", "name": "South Korea (provinces) Symbols", "revision": 12, "isPremium": False }, { "id": "spain-provinces-symbols", "name": "Spain (provinces) Symbols", "revision": 12, "isPremium": False }, { "id": "sweden-counties-symbols", "name": "Sweden (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "switzerland-cantons-symbols", "name": "Switzerland (cantons) Symbols", "revision": 12, "isPremium": False }, { "id": "taiwan-municipalities-symbols", "name": "Taiwan (municipalities) Symbols", "revision": 12, "isPremium": False }, { "id": "thailand-provinces-symbols", "name": "Thailand (provinces) Symbols", "revision": 12, "isPremium": False }, { "id": "turkey-provinces-symbols", "name": "Turkey (provinces) Symbols", "revision": 12, "isPremium": False }, { "id": "uae-emirates-symbols", "name": "UAE (emirates) Symbols", "revision": 12, "isPremium": False }, { "id": "uk-districts-symbols", "name": "UK (districts) Symbols", "revision": 12, "isPremium": False }, { "id": "ukraine-regions-symbols", "name": "Ukraine (regions) Symbols", "revision": 12, "isPremium": False }, { "id": "west-africa-countries-symbols", "name": "West Africa (countries) Symbols", "revision": 12, "isPremium": False }, { "id": "world-continents-symbols", "name": "World (continents) Symbols", "revision": 13, "isPremium": False }, { "id": "world-countries-symbols", "name": "World (countries) Symbols", "revision": 14, "isPremium": False }, { "id": "usa-counties-symbols", "name": "USA (counties) Symbols", "revision": 14, "isPremium": False }, { "id": "new-york-boroughs-symbols", "name": "New York (boroughs) Symbols", "revision": 12, "isPremium": False }, { "id": "alabama-counties-symbols", "name": "Alabama (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "alaska-boroughs-symbols", "name": "Alaska (boroughs) Symbols", "revision": 12, "isPremium": False }, { "id": "arizona-counties-symbols", "name": "Arizona (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "arkansas-counties-symbols", "name": "Arkansas (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "california-counties-symbols", "name": "California (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "colorado-counties-symbols", "name": "Colorado (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "connecticut-counties-symbols", "name": "Connecticut (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "delaware-counties-symbols", "name": "Delaware (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "florida-counties-symbols", "name": "Florida (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "georgia-counties-symbols", "name": "Georgia (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "hawaii-counties-symbols", "name": "Hawaii (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "idaho-counties-symbols", "name": "Idaho (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "timeline", "name": "Project Management", "revision": 20, "isPremium": False }, { "id": "illinois-counties-symbols", "name": "Illinois (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "indiana-counties-symbols", "name": "Indiana (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "iowa-counties-symbols", "name": "Iowa (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "kansas-counties-symbols", "name": "Kansas (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "kentucky-counties-symbols", "name": "Kentucky (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "louisiana-counties-symbols", "name": "Louisiana (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "maine-counties-symbols", "name": "Maine (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "maryland-counties-symbols", "name": "Maryland (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "massachusetts-counties-symbols", "name": "Massachusetts (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "michigan-counties-symbols", "name": "Michigan (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "minnesota-counties-symbols", "name": "Minnesota (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "mississippi-counties-symbols", "name": "Mississippi (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "missouri-counties-symbols", "name": "Missouri (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "montana-counties-symbols", "name": "Montana (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "nebraska-counties-symbols", "name": "Nebraska (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "nevada-counties-symbols", "name": "Nevada (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "new-hampshire-counties-symbols", "name": "New Hampshire (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "new-jersey-counties-symbols", "name": "New Jersey (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "new-mexico-counties-symbols", "name": "New Mexico (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "new-york-counties-symbols", "name": "New York (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "north-carolina-counties-symbols", "name": "North Carolina (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "north-dakota-counties-symbols", "name": "North Dakota (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "ohio-counties-symbols", "name": "Ohio (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "oklahoma-counties-symbols", "name": "Oklahoma (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "oregon-counties-symbols", "name": "Oregon (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "pennsylvania-counties-symbols", "name": "Pennsylvania (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "rhode-island-counties-symbols", "name": "Rhode Island (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "south-carolina-counties-symbols", "name": "South Carolina (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "south-dakota-counties-symbols", "name": "South Dakota (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "tennessee-counties-symbols", "name": "Tennessee (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "texas-counties-symbols", "name": "Texas (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "utah-counties-symbols", "name": "Utah (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "vermont-counties-symbols", "name": "Vermont (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "virginia-counties-symbols", "name": "Virginia (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "washington-counties-symbols", "name": "Washington (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "west-virginia-counties-symbols", "name": "West Virginia (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "wisconsin-counties-symbols", "name": "Wisconsin (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "wyoming-counties-symbols", "name": "Wyoming (counties) Symbols", "revision": 12, "isPremium": False }, { "id": "galaxy-chart", "name": "Galaxy Chart", "revision": 16, "isPremium": False }, { "id": "africa-countries-circles", "name": "Africa (countries) Bubbles", "revision": 17, "isPremium": False }, { "id": "argentina-provinces-circles", "name": "Argentina (provinces) Bubbles", "revision": 13, "isPremium": False }, { "id": "asia-countries-circles", "name": "Asia (countries) Bubbles", "revision": 13, "isPremium": False }, { "id": "australia-states-circles", "name": "Australia (states) Bubbles", "revision": 13, "isPremium": False }, { "id": "austria-states-circles", "name": "Austria (states) Bubbles", "revision": 13, "isPremium": False }, { "id": "bangladesh-districts-circles", "name": "Bangladesh (districts) Bubbles", "revision": 13, "isPremium": False }, { "id": "belgium-provinces-circles", "name": "Belgium (provinces) Bubbles", "revision": 13, "isPremium": False }, { "id": "brazil-states-circles", "name": "Brazil (states) Bubbles", "revision": 13, "isPremium": False }, { "id": "canada-provinces-and-territories-circles", "name": "Canada (provinces and territories) Bubbles", "revision": 12, "isPremium": False }, { "id": "central-america-countries-circles", "name": "Central America (countries) Bubbles", "revision": 13, "isPremium": False }, { "id": "chile-regions-circles", "name": "Chile (regions) Bubbles", "revision": 13, "isPremium": False }, { "id": "china-provinces-circles", "name": "China (provinces) Bubbles", "revision": 13, "isPremium": False }, { "id": "colombia-departments-circles", "name": "Colombia (departments) Bubbles", "revision": 13, "isPremium": False }, { "id": "czech-republic-regions-circles", "name": "Czech Republic (regions) Bubbles", "revision": 13, "isPremium": False }, { "id": "denmark-provinces-circles", "name": "Denmark (provinces) Bubbles", "revision": 13, "isPremium": False }, { "id": "europe-countries-circles", "name": "Europe (countries) Bubbles", "revision": 14, "isPremium": False }, { "id": "finland-regions-circles", "name": "Finland (regions) Bubbles", "revision": 13, "isPremium": False }, { "id": "france-departments-circles", "name": "France (departments) Bubbles", "revision": 13, "isPremium": False }, { "id": "germany-states-circles", "name": "Germany (states) Bubbles", "revision": 13, "isPremium": False }, { "id": "greece-regions-circles", "name": "Greece (regions) Bubbles", "revision": 13, "isPremium": False }, { "id": "hungary-regions-circles", "name": "Hungary (regions) Bubbles", "revision": 13, "isPremium": False }, { "id": "india-states-bubbles", "name": "India (states) Bubbles", "revision": 13, "isPremium": False }, { "id": "indonesia-provinces-bubbles", "name": "Indonesia (provinces) Bubbles", "revision": 12, "isPremium": False }, { "id": "iran-provinces-bubbles", "name": "Iran (provinces) Bubbles", "revision": 15, "isPremium": False }, { "id": "ireland-counties-bubbles", "name": "Ireland (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "israel-districts-bubbles", "name": "Israel (districts) Bubbles", "revision": 12, "isPremium": False }, { "id": "italy-provinces-bubbles", "name": "Italy (provinces) Bubbles", "revision": 12, "isPremium": False }, { "id": "japan-prefectures-bubbles", "name": "Japan (prefectures) Bubbles", "revision": 12, "isPremium": False }, { "id": "latin-america-countries-bubbles", "name": "Latin America (countries) Bubbles", "revision": 12, "isPremium": False }, { "id": "malaysia-states-bubbles", "name": "Malaysia (states) Bubbles", "revision": 12, "isPremium": False }, { "id": "mediterranean-sea-countries-bubbles", "name": "Mediterranean Sea (countries) Bubbles", "revision": 12, "isPremium": False }, { "id": "mexico-states-bubbles", "name": "Mexico (states) Bubbles", "revision": 12, "isPremium": False }, { "id": "middle-east-countries-bubbles", "name": "Middle East (countries) Bubbles", "revision": 12, "isPremium": False }, { "id": "netherlands-provinces-bubbles", "name": "Netherlands (provinces) Bubbles", "revision": 12, "isPremium": False }, { "id": "nigeria-states-bubbles", "name": "Nigeria (states) Bubbles", "revision": 12, "isPremium": False }, { "id": "north-america-countries-bubbles", "name": "North America (countries) Bubbles", "revision": 12, "isPremium": False }, { "id": "norway-counties-bubbles", "name": "Norway (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "oceania-countries-bubbles", "name": "Oceania (countries) Bubbles", "revision": 12, "isPremium": False }, { "id": "pakistan-provinces-bubbles", "name": "Pakistan (provinces) Bubbles", "revision": 12, "isPremium": False }, { "id": "peru-regions-bubbles", "name": "Peru (regions) Bubbles", "revision": 12, "isPremium": False }, { "id": "philippines-provinces-bubbles", "name": "Philippines (provinces) Bubbles", "revision": 12, "isPremium": False }, { "id": "poland-provinces-bubbles", "name": "Poland (provinces) Bubbles", "revision": 12, "isPremium": False }, { "id": "portugal-subdivisions-bubbles", "name": "Portugal (subdivisions) Bubbles", "revision": 12, "isPremium": False }, { "id": "qatar-municipalities-bubbles", "name": "Qatar (municipalities) Bubbles", "revision": 12, "isPremium": False }, { "id": "romania-regions-bubbles", "name": "Romania (regions) Bubbles", "revision": 12, "isPremium": False }, { "id": "russia-federal-subjects-bubbles", "name": "Russia (federal subjects) Bubbles", "revision": 12, "isPremium": False }, { "id": "saudi-arabia-provinces-bubbles", "name": "Saudi Arabia (provinces) Bubbles", "revision": 12, "isPremium": False }, { "id": "singapore-regions-bubbles", "name": "Singapore (regions) Bubbles", "revision": 12, "isPremium": False }, { "id": "south-africa-provinces-bubbles", "name": "South Africa (provinces) Bubbles", "revision": 12, "isPremium": False }, { "id": "south-america-countries-bubbles", "name": "South America (countries) Bubbles", "revision": 12, "isPremium": False }, { "id": "south-east-asia-countries-bubbles", "name": "South East Asia (countries) Bubbles", "revision": 12, "isPremium": False }, { "id": "south-korea-provinces-bubbles", "name": "South Korea (provinces) Bubbles", "revision": 12, "isPremium": False }, { "id": "spain-provinces-bubbles", "name": "Spain (provinces) Bubbles", "revision": 12, "isPremium": False }, { "id": "sweden-counties-bubbles", "name": "Sweden (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "switzerland-cantons-bubbles", "name": "Switzerland (cantons) Bubbles", "revision": 12, "isPremium": False }, { "id": "taiwan-municipalities-bubbles", "name": "Taiwan (municipalities) Bubbles", "revision": 12, "isPremium": False }, { "id": "thailand-provinces-bubbles", "name": "Thailand (provinces) Bubbles", "revision": 12, "isPremium": False }, { "id": "turkey-provinces-bubbles", "name": "Turkey (provinces) Bubbles", "revision": 12, "isPremium": False }, { "id": "uae-emirates-bubbles", "name": "UAE (emirates) Bubbles", "revision": 13, "isPremium": False }, { "id": "uk-districts-bubbles", "name": "UK (districts) Bubbles", "revision": 12, "isPremium": False }, { "id": "ukraine-regions-bubbles", "name": "Ukraine (regions) Bubbles", "revision": 12, "isPremium": False }, { "id": "west-africa-countries-bubbles", "name": "West Africa (countries) Bubbles", "revision": 12, "isPremium": False }, { "id": "world-continents-bubbles", "name": "World (continents) Bubbles", "revision": 13, "isPremium": False }, { "id": "usa-states-bubbles", "name": "USA (states) Bubbles", "revision": 15, "isPremium": False }, { "id": "usa-counties-bubbles", "name": "USA (counties) Bubbles", "revision": 17, "isPremium": False }, { "id": "new-york-boroughs-bubbles", "name": "New York (boroughs) Bubbles", "revision": 12, "isPremium": False }, { "id": "alabama-counties-bubbles", "name": "Alabama (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "alaska-boroughs-bubbles", "name": "Alaska (boroughs) Bubbles", "revision": 12, "isPremium": False }, { "id": "arizona-counties-bubbles", "name": "Arizona (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "arkansas-counties-bubbles", "name": "Arkansas (counties) Bubbles", "revision": 11, "isPremium": False }, { "id": "california-counties-bubbles", "name": "California (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "colorado-counties-bubbles", "name": "Colorado (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "connecticut-counties-bubbles", "name": "Connecticut (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "delaware-counties-bubbles", "name": "Delaware (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "florida-counties-bubbles", "name": "Florida (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "georgia-counties-bubbles", "name": "Georgia (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "hawaii-counties-bubbles", "name": "Hawaii (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "idaho-counties-bubbles", "name": "Idaho (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "illinois-counties-bubbles", "name": "Illinois (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "indiana-counties-bubbles", "name": "Indiana (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "iowa-counties-bubbles", "name": "Iowa (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "kansas-counties-bubbles", "name": "Kansas (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "kentucky-counties-bubbles", "name": "Kentucky (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "louisiana-counties-bubbles", "name": "Louisiana (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "maine-counties-bubbles", "name": "Maine (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "maryland-counties-bubbles", "name": "Maryland (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "massachusetts-counties-bubbles", "name": "Massachusetts (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "michigan-counties-bubbles", "name": "Michigan (counties) Bubbles", "revision": 11, "isPremium": False }, { "id": "minnesota-counties-bubbles", "name": "Minnesota (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "mississippi-counties-bubbles", "name": "Mississippi (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "missouri-counties-bubbles", "name": "Missouri (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "montana-counties-bubbles", "name": "Montana (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "nebraska-counties-bubbles", "name": "Nebraska (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "nevada-counties-bubbles", "name": "Nevada (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "new-hampshire-counties-bubbles", "name": "New Hampshire (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "new-jersey-counties-bubbles", "name": "New Jersey (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "new-mexico-counties-bubbles", "name": "New Mexico (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "new-york-counties-bubbles", "name": "New York (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "north-carolina-counties-bubbles", "name": "North Carolina (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "north-dakota-counties-bubbles", "name": "North Dakota (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "ohio-counties-bubbles", "name": "Ohio (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "oklahoma-counties-bubbles", "name": "Oklahoma (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "oregon-counties-bubbles", "name": "Oregon (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "pennsylvania-counties-bubbles", "name": "Pennsylvania (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "rhode-island-counties-bubbles", "name": "Rhode Island (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "south-carolina-counties-bubbles", "name": "South Carolina (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "south-dakota-counties-bubbles", "name": "South Dakota (counties) Bubbles", "revision": 11, "isPremium": False }, { "id": "tennessee-counties-bubbles", "name": "Tennessee (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "texas-counties-bubbles", "name": "Texas (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "utah-counties-bubbles", "name": "Utah (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "vermont-counties-bubbles", "name": "Vermont (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "virginia-counties-bubbles", "name": "Virginia (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "washington-counties-bubbles", "name": "Washington (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "west-virginia-counties-bubbles", "name": "West Virginia (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "wisconsin-counties-bubbles", "name": "Wisconsin (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "wyoming-counties-bubbles", "name": "Wyoming (counties) Bubbles", "revision": 12, "isPremium": False }, { "id": "andalusia-provinces-symbols", "name": "Andalusia (provinces) Symbols", "revision": 12, "isPremium": False }, { "id": "andalusia-provinces-bubbles", "name": "Andalusia (provinces) Bubbles", "revision": 11, "isPremium": False }, { "id": "balloon-chart", "name": "Balloon Chart", "revision": 14, "isPremium": False }, { "id": "timelinee", "name": "Timeline", "revision": 60, "isPremium": False }, { "id": "stacked-polar", "name": "Stacked Polar prop", "revision": 12, "isPremium": False }, { "id": "racing-pie", "name": "Racing Pie", "revision": 25, "isPremium": False }, { "id": "pictogram", "name": "Pictogram Vertical", "revision": 28, "isPremium": False }, { "id": "marimekko", "name": "Marimekko", "revision": 13, "isPremium": False }, { "id": "pictogram-horizontal", "name": "Pictogram Horizontal", "revision": 13, "isPremium": False }, { "id": "stream-graph", "name": "Stream Graph", "revision": 10, "isPremium": False }, { "id": "bar-chart-change-indicator", "name": "Bar chart (change indicator)", "revision": 7, "isPremium": False } ]



def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def ListingYourCharts() :
    url = "https://api.plotset.com/v1/charts"


    payload={}
    headers = {
    'Accept': 'application/json',
    'Authorization': apiKey
    }


    response = requests.request("GET", url, headers=headers, data=payload)


    result = json.loads(response.text)
    print(result)

    with open(f"result.json", "w" , encoding="utf-8") as f:
         json.dump(result , f , indent=4 , ensure_ascii=False)

def creatingChart(templateId,title="") :
    url = "https://api.plotset.com/v1/chart"
    payload = json.dumps({
    "title": f"{title}",
    "templateId": f"{templateId}"
    })
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': apiKey
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    dic = json.loads(response.text)
    return dic["id"]
    # print(response.text)

def gettingTheChartsDetails(id):
    url = f"https://api.plotset.com/v1/chart/{id}"
    payload={}
    headers = {
    'Accept': 'application/json',
    'Authorization': apiKey
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    d = json.loads(response.text)
    # with open(f"config\{d['title']}.json", "w" , encoding="utf-8") as f:
    #      json.dump(d , f , indent=4 , ensure_ascii=False)
    return d["chartConfig"]
    # f = open("test/chart.json" , "w") 
    # f.write(response.text)
    # f.close()
    # print(response.text)

def gettingData(id,folderName) :
    url = f"https://api.plotset.com/v1/chart/{id}/data"
    payload={}
    headers = {
    'Accept': 'application/json',
    'Authorization': 'xd1bVlrOnIz9kEjO_9J07NINIPyhxWWGdftkKJqm-aRtraQT'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.text
    for i in data :
        f=open (fr"data\{folderName}.csv" , "a" , encoding="utf-8")
        f.write(i)
        f.close()

def updatingData(id) :
    url = f"https://api.plotset.com/v1/chart/{id}/data"
    payload={}
    mp_encoder = MultipartEncoder(fields={'file':('result.csv',open(f'flourish data.csv','rb'),'text/csv'),})
    headers = {
    'Content-Type': mp_encoder.content_type,
    # 'Accept': 'application/json',
    'Authorization': apiKey
    }
    response = requests.put(url, headers=headers, data=mp_encoder)
    print(response.text)

def updatingConfigs(id,config) :
    url = f"https://api.plotset.com/v1/chart/{id}/config"
   
    payload = json.dumps(config)
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': apiKey
    }
    response = requests.request("PUT", url, headers=headers, data=payload)
    print(response.text)

def GettingtheDataBinding(id) :
    url = f"https://api.plotset.com/v1/chart/{id}/binding"
   
   
    payload = {}
    headers = {
    'Accept': 'application/json',
    'Authorization': apiKey
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    result = json.loads(response.text)
    return result

def UpdatingtheDataBinding(id,newB) :
    url = f"https://api.plotset.com/v1/chart/{id}/binding"
   
    binding = GettingtheDataBinding(id)
    for a in newB :
        for i in range(len(binding)) :
            if a == binding[i]["field"] :
                binding[i]["default"] = newB[a]
                break
        
    b = {"bindings" : binding}
    payload = json.dumps(b)
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': apiKey
    }
    response = requests.request("PUT", url, headers=headers, data=payload)
    print(response.text)

def creatingEmbed(id) :
    url = f"https://api.plotset.com/v1/chart/{id}/embed"
    payload={}
    headers = {
    'Accept': 'application/json',
    'Authorization': apiKey
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    # print(response.text)
    r = json.loads(response.text)
    # print(f'\nhere is the share link :\n\n{r["share"]}\n')
    return r["share"]
    # return r["share"]

def get_embed(new_chart_id):
    
    url = "https://api.plotset.com/v1/chart/{}/embed".format(new_chart_id)


    payload={}
    headers = {
      'Accept': 'application/json',
      'Authorization': apiKey
    }


    response = requests.request("POST", url, headers=headers, data=payload)
    
    share_link = eval(response.text)['share']


    return share_link

def UpdatingTheEmbed(id) :
    url = f"https://api.plotset.com/v1/chart/{id}/embed"
    payload={}
    headers = {
    'Accept': 'application/json',
    'Authorization': apiKey
    }
    response = requests.request("PUT", url, headers=headers, data=payload)
    r = json.loads(response.text)
    print(f'\nhere is the updated share link :\n\n{r["share"]}\n')
    # print(response.text)

def flourishConfigGetter(url) :
    page_sourceF = ""
    if "<!DOCTYPE html>" not in url :
        responseF = requests.get(url)
        if responseF.status_code == 200:
            page_sourceF = responseF.text
    else :
        page_sourceF = url
    if page_sourceF != "" :
        soupF = BeautifulSoup(page_sourceF, 'html.parser')
        scriptsF = soupF.find_all("script")
        for t in scriptsF :
            scriptF = t.text
            if "var _Flourish_settings = " in scriptF :
                break
        temp = ""
        flourishConfig = ""
        for i in scriptF :
            temp += i 
            if "var _Flourish_settings = " in temp :
                if ";\n\t\t" in flourishConfig :
                    break
                flourishConfig += i
        flourishConfig = flourishConfig.replace(";\n\t\t","")
        flourishConfig = flourishConfig.replace("\n","\\n")
        
        
        try :
            flourishConfig = json.loads(flourishConfig)
        except :
            return False
        return flourishConfig

def flourishDataGetter(url) :
    flourishCon = flourishConfigGetter(url)
    if flourishCon == False :
        print("no chart id")
        return False        
    elif "chart_type" in flourishCon :
        chartType = flourishCon["chart_type"]
    else :
        print("no chart id")
        return False
    try :
        sortmode = flourishCon["sort_mode"]
    except :
        sortmode = None
    page_sourceF = ""
    if "<!DOCTYPE html>" not in url :
        responseF = requests.get(url)
        if responseF.status_code == 200:
            page_sourceF = responseF.text
    else :
        page_sourceF = url
    if page_sourceF != "" :
        soupF = BeautifulSoup(page_sourceF, 'html.parser')
        scriptsF = soupF.find_all("script")
        for t in scriptsF :
            scriptF = t.text
            if "var _Flourish_data_column_names = " in scriptF :
                break
        temp = ""
        flourishBinding = ""
        for i in scriptF :
            temp += i 
            if "_Flourish_data_column_names = " in temp :
                if ",\n\t\t" in flourishBinding :
                    break
                flourishBinding += i
        flourishBinding = flourishBinding.replace(",\n\t\t","")
        try :
            flourishBinding = json.loads(flourishBinding)
        except :
            return False
        plotsetBinding = {"labels" : "" , "values" : ""}
        
        temp = flourishBinding["data"]
        dec = 65
        for fK , fV in temp.items() :
            if fK == "label" :
                plotsetBinding["labels"] = chr(dec)
                dec += 1
            elif fK == "value" :
                if isinstance(fV,list) :
                    if len(fV) > 1 :
                        plotsetBinding["values"] = chr(dec)
                        for d in fV :
                            dec += 1
                        dec -= 1
                        plotsetBinding["values"] += f"-{chr(dec)}"
                    else :
                        plotsetBinding["values"] = chr(dec)
                        dec += 1
                else :
                    plotsetBinding["values"] = chr(dec)
                    dec += 1
                        
        

        temp = flourishBinding["data"]
        tempD = ""
        
        for jK , jV in temp.items() :
            if isinstance(jV,list) :
                for d in jV :
                    tempD += f"{d},"
            else :
                    tempD += f"{jV},"
        if tempD != "" :
            tempD += "\n"

        temp = ""
        flourishData = ""
        for i in scriptF :
            temp += i 
            if "_Flourish_data = " in temp :
                if ",\n\t\t" in flourishData :
                    break
                flourishData += i
        flourishData = flourishData.replace(",\n\t\t","")
        try :
            flourishData = json.loads(flourishData)
        except :
            return False
        temp = flourishData["data"]
        if sortmode == "value" or sortmode == "label" :
            for s in range(len(temp)) :
                for l in range(len(temp)-s-1) :
                    if sortmode == "value" :
                        if "bar" in chartType :
                            if isinstance(temp[l]["value"],list) and isinstance(temp[l+1]["value"],list) :
                                sumL = 0
                                for n in temp[l]["value"] :
                                    sumL += float(n.replace(',', '.'))
                                sumL1 = 0
                                for o in temp[l+1]["value"] :
                                    sumL1 += float(o.replace(',', '.'))
                                if sumL < sumL1 :
                                    temp[l] , temp[l+1] = temp[l+1] ,temp[l]
                            elif temp[l]["value"] < temp[l+1]["value"] :
                                temp[l] , temp[l+1] = temp[l+1] ,temp[l]
                        elif "column" in chartType :
                            if isinstance(temp[l]["value"],list) and isinstance(temp[l+1]["value"],list) :
                                sumL = 0
                                for n in temp[l]["value"] :
                                    sumL += float(n.replace(',', '.'))
                                sumL1 = 0
                                for o in temp[l+1]["value"] :
                                    sumL1 += float(o.replace(',', '.'))
                                if sumL > sumL1 :
                                    temp[l] , temp[l+1] = temp[l+1] ,temp[l]
                            elif temp[l]["value"] > temp[l+1]["value"] :
                                temp[l] , temp[l+1] = temp[l+1] ,temp[l]
                    elif sortmode == "label" :
                        if "bar" in chartType :
                            m = 0
                            while m < len(temp[l]["label"]) and m < len(temp[l+1]["label"]) :
                                if ord(temp[l]["label"][m]) < ord(temp[l+1]["label"][m]) :
                                    temp[l] , temp[l+1] = temp[l+1] ,temp[l]
                                    break
                                elif ord(temp[l]["label"][m]) > ord(temp[l+1]["label"][m]) :
                                    break
                                elif ord(temp[l]["label"][m]) == ord(temp[l+1]["label"][m]) :
                                    m += 1
                        elif "column" in chartType :
                            m = 0
                            while m < len(temp[l]["label"]) and m < len(temp[l+1]["label"]) :
                                if ord(temp[l]["label"][m]) > ord(temp[l+1]["label"][m]) :
                                    temp[l] , temp[l+1] = temp[l+1] ,temp[l]
                                    break
                                elif ord(temp[l]["label"][m]) < ord(temp[l+1]["label"][m]) :
                                    break
                                elif ord(temp[l]["label"][m]) == ord(temp[l+1]["label"][m]) :
                                    m += 1


        for t in temp :
            for jK , jV in t.items() :
                if isinstance(jV,list) :
                    for d in jV :
                        tempD += f'''"{str(d)}",'''
                else :
                        tempD += f'''"{str(jV)}",'''
            if tempD != "" :
                tempD += "\n"
        tempD = tempD.replace(",\n","\n")
        f = open("flourish data.csv" , "w" , encoding="utf-8")
        f.write(tempD)
        f.close()


        return plotsetBinding

def templateIdMatcher(flourishUrl,plotsetBinding) :
    flourishConfig = flourishConfigGetter(flourishUrl)
    if len(plotsetBinding['values']) == 1 :
        flourishConfig["chart_type"] = flourishConfig["chart_type"].replace("grouped","").replace("stacked","")

    if flourishConfig == False :
        print("no chart id")
        return False        
    elif "chart_type" in flourishConfig :
        print(flourishConfig["chart_type"])
    else :
        print("no chart id")
        return False

    parts = []
    temp = ""
    flourishConfig["chart_type"] += "_"
    flourishConfig["chart_type"] = flourishConfig["chart_type"].replace("__","_")
    for f in flourishConfig["chart_type"] :
        if f != "_" :
            temp += f 
        else :
            parts.append(temp)
            temp = ""


    matches = {}
    for i in range(len(plotsetChartIds)) :
        ii = plotsetChartIds[i]["name"].lower().replace("chart","")
        status = True
        for p in parts :
            if p not in ii:
                status = False
                break
        if status == True :
            matches[ii] = i

    result = {}
    for m in matches :
        temp = m.replace(" ","")
        for p in parts :
            temp = temp.replace(p,"")
        result[matches[m]] = len(temp)


    result = dict(sorted(result.items(),key = lambda item:item[1]))

    if len(result) == 0 :
        print("no templates for this chart")
        exit()
    else :
        fk,fv = next(iter(result.items()))
        if plotsetChartIds[fk]["id"] != None :
            ID = creatingChart(plotsetChartIds[fk]["id"])
            return ID

def configMatcher(id,flourishUrl,plotsetBinding) :
    flourishCon = flourishConfigGetter(flourishUrl)
    plotsetCon = gettingTheChartsDetails(id)
    with open(f"all config.json" , "r" , encoding="utf-8") as f :
        allConfig = json.load(f)
    if len(plotsetBinding['values']) == 1 :
        flourishCon["chart_type"] = flourishCon["chart_type"].replace("grouped","").replace("stacked","")

    if "color.categorical_palette" not in flourishCon :
        if "grouped" not in flourishCon["chart_type"] and "stacked" not in flourishCon["chart_type"]:
            plotsetCon["palette.type"] = "mono"
            plotsetCon["palette.selected_key_mono"] = "custom"
            plotsetCon["palette.colors"] = ["#4328e7"]
            plotsetCon["palette.color__mono_0"] = "#4328e7"
        else :
            plotsetCon["palette.type"] = "multi"
            plotsetCon["palette.selected_key_multi"] = "custom"
            plotsetCon["palette.colors"] = ["#4328e7","#9654e5","#ff6283","#ff8800","#ffc502","#007d8e","#1aa7ee","#29dae4","#88e99a","#019c00","#c11f1f","#730000"]
            plotsetCon["palette.color__multi_0"] = "#4328e7"
            plotsetCon["palette.color__multi_1"] = "#9654e5"
            plotsetCon["palette.color__multi_2"] = "#ff6283"
            plotsetCon["palette.color__multi_3"] = "#ff8800"
            plotsetCon["palette.color__multi_4"] = "#ffc502"
            plotsetCon["palette.color__multi_5"] = "#007d8e"
            plotsetCon["palette.color__multi_6"] = "#1aa7ee"
            plotsetCon["palette.color__multi_7"] = "#29dae4"
            plotsetCon["palette.color__multi_8"] = "#88e99a"
            plotsetCon["palette.color__multi_9"] = "#019c00"
            plotsetCon["palette.color__multi_10"] = "#c11f1f"
            plotsetCon["palette.color__multi_11"] = "#730000"

    for conK , conV in flourishCon.items() :
        for i in range(len(allConfig)) :
            flourishField = allConfig[i]["field"].values()
            flourishField = list(flourishField)
            flourishField = flourishField[0]
        
            if conK == flourishField :
               
            
                plotsetField = allConfig[i]["field"].keys()
                plotsetField = list(plotsetField)
                plotsetField = plotsetField[0]
                
                flourishVal = allConfig[i]["value"].values()
                flourishVal = list(flourishVal)
                flourishVal = flourishVal[0]

                plotsetVal = allConfig[i]["value"].keys()
                plotsetVal = list(plotsetVal)
                plotsetVal = plotsetVal[0]
                
                if conK == "color.categorical_palette" :
                    
                    try :
                        if flourishCon["color_mode"] == "column" and "grouped" not in flourishCon["chart_type"] and "stacked" not in flourishCon["chart_type"]:
                                plotsetCon["palette.type"] = "mono"
                                plotsetCon["palette.selected_key_mono"] = "custom"
                                plotsetCon[plotsetField] = [conV[0]]
                                plotsetCon["palette.color__mono_0"] = conV[0]
                        else :
                            plotsetCon["palette.type"] = "multi"
                            plotsetCon["palette.selected_key_multi"] = "custom"
                            
                            
                            plotsetCon[plotsetField] = conV
                            for cunt in range(len(conV)) :
                                plotsetCon[f"palette.color__multi_{cunt}"] = conV[cunt]
                          
                            
                    except Exception as error:
                        print(error)
                        plotsetCon["palette.type"] = "mono"
                        plotsetCon["palette.selected_key_mono"] = "custom"
                        
                        plotsetCon[plotsetField] = [conV[0]]
                        plotsetCon["palette.color__mono_0"] = conV[0]
                       
                        # plotsetCon[plotsetField] = conV
                        # for cunt in range(len(conV)) :
                        #     plotsetCon[f"palette.color__multi_{cunt}"] = conV[cunt]
                        
                elif flourishVal == plotsetVal == "" :
                    plotsetCon[plotsetField] = conV
                    break

                elif flourishVal == plotsetVal.replace("-","") :
                    if flourishVal == conV :
                        plotsetCon[plotsetField] = plotsetVal
                        break

                elif is_number(flourishVal) == True and is_number(plotsetVal) == True and is_number(conV) == True : 
                    flourishVal = float(flourishVal)
                    plotsetVal = float(plotsetVal)
                    conV = float(conV)
                    temp = plotsetVal*conV/flourishVal
                    plotsetCon[plotsetField] = temp
                elif flourishVal == conV :
                    plotsetCon[plotsetField] = plotsetVal
                    break

    updatingConfigs(id,plotsetCon)

def csvWriter(csv) :
    result = ""
    for i in csv :
        t = i.keys()
        t = list(t)
        t = t[0]
        result += t 
        result += ","
        t = i.values()
        t = list(t)
        t = t[0]
        result += t 
        result += "\n"
    f = open("share links.csv" , "w" , encoding="utf-8")
    f.write(result)
    f.close()

def tester(flourishUrl) :
    if "https://public.flourish.studio/visualisation" in flourishUrl :
        flourishUrl += "embed"
  
    binding = flourishDataGetter(flourishUrl)
    if binding == False :
        return False
    ID = templateIdMatcher(flourishUrl,binding)
    if ID == False :
        return False
    configMatcher(ID,flourishUrl,binding)
    updatingData(ID)
    UpdatingtheDataBinding(ID,binding)
    plotsetShare = creatingEmbed(ID)
    return plotsetShare







result = []

if test == False :
    counter = 0
    for filename in os.listdir(directory):
        counter += 1 
        for z in range(20) :
            print(counter)
        old_path = os.path.join(directory, filename)
        with open(old_path,"r",encoding="utf-8") as f :
            item = f.read()
        translated_text = bytes(item, 'utf-8').decode('unicode_escape')
        links = tester(translated_text)
        # links = tester(item)
        if links == False :
            continue
        result.append({f'''https://public.flourish.studio/visualisation/{filename.replace(".html","")}''':links})

    with open("share links.json","w",encoding="utf-8") as f :
        json.dump(result,f,indent=4,ensure_ascii=False)
    csvWriter(result)
    

else :
    filename = f"{sample}.html"
        

    old_path = os.path.join(directory, filename)
    with open(old_path,"r",encoding="utf-8") as f :
        item = f.read()
    translated_text = bytes(item, 'utf-8').decode('unicode_escape')
    links = tester(translated_text)
    # links = tester(item)
    if links == False :
        exit()

    result.append({f'''https://public.flourish.studio/visualisation/{filename.replace(".html","")}''':links})
    with open("share links.json","w",encoding="utf-8") as f :
        json.dump(result,f,indent=4,ensure_ascii=False)
    csvWriter(result)



# links = tester("https://public.flourish.studio/visualisation/15758410/")