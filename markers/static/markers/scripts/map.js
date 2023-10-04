/* markers/static/markers/scripts/map.js */

var copy  = "&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors";
var url   = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
var layer = L.tileLayer(url, { attribution: copy });
var map   = L.map("mapid", { layers: [layer] });

/* set map */
map.locate()
  .on("locationfound", (e) => map.setView(e.latlng, 14))
  .on("locationerror", () => map.setView([52.5, 4.95], 12));
  
/* load markers */
async function load_markers() {
  const markers_url = `/api/markers/?in_bbox=${map
    .getBounds()
    .toBBoxString()}`;
  const response = await fetch(markers_url);
  const geojson = await response.json();
  return geojson;
}
/* render markers */
async function render_markers() {
  const markers = await load_markers();
  L.geoJSON(markers)
    .bindPopup((layer) => layer.feature.properties.name)
    .addTo(map);
}

map.on("moveend", render_markers);

/* load areas */
async function load_areas() {
  const areas_url = `/api/areas/?in_bbox=${map
    .getBounds()
    .toBBoxString()}`;
  const response_a = await fetch(areas_url);
  const geojson_a = await response_a.json();
  return geojson_a;
}
/* render areas */
async function render_areas() {
  const areas = await load_areas();
  L.geoJSON(areas)
    .bindPopup((layer) => layer.feature.properties.name)
    .addTo(map);
}

map.on("moveend", render_areas);

/* load multiareas */
async function load_multiareas() {
  const multiareas_url = `/api/multiareas/?in_bbox=${map
    .getBounds()
    .toBBoxString()}`;
  const response_ma = await fetch(multiareas_url);
  const geojson_ma = await response_ma.json();
  return geojson_ma;
}
/* render multiareas */
async function render_multiareas() {
  const multiareas = await load_multiareas();
  L.geoJSON(multiareas)
    .bindPopup((layer) => layer.feature.properties.name)
    .addTo(map);
}

map.on("moveend", render_multiareas);

/* load multilines */
async function load_multilines() {
  const multilines_url = `/api/multilines/?in_bbox=${map
    .getBounds()
    .toBBoxString()}`;
  const response_m = await fetch(multilines_url);
  const geojson_m = await response_m.json();
  return geojson_m;
}
/* render multilines */
async function render_multilines() {
  const multilines = await load_multilines();
  L.geoJSON(multilines)
    .bindPopup((layer) => layer.feature.properties.name)
    .addTo(map);
}

map.on("moveend", render_multilines);