function productExceptSelf(nums: number[]): number[] {
  const answer = Array<number>(nums.length).fill(1);

  const reduceFunction = (serialProduct: number, num: number, i: number) => {
    answer[i] *= serialProduct;
    return serialProduct * num;
  };

  nums.reduce(reduceFunction, 1);
  nums.reduceRight(reduceFunction, 1);

  return answer;
}
