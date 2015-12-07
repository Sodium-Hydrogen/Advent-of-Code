//var html = document.getElementsByTagName('pre')[0];
//input = html.innerHTML;
var input = "qjhvhtzxzqqjkmpb"
console.log(input);
var x = input.split('\n');
console.log(x);
var array = 0;
var nice = [];
var naughty = [];
var niceArray = 0;
var naughtyArray = 0;
while (array == x.length - 1){
  var arraySub = 0;
  var arrayCal = x[array];
  var other = 0;
  var repeat = 0;
  var group = 0;
  while (arraySub < arrayCal.length){
    var a = arrayCal[arraySub];
    var b = arrayCal[arraySub + 1];
    var matching = new RegExp(a + b , 'g');
    console.log(matching);
    if (arrayCal[arraySub] == arrayCal[arraySub + 2]){
      repeat += 1;
    } else {}
    other = arrayCal.match(matching);
    if (other != null){
      group = 1;
    } else {}
    console.log(other);
    arraySub += 1;
  }
  if (repeat >= 1){
    nice[niceArray] = arrayCal;
    niceArray += 1;
  } else {
    naughty[naughtyArray] = arrayCal;
    naughtyArray += 1;
  }
  console.log(other);
  console.log(group);
  array += 1;
}
console.log(nice);
console.log(naughty);
console.log(nice.length);
console.log("exit");
