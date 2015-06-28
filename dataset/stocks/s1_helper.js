var require = patchRequire(require);
var casper = require('casper').create(
        {
//            verbose: true,
  //          logLevel: "debug"
        });
var filename =  casper.cli.args[0];
var initUrl = "http://www.nseindia.com/products/dynaContent/common/productsSymbolMapping.jsp?symbol=" + casper.cli.args[0] + "&segmentLink=3&symbolCount=1&series=ALL&dateRange=24month&fromDate=&toDate=&dataType=PRICEVOLUMEDELIVERABLE";
    try {
        casper.start(initUrl, function () {
            if(this.exists('a')) {
               var str = "http://www.nseindia.com" + this.getElementAttribute('a', 'href');
               console.log("");
               this.download(str, filename + ".csv");
            }
        });
        //Execute the whole sequence
        casper.run(function () {
            this.echo('Logged in successfully');
            this.exit();
        }); 
    }  catch (err) {
        console.log("Error: couldn't read credentials " + err);
    }

