function openDict(evt, Word) {
  var i, meaning, tabs;
  meaning = document.getElementsByClassName("meaning");
  for (i = 0; i < meaning.length; i++) {
    meaning[i].style.display = "none";
  }
  tabs = document.getElementsByClassName("tabs");
  for (i = 0; i < tabs.length; i++) {
    tabs[i].className = tabs[i].className.replace(" active", "");
  }
  document.getElementById(Word).style.display = "block";
  evt.currentTarget.className += " active";
}

function openIdio(evt, Idiom) {
    var i, meaning, tabs;
    meaning = document.getElementsByClassName("meaning");
    for (i = 0; i < meaning.length; i++) {
        meaning[i].style.display = "none";
    }
    tabs = document.getElementsByClassName("tabs");
    for (i = 0; i < tabs.length; i++) {
        tabs[i].className = tabs[i].className.replace(" active", "");
    }
    document.getElementById(Idiom).style.display = "block";
    evt.currentTarget.className += " active";
}
