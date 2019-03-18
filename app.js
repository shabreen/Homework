// from data.js
var tableData = data;

// reference the html table body
var tbody = d3.select("tbody");

// Loop Through `data` and console.log each sightings object
data.forEach(function(sightings) {
    console.log(sightings);
    // append one table row `tr` for each sightings object
    var row = tbody.append("tr");
    // `Object.entries` to console.log each sightings value
    Object.entries(sightings).forEach(function([key, value]) {
      console.log(key, value);
      // Append a cell to the row for each value in the sightings object
      var cell = tbody.append("td");
      cell.text(value);
    });
  });

// Select the submit button
var submit = d3.select("#filter-btn");

submit.on("click", function() {

  // Prevent the page from refreshing
  d3.event.preventDefault();

  // Select the input element and get the raw HTML node
  var inputValue = d3.select("#datetime").property('value');

  //  clear text of the tds
  d3.selectAll("td").property("textContent", "");

  // delete all table rows in the table body
  d3.select("tbody").selectAll("tr").remove();

  var filteredData = tableData.filter(function(sightings) {
    return sightings.datetime === inputValue;
  })

  // append the values of the filtered date to the table
  filteredData.forEach((sightings) => {
  var row = tbody.append("tr");
  Object.entries(sightings).forEach(([key, value]) => {
      var cell = row.append("td");
      cell.text(value);
      })
  });
});
