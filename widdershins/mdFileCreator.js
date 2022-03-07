const widdershins = require('widdershins'); // Used as an "import widdershins"
const fs = require('fs');

const options = {
  language_tabs: [{ java: "Java" },{ shell: "Shell" },{ python: "Python" }],};
options.language_clients = [{ 'shell': 'curl' }, { 'node': 'request' }, { 'java': 'unirest' }];
options.clipboard=true;        //must  
options.theme = 'darkula';     //must
options.search = true;         //must
options.codeSamples = true;    //must
options.headings = 2;          //must
options.httpsnipets= true;     //must
options.tocSummary = true;     //poner el nombre del summmary del endpoint         
         
const fileData = fs.readFileSync('openapi.json', 'utf8'); // OpenAPI File to be converted from JSON to .md


const swaggerFile = JSON.parse(fileData);

widdershins.convert(swaggerFile, options)
.then(markdownOutput => {
  // markdownOutput contains the converted markdown
  fs.writeFileSync('widdershins.md', markdownOutput, 'utf8'); // Name of the MarkDown generated file
})
.catch(err => {
  // handle errors
});

