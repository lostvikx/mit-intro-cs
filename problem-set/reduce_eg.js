const mixed = [1, 2, "a", 3, 4.1];

const square_ints = mixed.reduce((acc, x) => {

  if (typeof x == "number" && Math.floor(x) === x) {
    acc.push(x*x);
  }
  
  return acc;
}, []);

console.log(square_ints);