function pausecomp(millis)
{
    var date = new Date();
    var curDate = null;

    do { curDate = new Date(); }
    while(curDate-date < millis);
}

function update(data){
    document.getElementById("views2").style.display = "block"
    setTimeout(()=>{
        console.log(data)
    if(data["correct"]){
        
        var randomColor = Math.floor(Math.random() * 16777215).toString(16);
        document.getElementById("views2").style.display = "none"

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
        console.log(document.getElementById("one-cont")) //.style.backgroundColor
        
        document.getElementById("one-cont").style.backgroundColor = document.getElementById("two-cont").style.backgroundColor
        document.getElementById("two-cont").style.backgroundColor = randomColor;
        
    }else{
        // window.location.replace('play', 'gameover');
        // console.log(window.location.href)
        window.location.href = "127.0.0.1:5000/gameover"
    }},2000)
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