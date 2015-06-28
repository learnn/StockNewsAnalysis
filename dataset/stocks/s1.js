//Download CSV from NSE exchange for all scrips
var Converter=require("csvtojson").core.Converter;

var fs=require("fs"); 
//CSV File Path or CSV String or Readable Stream Object
var csvFileName="./test.csv";

//new converter instance
var csvConverter=new Converter();
var i = 0;
//end_parsed will be emitted once parsing finished
csvConverter.on("end_parsed",function(jsonObj){
    var _ = require('underscore');
    var a = _.uniq(jsonObj, false, function(elem) { 
        return elem.SYMBOL;
    });
    a.forEach(function(elem) {
        i++;
        setTimeout(function () {
        console.log(elem); //here is your result json object
        var child_process = require('child_process');
        var ref = child_process.execFile('casperjs',
            ['s1_helper.js', elem.SYMBOL],
            {cwd: './', env: process.env}, function _execFileCb(error, stdout, stderr) {
                                                                                           console.log("Printing" + elem.SYMBOL);
                                                                                       });
        }, 1000 + i * 500);
    });
});

//read from file
fs.createReadStream(csvFileName).pipe(csvConverter);
