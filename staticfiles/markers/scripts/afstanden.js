/* markers/static/markers/scripts/afstanden.js */

// Initialize the map
var map = L.map('mapid').setView([52.5, 4.95], 17);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

L.marker([52.507, 4.954]).addTo(map)
  .bindPopup('I am here.<br> Looking for markers.')
  .openPopup();

{% for marker in markers %}
  var circle = L.circle([{{ marker.location.y }}, {{ marker.location.x }}], {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5,
    radius: 5
  }).addTo(map);
{% endfor %}
// leaflet draw 
var drawnFeatures = new L.FeatureGroup();
map.addLayer(drawnFeatures);

// add drawcontrol to the map
var drawControl = new L.Control.Draw({
  // position of drawcontrols om the map
  position: "topleft",
  // add properties to objects
  draw: {
    polygon: {
      shapeOptions: {
      color: 'purple'
      },
      allowIntersection: false,
    },
    polyline: {
      shapeOptions: {
      color: 'red'
      },
    },
    rect: {
      shapeOptions: {
      color: 'green'
      },
    },
    circle: {
      shapeOptions: {
      color: 'steelblue'
      },
    },
  },
  // add edit option to drawcontrols
  edit: {
    featureGroup: drawnFeatures,
    remove: false
  },
  // add delete option to drawcontrols
  delete: {
    featureGroup: drawnFeatures,
    remove: false
  },
});
map.addControl(drawControl);

// on new drawing add popup with geodata
map.on("draw:created", function(e){
  var type  = e.layerType;
  var layer = e.layer;
  //console.log(layer.toGeoJSON())

  layer.bindPopup(`<p>${JSON.stringify(layer.toGeoJSON())}</p>`)
  drawnFeatures.addLayer(layer);
});
// edit drawing
map.on("draw:edited", function(e){
  var type   = e.layerType;
  var layers = e.layers;

  layers.eachLayer(function(layer){
  console.log(layer)
  if (type == 'Point'){
    console.log('hallo')
  }
  }) 
})