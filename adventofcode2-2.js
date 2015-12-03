var html = document.getElementsByTagName('pre')[0];
var input = html.innerHTML;
console.log(input);
var x = input.split('\n');
console.log(x);
var total = 0;
var arraycnt = 0;
while (arraycnt < 1000) {
    var array = x[arraycnt];
    var a = array.split("x");
    console.log(a);
    total = total + a[0]*a[1]*a[2];
    if (1*a[0] <= 1*a[1] && 1*a[0] <= 1*a[2]) {
        if(1*a[1] <= 1*a[2]) {
          total = total + (a[0]*2+a[1]*2);
        } else {
          total = total + (a[0]*2+a[2]*2);
        }
    }
    else if (1*a[1] <= 1*a[0] && 1*a[1] <= 1*a[2]) {
        if(1*a[0] <= 1*a[2]) {
          total = total + (a[1]*2+a[0]*2);
        } else {
          total = total + (a[1]*2+a[2]*2);
        }
    }
    else {
      if(1*a[0] < 1*a[1]) {
        total = total + (a[2]*2+a[0]*2);
      } else {
        total = total + (a[2]*2+a[1]*2);
      }
    }
    arraycnt = arraycnt + 1;
  }
console.log(total);
