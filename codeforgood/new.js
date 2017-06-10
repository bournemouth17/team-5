<script>
setInterval (function PlaySound(soundObj) {
  var sound = document.getElementById(soundObj);
  sound.Play();
}, 10000);
</script>

<embed src="{{ url_for('static', filename='beeping.mp3') }}" autostart="false" width="0" height="0" id="soundObj"
enablejavascript="true">

