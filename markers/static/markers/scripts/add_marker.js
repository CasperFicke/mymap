/* markers/static/markers/scripts/add_marker.js */

// set footer for contributors in leaflet map
const copy       = "&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors";
// set url for background leaflet map
const tiles_url  = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
// add contribution footer to map
const base_layer = L.tileLayer(tiles_url, { attribution: copy });
// define map
const map        = L.map("mapid", { layers: [base_layer] });

// set map center and zoom
map.locate()
  // centerlocation from ip
  .on("locationfound", (e) => map.setView(e.latlng, 14))
  // default centerlocation
  .on("locationerror", () => map.setView([52.5, 4.95], 12));

// function to place new marker on the map
async function place_marker(event){
  var location = {
    lat: event.latlng.lat,
    lng: event.latlng.lng
  }
  var new_marker = new L.marker(location, {title:"nieuwe garage",draggable:true}).addTo(map)
  // load lat en lon in dom elements
  document.getElementById('lat').textContent = new_marker._latlng.lat;
  document.getElementById('lng').textContent = new_marker._latlng.lng;
  fetch(`/markers/markers/savemarker?${new_marker}`)
}
// add marker to the map
map.on('dblclick', place_marker)
