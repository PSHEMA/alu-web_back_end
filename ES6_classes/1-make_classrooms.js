import ClassRoom from './0-classroom.js';

function initializeRooms() {
  const ClassRoom1 = new ClassRoom(19);
  const ClassRoom2 = new ClassRoom(20);
  const ClassRoom3 = new ClassRoom(34);
  return [ClassRoom1, ClassRoom2, ClassRoom3];
}
