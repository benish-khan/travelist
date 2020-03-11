// <!-- <!DOCTYPE html>

// <head>
//     <style type="text/css">
//         html, body { height: 100%; margin: 0; padding: 0; }
//         #map { height: 100%; }
//     </style>
// </head>

// <body>
//     <div id="map"></div> -->

    // <!-- Google maps API -->
    <!-- // <script src="https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=places"></script> -->

    // <!-- what it looks like with a key -->
    <!-- // <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script> -->
    <!-- // <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script> -->
    <!-- // <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBEtBxlWamg_eBoAUrffjaDesPJPx98jQk"></script> -->
    // <!--> <script> -->

        let geocoder = new google.maps.Geocoder();

        let map = new google.maps.Map(document.querySelector('#map'),{
            center : { lat:37.7643148, lng:-122.3996072 },
            zoom:10,
            mapTypeId: 'roadmap',
            styles: [{"featureType":"all","elementType":"all","stylers":[{"color":"#d4b78f"},{"visibility":"on"}]},{"featureType":"all","elementType":"geometry.stroke","stylers":[{"color":"#0d0000"},{"visibility":"on"},{"weight":1}]},{"featureType":"administrative","elementType":"labels.text.fill","stylers":[{"color":"#98290e"},{"visibility":"on"}]},{"featureType":"administrative","elementType":"labels.text.stroke","stylers":[{"visibility":"off"}]},{"featureType":"administrative.province","elementType":"all","stylers":[{"visibility":"off"}]},{"featureType":"administrative.locality","elementType":"labels.text.fill","stylers":[{"color":"#98290e"},{"visibility":"on"}]},{"featureType":"administrative.locality","elementType":"labels.text.stroke","stylers":[{"visibility":"off"}]},{"featureType":"administrative.neighborhood","elementType":"all","stylers":[{"visibility":"on"}]},{"featureType":"landscape","elementType":"all","stylers":[{"color":"#d4b78f"},{"visibility":"on"}]},{"featureType":"poi","elementType":"all","stylers":[{"visibility":"off"}]},{"featureType":"poi.park","elementType":"all","stylers":[{"color":"#c4b17e"},{"visibility":"on"}]},{"featureType":"road","elementType":"labels.icon","stylers":[{"visibility":"off"}]},{"featureType":"road.highway","elementType":"geometry.stroke","stylers":[{"visibility":"off"}]},{"featureType":"road.highway","elementType":"labels.text.fill","stylers":[{"color":"#0d0000"},{"visibility":"on"}]},{"featureType":"road.highway","elementType":"labels.text.stroke","stylers":[{"color":"#d9be94"},{"visibility":"on"}]},{"featureType":"road.highway.controlled_access","elementType":"geometry.fill","stylers":[{"color":"#0d0000"},{"visibility":"off"},{"weight":2}]},{"featureType":"road.arterial","elementType":"all","stylers":[{"visibility":"off"}]},{"featureType":"road.local","elementType":"all","stylers":[{"visibility":"off"}]},{"featureType":"transit","elementType":"all","stylers":[{"visibility":"off"}]},{"featureType":"water","elementType":"geometry","stylers":[{"color":"#a8ac91"}]},{"featureType":"water","elementType":"labels.text.fill","stylers":[{"color":"#98290e"},{"visibility":"on"}]},{"featureType":"water","elementType":"labels.text.stroke","stylers":[{"visibility":"off"}]}]

            });

    $.get('/trip-map-data', getLatLong)

    function getLatLong(results) {
        console.log(results)
        let locations = results.locations

        for (let location of locations) {
            
            console.log(location)

            geocoder.geocode( {'address':location}, setMarker)


        }

    }

    function setMarker (results, status) {
        if (status === google.maps.GeocoderStatus.OK) {

        let marker = new google.maps.Marker({
            map: map,
            position: results[0].geometry.location
        });

    } else {
        console.log('Geocode was not successful for the following reason: ' + status);
    }    
}
    <!-- // NYC Latitude‎: ‎40.730610 Longitude‎: ‎-73.935242 -->
   <!--  // OR Lat: 45.512231, Long: -122.658719
    // locationDetails = [[37.7643148,-122.3996072,"SF"],[40.730610,-73.935242,"NY"],[45.512231,-122.658719,"OR"]]

    // for (let locationDetail of locationDetails){

    //     console.log(locationDetail)
    //     // let locationDetail = locationDetails[i].split(' ');
    //     let latitude = parseFloat(locationDetail[0]);
    //     let longitude = parseFloat(locationDetail[1]);
    //     let centerObject = new google.maps.LatLng(latitude,longitude);
    //     let name = locationDetail[2];
    //     console.log(name);
    //     console.log(latitude);
    //     console.log(longitude);
    //     // console.log(centerObject);


    //     let marker = new google.maps.Marker({
    //      position: centerObject,
    //      map: map,
    //      title: TRIP
    //    });
    // }
    // </script>

// </body> -->