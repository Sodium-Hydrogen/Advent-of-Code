var html = document.getElementsByTagName('pre')[0];
var input = html.innerHTML;
console.log(input);
var x = input.split("");
console.log(x);
var array = 0;
var floor = 0;
while (floor > -1){
  if (x[array] == "(") {
    floor = floor + 1;
  }
  else {
    floor = floor - 1;
  }
  array = array + 1;
}
console.log(array);
