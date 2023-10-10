/* markers/static/markers/scripts/add_marker.js */

/* set footer for contributors in leaflet map */
const copy       = "&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors";
/* set url for background leaflet map */
const tiles_url  = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
/* add contribution footer to map */
const base_layer = L.tileLayer(tiles_url, { attribution: copy });
/* define map */
const map        = L.map("mapid", { layers: [base_layer] });

/* set map center and zoom */
map.locate()
  /* centerlocation from ip */
  .on("locationfound", (e) => map.setView(e.latlng, 14))
  /* default centerlocation */
  .on("locationerror", () => map.setView([52.5, 4.95], 12));

/* function to load marker */
async function load_marker() {
  /* get current marker */
  
  /* set drf url for markers */
  const marker_url = `/api/markers/v1/1/`;
  /* bevraag de url */
  const response   = await fetch(marker_url);
  /* retrieve json */
  const geojson    = await response.json();
  /* extract lat en lon from geojson */
  const latitude = geojson.geometry.coordinates[0];
  const longitude = geojson.geometry.coordinates[1];
  /* load lat en lon in dom elements  */
  document.getElementById('lat').textContent = latitude;
  document.getElementById('lon').textContent = longitude;
  /* return json */
  return geojson;
}
/* function to render marker; add marker tot the leaflet map */
async function render_marker() {
  /* call load_marker function */
  const marker = await load_marker();
  
  /* add layer with geojson to the map */
  L.geoJSON(marker)
    /* add popup for markers */
    .bindPopup((layer) => layer.feature.properties.name)
    /* add to the map */
    .addTo(map);
}
/* add marker to map */
map.on("moveend", render_marker);

// double click op the map
map.on('dblclick', (event) =>{
  //console.log(event.latlng)
  let lat = event.latlng.lat
  let lng = event.latlng.lng
  L.marker([lat, lng]).addTo(map)
  fetch(`/markers/get-nearest-station?latitude=${lat}&longitude=${lng}`).then(response => response.json()).then(result => {
    //console.log(result)
    station_coordinates = result.coordinates
    user_coordinates    = [lat, lng]
    // draw line between user location and nearest station
    let polyline = L.polyline([user_coordinates, station_coordinates]).addTo(map)
    // show popup at userlocation showing distance to nearest station
    var popup = L.popup()
    .setLatLng(user_coordinates)
    .setContent(`<p>Nearest station is ${result.distance.toFixed(2)} km away</p>`)
    .openOn(map);
  })
})