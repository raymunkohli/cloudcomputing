// using jQuery
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}


function onSignIn(googleUser) {
  var profile = googleUser.getBasicProfile();
  var id_token = googleUser.getAuthResponse().id_token;
  console.log('ID: ' + id_token); // Do not send to your backend! Use an ID token instead.
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "https://directed-sonar-234413.appspot.com/loggedin");
  xhr.setRequestHeader('Content-Type', 'application/json');
  console.log("ayylmao")
  data = {
    "id": id_token
  }
  console.log(JSON.stringify(data))
  xhr.send(JSON.stringify(data));
  xhr.onloadend = function () {
    location.reload()
  }
}
function signOutold() {
  gapi.load('auth2', function () {
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
      console.log('User signed out.');
    });

  })
}

function signOut() {
  gapi.load('auth2', function () {
    gapi.auth2.init().then(function () {
      var auth2 = gapi.auth2.getAuthInstance();
      auth2.signOut().then(function () {
        document.location.href = '/logout';
      });
    });
  });
}
