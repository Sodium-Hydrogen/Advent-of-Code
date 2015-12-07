var html = document.getElementsByTagName('pre')[0];
input = html.innerHTML;
console.log(input);
var x = input.split('\n');
console.log(x);
var array = 0;
var nice = [];
var naughty = [];
var niceArray = 0;
var naughtyArray = 0;
while (array < x.length - 1){
  var arraySub = 0;
  var arrayCal = x[array];
  var other = 0;
  var vowel = 0;
  var repeat = 0;
  while (arraySub < arrayCal.length){
    if (arrayCal[arraySub] == "a"){
      vowel += 1;
    } else {}
    if (arrayCal[arraySub] == "e"){
      vowel += 1;
    } else {}
    if (arrayCal[arraySub] == "i"){
      vowel += 1;
    } else {}
    if (arrayCal[arraySub] == "o"){
      vowel += 1;
    } else {}
    if (arrayCal[arraySub] == "u"){
      vowel += 1;
    } else {}
    if (arrayCal[arraySub] == arrayCal[arraySub + 1]){
      repeat += 1;
    } else {}
    if (arrayCal[arraySub] == "a" && arrayCal[arraySub + 1] == "b"){
      other = 1;  
    } else {}
    if (arrayCal[arraySub] == "c" && arrayCal[arraySub + 1] == "d"){
      other = 1;  
    } else {}
    if (arrayCal[arraySub] == "p" && arrayCal[arraySub + 1] == "q"){
      other = 1;  
    } else {}
    if (arrayCal[arraySub] == "x" && arrayCal[arraySub + 1] == "y"){
      other = 1;  
    } else {}
    arraySub += 1;
  }
  if (vowel >= 3 && repeat >= 1 && other == 0){
    nice[niceArray] = arrayCal;
    niceArray += 1;
  } else {
    naughty[naughtyArray] = arrayCal;
    naughtyArray += 1;
  }
  array += 1;
}
console.log(nice);
console.log(naughty);
console.log(arrayCal.length);
console.log(nice.length);
console.log("exit");var html = document.getElementsByTagName('pre')[0];
input = html.innerHTML;
console.log(input);
var x = input.split('\n');
console.log(x);
var array = 0;
var nice = [];
var naughty = [];
var niceArray = 0;
var naughtyArray = 0;
while (array < x.length - 1){
  var arraySub = 0;
  var arrayCal = x[array];
  var other = 0;
  var vowel = 0;
  var repeat = 0;
  while (arraySub < arrayCal.length){
    if (arrayCal[arraySub] == "a"){
      vowel += 1;
    } else {}
    if (arrayCal[arraySub] == "e"){
      vowel += 1;
    } else {}
    if (arrayCal[arraySub] == "i"){
      vowel += 1;
    } else {}
    if (arrayCal[arraySub] == "o"){
      vowel += 1;
    } else {}
    if (arrayCal[arraySub] == "u"){
      vowel += 1;
    } else {}
    if (arrayCal[arraySub] == arrayCal[arraySub + 1]){
      repeat += 1;
    } else {}
    if (arrayCal[arraySub] == "a" && arrayCal[arraySub + 1] == "b"){
      other = 1;  
    } else {}
    if (arrayCal[arraySub] == "c" && arrayCal[arraySub + 1] == "d"){
      other = 1;  
    } else {}
    if (arrayCal[arraySub] == "p" && arrayCal[arraySub + 1] == "q"){
      other = 1;  
    } else {}
    if (arrayCal[arraySub] == "x" && arrayCal[arraySub + 1] == "y"){
      other = 1;  
    } else {}
    arraySub += 1;
  }
  if (vowel >= 3 && repeat >= 1 && other == 0){
    nice[niceArray] = arrayCal;
    niceArray += 1;
  } else {
    naughty[naughtyArray] = arrayCal;
    naughtyArray += 1;
  }
  array += 1;
}
console.log(nice);
console.log(naughty);
console.log(arrayCal.length);
console.log(nice.length);
console.log("exit");
