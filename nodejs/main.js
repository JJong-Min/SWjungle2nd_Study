var http = require('http');
var fs = require('fs');
var url = require('url');
var qs = require('querystring');

var app = http.createServer(function(request,response){
    var _url = request.url;
    var queryData = url.parse(_url, true).query;
    var pathname = url.parse(_url, true).pathname;

    console.log(url.parse(_url, true));
    if (pathname === '/') {
      fs.readFile(`data/${queryData.id}`, 'utf-8', function(err, description){
        var title = queryData.id;
        if (queryData.id === undefined) {
          var title = 'Welcome';
          var description = 'Hello, Node.js';
        }
        fs.readdir('./data', function(error, filelist){
          var list = `<ul>`;
          var i = 0;
          while(i < filelist.length) {
            list += `<li> <a href="/?id=${filelist[i]}"> ${filelist[i]}</a> </li>`;
            i += 1;  
          }
          list += `</ul>`
          var template = `
          <!doctype html>
          <html>
          <head>
            <title>WEB1 - ${title}</title>
            <meta charset="utf-8">
          </head>
          <body>
            <h1><a href="/">WEB</a></h1>
            ${list}
            <a href="/create">create</a>
            <h2>${title}</h2>
            <p>${description}</p>
          </body>
          </html>
          `;   
          response.writeHead(200);
          response.end(template);
        })
      });
  } else if (pathname === '/create') {
    fs.readdir('./data', function(error, filelist){
      var list = `<ul>`;
      var i = 0;
      while(i < filelist.length) {
        list += `<li> <a href="/?id=${filelist[i]}"> ${filelist[i]}</a> </li>`;
        i += 1;  
      }
      list += `</ul>`
      var template = `
      <!doctype html>
      <html>
      <head>
        <title>WEB1 - Create</title>
        <meta charset="utf-8">
      </head>
      <body>
        <h1><a href="/">WEB</a></h1>
        ${list}
        <form action="http://localhost:3000/create_process" method="post">
          <p><input type="text" name="title" placeholder="title"></p>
          <p>
            <textarea name="description" placeholder="description"></textarea>
          </p>
          <p>
            <input type="submit">
          </p>
      </body>
      </html>
      `;   
      response.writeHead(200);
      response.end(template);
    });

  } else if (pathname === '/create_process'){
    var body = '';
    request.on('data', function(data) {
      body += data;
    });
    request.on('end', function() {
      var post = qs.parse(body);
      var title = post.title;
      var description = post.description;
      fs.writeFile(`data/${title}`, description, 'utf-8', function(error){
        response.writeHead(302, {location: `/?id=${title}`});
        response.end('success');
      });
    });

  } else {
    response.writeHead(404);
    response.end('Not Found');
  }
});
app.listen(3000);