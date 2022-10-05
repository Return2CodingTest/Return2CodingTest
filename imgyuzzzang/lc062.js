// 62. Unique Paths

/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
const uniquePaths = (m, n) => {
  let factorialTarget = 1;
  let multiplier = 2;
  let factorialM = 1;
  let factorialN = 1;
  const target = m + n - 2;

  while (multiplier <= target) {
    factorialTarget *= multiplier;

    if (multiplier === m - 1) {
      factorialM = factorialTarget;
    }
    if (multiplier === n - 1) {
      factorialN = factorialTarget;
    }
    multiplier += 1;
  }

  return factorialTarget / factorialM / factorialN;
};

// 다른 방법

const multiplyNtoM = (n, m) => {
  if (n * m === 0 || n > m) {
    return 1;
  }

  let start = n;
  while (n < m) {
    n += 1;
    start *= n;
  }
  return start;
};

const uniquePaths2 = (m, n) => {
  const { min, max } =
    m < n ? { max: n - 1, min: m - 1 } : { max: m - 1, min: n - 1 };

  const denominator = multiplyNtoM(1, min);
  const numerator = multiplyNtoM(max + 1, min + max);

  return numerator / denominator;
};
