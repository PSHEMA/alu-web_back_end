const http = require('http');
const fs = require('fs').promises;

function countStudents(path) {
  return new Promise((resolve, reject) => {
    if (!path) {
      reject(new Error('Cannot load the database'));
    }
    
    fs.readFile(path, 'utf8')
      .then((data) => {
        const lines = data
          .split('\n')
          .filter((line) => line.trim().length > 0);
        
        const students = lines.slice(1);
        if (students.length === 0) {
          reject(new Error('Cannot load the database'));
        }

        const fields = {};
        students.forEach((student) => {
          const [firstname, , , field] = student.split(',');
          if (firstname && field) {
            if (!fields[field]) {
              fields[field] = {
                count: 1,
                students: [firstname],
              };
            } else {
              fields[field].count += 1;
              fields[field].students.push(firstname);
            }
          }
        });

        let response = `Number of students: ${students.length}\n`;
        for (const [field, data] of Object.entries(fields)) {
          response += `Number of students in ${field}: ${data.count}. List: ${data.students.join(', ')}\n`;
        }
        resolve(response.trim());
      })
      .catch(() => {
        reject(new Error('Cannot load the database'));
      });
  });
}

const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  
  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    const databasePath = process.argv[2];
    
    let response = 'This is the list of our students\n';
    countStudents(databasePath)
      .then((data) => {
        response += data;
        res.end(response);
      })
      .catch((error) => {
        response += error.message;
        res.end(response);
      });
  } else {
    res.end('Not found');
  }
});

app.listen(1245);

module.exports = app;
