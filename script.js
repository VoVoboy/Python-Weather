angular.module('tableWeather', [])
  .controller('prog', function ($scope){
    $scope.persons = [
      {"date": "14.12.2016", "temperature": "270.15/271.15", "wind": "deg 20, speed 3", "clouds": "90", "pressure": "Давление", "describ": "light snow, icon 13n, id 600, main Snow"},
      
    ];
});