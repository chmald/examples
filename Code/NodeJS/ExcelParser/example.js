var parseXlsx = require('excel');
var asset = require('assert');

var filename = __dirname + '/spreadsheets/excel_mac_2011-basic.xlsx';

console.log(filename);
parseXlsx(filename, function(err, data) {
	if(err) throw err;
	console.log(data.toString());
});