// markers/static/markers/scripts/show_marker.js

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

// function to render marker; add marker tot the leaflet map
async function render_marker() {
  // set drf url for marker
  const marker_url = `/api/markers/v1/1/`;
  // bevraag de url
  const response   = await fetch(marker_url);
  // retrieve json
  const geojson    = await response.json();
  // extract lat en lon from geojson
  const latitude  = geojson.geometry.coordinates[0].toFixed(4);
  const longitude = geojson.geometry.coordinates[1].toFixed(4);
  // load lat en lon in dom elements
  document.getElementById('lat').textContent = latitude;
  document.getElementById('lon').textContent = longitude;
  
  // replace Leaflet's default blue marker with a custom icon
  function createCustomIcon (feature, latlng) {
    let myIcon = L.icon({
      iconUrl      : 'static/images/leaf-green.png',
      shadowUrl    : 'https://leafletjs.com/examples/custom-icons/leaf-shadow.png',
      iconSize     : [38, 95], // width and height of the image in pixels
      shadowSize   : [50, 64], // width, height of optional shadow image
      iconAnchor   : [22, 94], // point of the icon which will correspond to marker's location
      shadowAnchor : [4, 62],  // anchor point of the shadow. should be offset
      popupAnchor  : [-3, -76] // point from which the popup should open relative to the iconAnchor
    });
    return L.marker(latlng, { icon: myIcon })
  }
  // create an options object that specifies which function will called on each feature
  let myLayerOptions = {
    pointToLayer: createCustomIcon
  }
  // create the GeoJSON layer
  L.geoJSON(geojson, myLayerOptions)
    .bindPopup((layer) => layer.feature.properties.name)
    .addTo(map)
}

// add marker to map
map.on("moveend", render_marker);
