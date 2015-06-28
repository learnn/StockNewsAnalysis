//Converter Class
var Converter=require("csvtojson").core.Converter;
var fs=require("fs"); 
    //new converter instance
    var csvConverter=new Converter();
    //end_parsed will be emitted once parsing finished
    csvConverter.on("end_parsed",function(jsonObj){
        if(typeof jsonObj[0].Symbol === 'undefined')  {
            console.log("Skipping");
            return;
        } else {
            fs.writeFile(jsonObj[0].Symbol + ".json", JSON.stringify(jsonObj), function(err) {
                console.log("Converted to JSON " + jsonObj[0].Symbol);
            });
        }
    });
console.log("Converting " + process.argv[2]);
fs.createReadStream(process.argv[2]).pipe(csvConverter);
