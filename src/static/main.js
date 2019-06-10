
document.getElementById("input").focus();



// function to display msg in bottom
function gotoBottom(){
   var element = document.getElementById("conversation");
   element.scrollTop = element.scrollHeight - element.clientHeight;
}


// display message
function displayMessage(content, type){
  var classEl = "justify-content-end";
  // if message sended buble message must be in right side
  if (type === "receiver") {
    classEl =   "justify-content-start";
  };
  // zone of conversation
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
  // append messageEl in zone of conversation
  conversationEl.insertAdjacentHTML('beforeend', messageEl);

  // clear input
  if (type === "receiver") {
    document.getElementById("input").value = "";
  };
}


function displayMap(query){
  var zoomLevel = 10;
  var url = 'https://maps.google.com/maps?q='+query+'&t=&z='+zoomLevel+'&ie=UTF8&iwloc=&output=embed';
  var mapEl = '<iframe width="100%" height="100%" id="gmap_canvas" src='+url+' frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe>';
  displayMessage('<div id="map">'+mapEl+'</div>', "receiver");
}


async function getJson(query){
  var response = await fetch('/result/rr');
  var data = await response.json();

  return data.city;
}



async function replay(){
  var text = document.getElementById("input").value;
  displayMessage(text, "sender");

  displayMessage("you ask me about "+text+"?", "receiver");

  displayMap(text);

  displayMessage("for more infos: <a>Click here</a>", "receiver");

  displayMessage(await getJson(""), "receiver");

  document.getElementById("input").value =  "";

  gotoBottom();
}
