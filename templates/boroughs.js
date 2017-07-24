var colors = ["#ffcb40", "#ffba00", "#ff7d73", "#ff4e40", "#ff1300"]
var div = d3.select("body").append("div")   
            .attr("class", "tooltip")               
            .style("opacity", 0);
var geoData = {{ input|safe }}
var width = 960, 
    height = 1160;
var projection = d3.geoMercator()
                    .scale(10000)
                    .translate([width / 2, height / 2]);
var svg = d3.select("body").append("svg")
            .attr("width", width)
            .attr("height", height);
  //Determine where to center map.
var center = d3.geoCentroid(geoData);
  projection.center(center);
 
  var path = d3.geoPath().projection(projection);
  
  //Colorizing boroughs
  var boroughCodes = [];
  var tweetVolumes = [];
  d3.csv("/static/tweet-volume-borough.csv", function(data) {
	  	//add data from csv files to arrays
		data.map(function(d) {
			boroughCodes.push(d.BoroughName);
			tweetVolumes.push(d.tweets);
		})
		console.log(boroughCodes);
		console.log(tweetVolumes);
	});
	console.log(geoData.features.properties);
    // and finally draw the actual polygons
    svg.selectAll("path")
      .data(geoData.features)
      .enter()
      .append("path")
      .attr("d", path)
	  .style("fill", function(d) {
			return colors[0];
  })
