import {mkdir,copyFile,readFile,writeFile} from 'node:fs/promises';
await mkdir('dist/static',{recursive:true});
for(const name of ['style.css','app.js'])await copyFile('restaurant/static/'+name,'dist/static/'+name);
await writeFile('dist/index.html',(await readFile('restaurant/templates/index.html','utf8')).replace('{% csrf_token %}',''));
console.log('Static preview built. Reservations require Django.');
