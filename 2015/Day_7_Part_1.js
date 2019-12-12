var html = document.getElementsByTagName('pre')[0];
input = html.innerHTML;
var x = input.split('\n');
console.log(x);
var i = 0;
var array = [];
var circut = [];
while (i < x.length - 1){
  array = x[i].split(" ");
  
  i++;
}
