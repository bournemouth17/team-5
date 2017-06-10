<script>
setInterval (function PlaySound(soundObj) {
  var sound = document.getElementById(soundObj);
  sound.Play();
}, 10000);
</script>

<embed src="beeping.wav" autostart="false" width="0" height="0" id="soundObj"
enablejavascript="true">

