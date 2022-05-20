$(document).ready(function () {
  function showPosition(position) {
    var lat = position.coords.latitude;
    var lon = position.coords.longitude;
    var apikey='4b03add00b2574f0e040ad2ddb067742';


     console.log(lat)
     console.log(lon)
    
     $.get(
      `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${apikey}&units=metric`,
      function (data) {
       console.log(data)
      $("#futer").html(`TEMPERATURA: <img  src='http://openweathermap.org/img/wn/${data.weather[0].icon}.png' height='25px'>
      ${data.main.temp}`)}
    );

    }
  if (navigator.geolocation){
          
          navigator.geolocation.getCurrentPosition(function(posision){
            showPosition(posision);
          })
        
        }else{
          alert("navergador no soporta la geolocalizacion")
        }
  
  })
  
