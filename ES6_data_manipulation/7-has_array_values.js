export default function hasValuesFromArray(set, array) {
  for (const element of array) {
    if (!set.has(element)) return false;
  }
  return true;
}

// const hasValuesFromArray = (set, array) => array.every((element) => set.has(element));
