function GetBatteryCharge() {
    // create a new XMLHttpRequest object
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/GetBattery', true);
  
    xhr.onload = function() {
      if (xhr.status === 200) {
        var imgUrl = '';
        // load the specific picture of battery charge
        switch (true) {
            case parseInt(xhr.responseText) > 80:
                imgUrl = '/static/img/battery_100.svg';
                break;
            case parseInt(xhr.responseText) > 60:
                imgUrl = '/static/img/battery_75.svg';
                break;
            case parseInt(xhr.responseText) > 40:
                imgUrl = '/static/img/battery_50.svg';
                break;
            case parseInt(xhr.responseText) > 10:
                imgUrl = '/static/img/battery_25.svg';
                break;
            default:
                imgUrl = '/static/img/battery_0.svg';
                break;
        }
        document.getElementById('imgBatteryCharge').src = imgUrl;
        document.getElementById('imgBatteryCharge').title = xhr.responseText + "%";
      }
    };
  
    // send the request
    xhr.send();
}

function GetVersion(){
    // create a new XMLHttpRequest object
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/GetVersion', true);

    xhr.onload = function() {
      if (xhr.status === 200) {
        document.getElementById('Version').innerText = 'Version: ' + xhr.responseText;
      }
    }
    xhr.send();
}

$(document).ready(function() {
    // get the battery charge
    GetBatteryCharge();

    // get battery charge every 60 seconds
    setInterval(GetBatteryCharge, 60000);
    
    // get the version
    GetVersion();

    var isTouchedOrPressed = false;
    var debounceTimeout = null;

    function debounceAction(endpoint) {
        if (!isTouchedOrPressed) {
            isTouchedOrPressed = true;
            // Call the corresponding Flask route
            $.ajax({
                type: 'GET',
                url: endpoint,  // Replace with your Flask endpoint URL
                success: function(response){
                    $('#logDiv').append('<p>' + response + '</p>');
                }
            });

            debounceTimeout = setTimeout(function() {
                isTouchedOrPressed = false;
            }, 5000); // Adjust the delay as needed (in milliseconds)
        }
    }

    // Event handlers for touchstart and mousedown on specific divs
    $("#driveforward, #driveleft, #driveright, #drivebackward, #drivebrake").on('touchstart mousedown', function(event) {
        var endpoint = '';
        switch ($(this).attr('id')) {
            case 'driveforward':
                endpoint = '/Forward';
                $(this).css('background-position', '0 -90px');
                break;
            case 'driveleft':
                endpoint = '/Left';
                $(this).css('background-position', '-90px 0');
                break;
            case 'driveright':
                endpoint = '/Right';
                $(this).css('background-position', '-90px 0');
                break;
            case 'drivebackward':
                endpoint = '/Backward';
                $(this).css('background-position', '0 -90px');
                break;
            case 'drivebrake':
                endpoint = '/Stop';
                $(this).css('background-position', '-150px 0');
                break;
            default:
                break;
        }
        debounceAction(endpoint);
    });

    // Event handler for touchend and mouseup on specific divs
    $("#driveforward, #driveleft, #driveright, #drivebackward, #drivebrake").on('touchend mouseup', function(event) {
        clearTimeout(debounceTimeout);
        isTouchedOrPressed = false;
        // Call the '/Stop' Flask route
        $.ajax({
            type: 'GET',
            url: '/Stop',  // Replace with your Flask endpoint URL
        });
        $(this).css('background-position', '0 0');
    });
    
    // Disable context menu on long touch (press and hold)
    $("#driveforward, #driveleft, #driveright, #drivebackward, #drivebrake").on('contextmenu', function(event) {
        event.preventDefault();
    });
});