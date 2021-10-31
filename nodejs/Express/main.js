const express = require('express');
const logger = require('morgan');
const app = express();
const users = [{'name': 'Alley'}, {'name': 'Endy'}];

app.get('/', (req, res) => res.send('Hello World!\n'));
app.get('/users', (req, res) => res.json(users));

app.listen(3000, () => console.log('running'));