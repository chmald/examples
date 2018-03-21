var parseXlsx = require('excel');
var asset = require('assert');

var sheetsDir = __dirname + '/spreadsheets';

require('fs').readdirSync(sheetsDir).forEach(function(file){

filename = sheetsDir + '/' + file;

console.log(filename);
parseXlsx(filename, function(err, data) {
	if(err) throw err;
	console.log(data.toString());
});

});
