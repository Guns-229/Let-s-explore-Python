function listen() {
    var source = new EventSource("/stream/");
    var target = document.getElementById("output");
    source.onmessage = function(msg) {
        if(msg.data  == "....end...."){
            source.close();
        }else{
            target.innerHTML = msg.data + '<br>';
        }
    }
}

listen();
