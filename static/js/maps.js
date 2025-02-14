async function initMap () {
    const { Map } = await google.maps.importLibrary("maps");
    const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");
    const places = [
        ["Parking A1",13.0436,80.2722],
        ["Parking A2",13.0455,80.2701],
        ["Parking A3",13.0660,80.2819],
        ["Parking A4",13.0638,80.2664],
        ["Parking A5",13.0406,80.2772],
        ["Parking A6",13.0612,80.2443],
        ["Parking A7",12.8499,80.2348],
        ["Parking A8",12.9948,80.2243],
        ["Parking A9",13.0168,80.2922],
        ["Parking A10",13.0011,80.2091]];
    const map = new Map(document.getElementById("map"),{
        center: { lat: 13.0843, lng: 80.2705 },
        zoom: 12,
        mapId: "a988f1de55e37650",
    });

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition((position) => {
            pos = {lat: position.coords.latitude, lng: position.coords.longitude,};
            map.setCenter(pos);
            const icon = document.createElement("div");
            icon.innerHTML = '<i class="fa-brands fa-product-hunt fa-beat fa-2xl"></i>'
            const pin = new google.maps.marker.PinElement({
                scale: 1.5,
                glyph: icon,
                glyphColor: "rgb(145, 114, 4)",
                background: "#ffd43b",
                borderColor:"rgb(192, 150, 0)",
            });
            const marker = new AdvancedMarkerElement({
                map,
                position: map.getCenter(),
                content: pin.element,
            });
        },
        () => {
            alert("Unable to retrieve your location");
        });
    } else {
        alert("Your browser does not support geolocation");
    }
}

initMap();