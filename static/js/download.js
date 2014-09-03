<script>
time = 5;
document.getElementById("counter").innerHTML = time;
timer = setInterval("count()", 1000);

function count()
{
  if(time == 1)
  {
    // clear timer and remove counter from page
    clearInterval(timer);
    document.getElementById("counter-text").style.display="none";
    // if you want to display link
//    document.getElementById("link").style.display="block";
    // or directly start download
    download('file.ext');
  } else {
    time--;
    document.getElementById("counter").innerHTML = time;
  }
}

function download(file)
{
  window.location=file;
}
</script>
