function threeSum(_nums: number[]): number[][] {
  const nums = JSON.parse(JSON.stringify(_nums)) as number[];
  nums.sort();

  const nNumMap = nums.reduce<Record<string, number>>((map, v) => {
    const key = v.toString();
    map[key] = (map[key] || 0) + 1;
    return map;
  }, {});

  const answer: number[][] = [];
  let prevNum1;
  for (let i = 0; i < nums.length; i++) {
    const num1 = nums[i];
    if (num1 === prevNum1) continue;
    prevNum1 = num1;

    let prevNum2;
    for (let j = i + 1; j < nums.length; j++) {
      const num2 = nums[j];
      if (num2 === prevNum2) continue;
      prevNum2 = num2;

      const target = (num1 + num2) * -1;
      if (target < num2) continue;

      const nTarget = (nNumMap[target] || 0)
        - (num1 === target ? 1 : 0)
        - (num2 === target ? 1 : 0);
      if (nTarget > 0) {
        answer.push([num1, num2, target]);
      }
    }
  }

  return answer;
}
