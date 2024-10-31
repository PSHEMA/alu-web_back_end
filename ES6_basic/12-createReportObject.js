export default function createReportObject(employeesList) {
  return {
    allemployees: {
      ...employeesList,
    },
    getNumberOfDepartments: function() {
      return Object.keys(this).length;
    }
  }
}
