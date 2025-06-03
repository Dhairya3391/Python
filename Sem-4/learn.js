async function foo(some) {
  n = 0;
  for (let i = 0; i < 5000000000; i++) {
    n = n + 1;
  }
  console.log("in foo", some);
}

async function bar(n, callback) {
  await callback(n);
  console.log("in bar", n);
}

bar(42, foo);
