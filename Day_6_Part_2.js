//var html = document.getElementsByTagName('pre')[0];
//input = html.innerHTML;
var input = "turn on 1,0 through 1,0"
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
  if (stuff[0] == "toggle"){
    var a = [];
    i = stuff[1].split(",");
    m = stuff[3].split(",");
    a.push(i[0]*1);
    a.push(i[1]*1);
    a.push(m[0]*1);
    a.push(m[1]*1);
    var things = a[1];
    while (things <= a[3]){
      var count = things*1000 + a[0];
      var counta = things*1000 + a[2];
      while(count <= counta){
      lights[count] += 2;
      count += 1;
      }
      things ++ ;
    }
    console.log(a);
  }
  else{
    if (stuff[1] == "on"){
      a = [];
      i = stuff[2].split(",");
      m = stuff[4].split(",");
      a.push(i[0]*1);
      a.push(i[1]*1);
      a.push(m[0]*1);
      a.push(m[1]*1);
      console.log(a);
      var things = a[1];
      while (things <= a[3]){
        var count = things*1000 + a[0];
        var counta = things*1000 + a[2];
      while(count <= counta){
        lights[count] += 1;
        count += 1;
      }
      things += 1;
      }
    } else {
       a = [];
      i = stuff[2].split(",");
      m = stuff[4].split(",");
      a.push(i[0]*1);
      a.push(i[1]*1);
      a.push(m[0]*1);
      a.push(m[1]*1);
      var things = a[1];
      while (things <= a[3]){
        var count = things*1000 + a[0];
        var counta = things*1000 + a[2];
      while(count <= counta){
        lights[count] -= 1;
        count += 1;
      }
      things += 1;
      }
    console.log(a);
    }
  }
  array += 1;
}
array = 0;
var total = 0;
while (array < lights.length){
  total += lights[array];
  array += 1;
}
console.log(total);
console.log(lights);
console.log('exit')
//17325717
//17325717
