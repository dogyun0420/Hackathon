function showInfo(lat, lon, mt, inT) {
    var content = `<p>Latitude: ${lat}</p><p>Longitude: ${lon}</p><p>Magnitude: ${mt}</p><p>Intensity: ${inT}</p>`;
    
    var popup = window.open('', '_blank', 'width=300,height=200');
    popup.document.write(content);
    
    var button = popup.document.createElement('button');
    button.textContent = 'Send to Main Page';
    button.onclick = function() {
        var data = {
            lat: lat,
            lon: lon,
            mt: mt,
            inT: inT
        };
        localStorage.setItem('popupData', JSON.stringify(data));
        popup.close();
    };
    popup.document.body.appendChild(button);
    
    popup.document.close();
}
