const class2019 = new HolbertonClass(2019, 'San Francisco');
const class2020 = new HolbertonClass(2020, 'San Francisco');

export class HolbertonClass {
  constructor(year, location) {
    this._year = year;
    this._location = location;
  }

  get year() {
    return this._year;
  }

  get location() {
    return this._location;
  }
}

export class StudentHolberton extends HolbertonClass {
  constructor(firstName, lastName, year, location) {
    super(year, location);
    this._firstName = firstName;
    this._lastName = lastName;
  }

  get fullName() {
    return `${this._firstName} ${this._lastName}`;
  }

  get fullStudentDescription() {
    return `${this._firstName} ${this._lastName} - ${this.year} - ${this.location}`;
  }
}

const student1 = new StudentHolberton('Guillaume', 'Salva', 2020, 'San Francisco');
const student2 = new StudentHolberton('John', 'Doe', 2020, 'San Francisco');
const student3 = new StudentHolberton('Albert', 'Clinton', 2019, 'San Francisco');
const student4 = new StudentHolberton('Donald', 'Bush', 2019, 'San Francisco');
const student5 = new StudentHolberton('Jason', 'Sandler', 2019, 'San Francisco');

export const listOfStudents = [student1, student2, student3, student4, student5];
