document.getElementById('play123').onclick = function() {
    say(document.getElementById('exampleFormControlTextarea4').value);
  }
  
function say(m , rate=1, pitch=0.8) {
    var msg = new SpeechSynthesisUtterance();
    var voices = window.speechSynthesis.getVoices();
    msg.voice = voices[1];
    msg.voiceURI = "native";
    msg.volume = 1;
    msg.rate = rate;
    msg.pitch = pitch;
    msg.text = m;
    msg.lang = 'en-US';
    speechSynthesis.speak(msg);
 }