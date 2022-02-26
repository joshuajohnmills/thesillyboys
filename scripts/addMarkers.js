
// initialize Leaflet
var map = L.map('map').setView({lon: 144.4, lat: -37.7}, 13);

// add the OpenStreetMap tiles
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
maxZoom: 19,
attribution: '&copy; <a href="https://openstreetmap.org/copyright">OpenStreetMap contributors</a>'
}).addTo(map);

L.control.scale({imperial: true, metric: true}).addTo(map);

var create = false;
// show a marker on the map

/*
L.marker({lon: 144.42, lat: -37.7}).bindPopup('Stus House').addTo(map);
L.marker({lon: 144.43, lat: -37.705}).bindPopup('Josh House').addTo(map);
L.marker({lon: 144.403, lat: -37.708}).bindPopup('Dans House').addTo(map);
L.marker({lon: 144.41, lat: -37.69}).bindPopup('Matts house').addTo(map);

L.marker({lon: 144.42, lat: -37.69}).bindPopup('Doms shack/palace').addTo(map);
*/

map.on('click', function(e) {
    //
    if(create){
        L.marker({lon: e.latlng.lng, lat:  e.latlng.lat}).bindPopup(message).addTo(map);
        create = false;
    
    $.post(
        "http://192.168.43.109:5000/event_post",
        JSON.stringify({"message": message,"latlon" : [ e.latlng.lat,e.latlng.lng] })
    )
    }
});

var current_marker;
var message = ""
const makeReadyMarker = () =>{
    message = document.getElementById("input_box").value;
    create = true;

    document.getElementById("input_box").value = "";

}
/*
const createNewMarker = (inputlon,inputlat,text) => {

    
    L.marker({lon: inputlon, lat: inputlat}).bindPopup(text).addTo(map);
}
*/
