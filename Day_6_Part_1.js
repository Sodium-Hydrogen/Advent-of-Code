var html = document.getElementsByTagName('pre')[0];
input = html.innerHTML;
console.log(input);
var other = input.split('\n');
console.log(other);
var x = 0;
var y = 0;
var array = 0;
var stuff = 0;
var lights = [];
var i = [];
var m = [];
while(array <= 999999){
  lights[array] = 0;
  array += 1;
}
array = 0;
console.log(lights);
while (array < other.length - 1){
  stuff = other[array].split(" ");
  console.log(stuff);
  if (stuff[0] == "toggle"){
    var a = [];
    i = stuff[1].split(",");
    m = stuff[3].split(",");
    a.push(i[0]*1)
    a.push(i[1]*1);
    a.push(m[0]*1);
    a.push(m[1]*1);
    console.log(a);
  }
  array += 1;
}
console.log('exit')
