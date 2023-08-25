// static/admin/show_info_popup.js

function showInfo(lat, lon, mt, inT) {
    var content = `<p>Latitude: ${lat}</p><p>Longitude: ${lon}</p><p>Magnitude: ${mt}</p><p>Intensity: ${inT}</p>`;
    
    var popup = window.open('', '_blank', 'width=300,height=200');
    popup.document.write(content);
    popup.document.close();
}
