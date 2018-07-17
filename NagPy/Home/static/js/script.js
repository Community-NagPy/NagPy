$(document).ready(function() {
  $("#toggle").click(function() {
    $(this).toggleClass("active");
    $("#overlay").toggleClass("open");
    $("#ttl").toggleClass("txt-white");
  });
});

console.log("i am script");
console.log($);
