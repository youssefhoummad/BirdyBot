document.getElementById("comment").focus();



// var map;
// function initMap() {
//  map = new google.maps.Map(document.getElementById('map'), {
//   center: {lat: -34.397, lng: 150.644},
//   zoom: 8,
//   disableDefaultUI: true,
//   draggable: false
//  });
// }







// function to display msg in bottom
function gotoBottom(id){
   var element = document.getElementById(id);
   element.scrollTop = element.scrollHeight - element.clientHeight;
}


// display message
function displayMessage(content, type){
  var classEl = "justify-content-end";
  if (type === "receiver") {
    classEl =   "justify-content-start";
  };

  var conversationEl = document.getElementById("conversation");
  var messageEl = '<div class="message-body row \
                    '+ classEl + '\
                    ">\
                    <div class="message-main">\
                      <div class="\
                      '+type+'\
                      ">\
                         ' + content + '\
                      </div>\
                    </div>\
                  </div>';
  conversationEl.insertAdjacentHTML('beforeend', messageEl);

    // clear input
  if (type === "receiver") {
    document.getElementById("comment").value = "";
  };
}


function replay(){
  var text = document.getElementById("comment").value;
  displayMessage(text, "sender");
  displayMessage("ok", "receiver");
}