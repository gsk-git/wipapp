let maps;

async function initMap (lat, lng) {
    const { Map } = await google.maps.importLibrary("maps");
    
    maps = new Map(document.getElementById("map"),{
        center: { lat: -25.344, lng: 131.031 },
        zoom: 10,
        });

    const marker = new AdvancedMarkerElement({
        map: map,
        position: position,
        title: "WIPAPP",
        });
}

initMap();