function getCurrentYear() {
  const date = new Date();
  return date.getFullYear();
}

export default function getBudgetForCurrentYear(income, gdp, capita) {
  return {
    income: [`income-${getCurrentYear()}`],
    gdp: [`gdp-${getCurrentYear()}`],
    capita: [`capita-${getCurrentYear()}`], 
  }
}
