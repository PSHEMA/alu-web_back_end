import fs from 'fs';
import path from 'path';

export const readDatabase = (filePath) => {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) {
        reject(err);
      } else {
        try {
          const rows = data.split('\n').map(row => row.split(','));
          const studentsByField = {};
          
          rows.forEach(([firstName, major]) => {
            if (!studentsByField[major]) {
              studentsByField[major] = [];
            }
            studentsByField[major].push(firstName);
          });

          resolve(studentsByField);
        } catch (err) {
          reject(err);
        }
      }
    });
  });
};
