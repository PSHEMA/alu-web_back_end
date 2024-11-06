import classRoom from './0-classroom.js';

function initializeRooms() {
  const classRoom1 = new classRoom(19);
  const classRoom2 = new classRoom(20);
  const classRoom3 = new classRoom(34);
  return [classRoom1, classRoom2, classRoom3];
}
