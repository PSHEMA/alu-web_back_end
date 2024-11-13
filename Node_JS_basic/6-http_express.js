const express = require('express');

const app = express();
port = 1245;

app.get('/', (req, res) => {
    res.send('Hello Holberton School!');
});

app.listen(port, () => {
    // console.log(`Example app listening on port ${port}!`);
});
