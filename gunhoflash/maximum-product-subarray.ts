function maxProduct(nums: number[]): number {
  let answer = Math.max(...nums);

  let minPositiveSerialProduct = 1;
  let maxNegativeSerialProduct = 0;
  let serialProduct = 1;

  for (const num of nums) {
    serialProduct *= num;

    if (serialProduct < 0) {
      if (maxNegativeSerialProduct === 0) {
        maxNegativeSerialProduct = serialProduct;
      } else {
        answer = Math.max(answer, serialProduct / maxNegativeSerialProduct);
        maxNegativeSerialProduct = Math.max(maxNegativeSerialProduct, serialProduct);
      }
    } else if (serialProduct > 0) {
      answer = Math.max(answer, serialProduct / minPositiveSerialProduct);
      minPositiveSerialProduct = Math.min(minPositiveSerialProduct, serialProduct);
    } else {
      minPositiveSerialProduct = 1;
      maxNegativeSerialProduct = 0;
      serialProduct = 1;
    }
  }

  return answer;
}
