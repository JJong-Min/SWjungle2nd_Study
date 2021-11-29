const express = require('express');
const app = express();
const users = [{'name': 'Alley'}, {'name': 'Endy'}];

app.get('/', (req, res) =>
{console.log("hello");
res.send('Hello World!\n');}
);
app.get('/users', (req, res) => res.json(users));

app.listen(8080, () => console.log('running'));