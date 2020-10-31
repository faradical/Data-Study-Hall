console.log("JS form v1")

// FUNCTIONS
function createPetResults(){
    var name = d3.select("#pet-name").node().value;
    var type = d3.select("#pet-type").node().value;

    d3.select("#results")
        .append("h1").text(`Your pet's name is ${name}. It is a ${type}.`);

    d3.select("#results")
        .append("a")
        .property("href", `/pet/result2/${name}/${type}`)
        .append("button")
        .text("Click Here");
}

function DoHere(){
    console.log("button pressed")
    var fname = d3.select("#fname").node().value;
    var lname = d3.select("#lname").node().value;
    d3.select("form").append("h1").text(`Whats up ${fname} ${lname}`);
}


// EVENT LISTENERS
d3.select("#pet-button").on("click", createPetResults);
d3.select("#DonleysButton").on("click", DoHere);