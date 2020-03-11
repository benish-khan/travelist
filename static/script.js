function showTripResults(result) {
    console.log(result.state)
    console.log(result.city)
    $('#trips').append(`<p>${result.city} ${result.state} | <a href="/user"> <i class="fa fa-heart"></i></a></p>`)

}

function addTrip(evt) {
    evt.preventDefault();
    console.log('inside addTrip')
    var formInputs = {
        "city": $("#city").val(),
        "state": $("#state").val(),
    };
    console.log(formInputs)
    $.post("/add-trip", formInputs, showTripResults);
}

$("#add-trip").on("submit", addTrip);

//the above ajax jquery works for addTrip!

// Katie: write an ajax request in your javascript file to get the results from the new route you created
// function addMarker(evt) {
//     evt.preventDefault();
//     console.log('inside addMarker')
//     var formInputs = {
//         "city": $("#city").val(),
//         "state": $("#state").val(),

//     };
//     console.log(formInputs)
//     $.post("/trip-map", formInputs, showTripResults);


// }


// function updateTrip(evt) {
//     evt.preventDefault();
//     console.log('inside updateTrip')
//     var formInputs = {
//         "city": $("#city").val(),
//         "state": $("#state").val(),
//         "new_city": $("#new_city").val(),
//         "new_state": $("#new_state").val(),
//     };
//     console.log(formInputs)
//     $.post("update-trip", formInputs, showTripResults);
// }

// $("#update-trip").on("submit", updateTrip);

// function deleteTrip(evt) {
//     evt.preventDefault();
//     console.log('inside deleteTrip')
//     var formInputs = {
//         "city": $("#city").val(),
//         "state": $("#state").val(),
//     };
//     console.log(formInputs)
//     $.post("/delete-trip", formInputs, showTripResults);
// }

// $("#delete-trip").on("submit", deleteTrip);