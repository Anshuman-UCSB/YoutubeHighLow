var score = 0;

function displayScore(){
    
}

function update(data){
    if(data["correct"]){
        document.getElementById("streak").innerHTML="Streak: "+String(data["score"]);
        var card1 = data["card1"];
        document.getElementById("img1").src=card1[0]
        document.getElementById("video-title1").innerHTML=card1[1]
        document.getElementById("channel1").innerHTML=card1[2]
        document.getElementById("views1").innerHTML=card1[3]

        var card2 = data["card2"];
        document.getElementById("img2").src=card2[0]
        document.getElementById("video-title2").innerHTML=card2[1]
        document.getElementById("channel2").innerHTML=card2[2]
        document.getElementById("views2").innerHTML=card2[3]
        
    }
}

$(function() {
    $('div#one-cont').on('click', function(e) {
    e.preventDefault()
    $.getJSON('/api',
        {"id":1, "sel":document.getElementById("views1").innerHTML,
        "notsel":document.getElementById("views2").innerHTML},
        function(data){update(data)});
    return false;
    });
});

$(function() {
    $('div#two-cont').on('click', function(e) {
    e.preventDefault()
    $.getJSON('/api',
        {"id":2, "sel":document.getElementById("views2").innerHTML,
        "notsel":document.getElementById("views1").innerHTML},
        function(data){update(data)});
    return false;
    });
});