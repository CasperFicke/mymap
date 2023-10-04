/* markers/static/markers/scripts/show_marker.js */

var copy  = "&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors";
var url   = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
var layer = L.tileLayer(url, { attribution: copy });
var map   = L.map("mapid", { layers: [layer] });

/* set map */
map.locate()
  .on("locationfound", (e) => map.setView(e.latlng, 14))
  .on("locationerror", () => map.setView([52.5, 4.95], 12));

/* load marker */
async function load_marker() {
  const markers_url = `/api/markers/?in_bbox=${map
    .getBounds()
    .toBBoxString()}`;
  const response = await fetch(markers_url);
  const geojson = await response.json();
  return geojson;
}
/* render marker */
async function render_marker() {
  const marker = await load_marker();
  L.geoJSON(marker)
    .bindPopup((layer) => layer.feature.properties.name)
    .addTo(map);
}

map.on("moveend", render_marker);
