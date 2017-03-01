// load all dependencies
var request = require('request');
var async = require('async');
var urlExpander = require('expand-url');

// add your own array of links here
var data = [ "http://bzfd.it/2g6Kraz", "http://bzfd.it/2ghsm88"
]

var counter=0;
var q = async.queue(function (shortUrl, callback) {
			// expander function 
		    urlExpander.expand(shortUrl, function(err, longUrl){
		        counter++;
		        // log the short url and the expanded url in the console
		        console.log(shortUrl + "," + longUrl);
		        callback();
		    });
		}, 100);

// runs the expander function for each data point
var i = 0;
while (i< data.length){
    q.push(data[i], function (err) {
    });
    i++;
}

// tells you in your console when you're done 
q.drain = function() {
    console.log(counter);
    console.log('all urls have been processed');
}