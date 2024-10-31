export default function appendToEachArrayValue(array, appendString) {
  // For...of loop
  const result = [];
  for (const value of array) {
    result.push(appendString + value);
  }
  return result;
}
