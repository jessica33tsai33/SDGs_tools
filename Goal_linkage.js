var svg = d3.select("svg"),
    width = +svg.attr("width"),
    height = +svg.attr("height"),
    filename = "goalRelation.json",
    index;

var i;
//var sdgList = ['1.1', '1.2', '1.3', '1.4', '1.5', '1.a', '1.b', '2.1', '2.2', '2.3', '2.4', '2.5', '2.a', '2.b', '2.c', '3.1', '3.2', '3.3', '3.4', '3.5', '3.6', '3.7', '3.8', '3.9', '3.a', '3.b', '3.c', '3.d', '4.1', '4.2', '4.3', '4.4', '4.5', '4.6', '4.7', '4.a', '4.b', '4.c', '5.1', '5.2', '5.3', '5.4', '5.5', '5.6', '5.a', '5.b', '5.c', '6.1', '6.2', '6.3', '6.4', '6.5', '6.6', '6.a', '6.b', '7.1', '7.2', '7.3', '7.a', '7.b', '8.1', '8.2', '8.3', '8.4', '8.5', '8.6', '8.7', '8.8', '8.9', '8.10', '8.a', '8.b', '9.1', '9.2', '9.3', '9.4', '9.5', '9.a', '9.b', '9.c', '10.1', '10.2', '10.3', '10.4', '10.5', '10.6', '10.7', '10.a', '10.b', '10.c', '11.1', '11.2', '11.3', '11.4', '11.5', '11.6', '11.7', '11.a', '11.b', '11.c', '12.1', '12.2', '12.3', '12.4', '12.5', '12.6', '12.7', '12.8', '12.a', '12.b', '12.c', '13.1', '13.2', '13.3', '13.a', '13.b', '14.1', '14.2', '14.3', '14.4', '14.5', '14.6', '14.7', '14.a', '14.b', '14.c', '15.1', '15.2', '15.3', '15.4', '15.5', '15.6', '15.7', '15.8', '15.9', '15.a', '15.b', '15.c', '16.1', '16.2', '16.3', '16.4', '16.5', '16.6', '16.7', '16.8', '16.9', '16.10', '16.a', '16.b', '17.1', '17.2', '17.3', '17.4', '17.5', '17.6', '17.7', '17.8', '17.9', '17.10', '17.11', '17.12', '17.13', '17.14', '17.15', '17.16', '17.17', '17.18', '17.19'];

var color = d3.scaleOrdinal(d3.schemeCategory20);

d3.json(filename, function(error, graph) {
    if (error) throw error;

    var simulation = d3.forceSimulation()
        .force("link", d3.forceLink().id(function(d) { return d.id; }).distance(100))
        .force("charge", d3.forceManyBody())
        .force("center", d3.forceCenter(width / 2, height / 2))
        .force("attraceForce", d3.forceManyBody().strength(-1000))
        .alphaMin(1);

    var link = svg.append("g")
        .attr("class", "links")
        .selectAll("line")
        .data(graph.links)
        .enter().append("line");

    var node = svg.append("g")
        .attr("class", "nodes")
        .selectAll("node")
        .data(graph.nodes)
        .enter().append("circle");

    var image = svg.append("g")
        .attr("class", "image")
        .selectAll("image")
        .data(graph.nodes)
        .enter().append("image")
        .attr("xlink:href", function(d){ return ("img/goal/E_SDG goals_icons-individual-cmyk-" + d.group + ".jpg");})
        .attr("height", "50px")
        .attr("width", "50px");

    simulation
        .nodes(graph.nodes)
        .on("tick", ticked);

    simulation
        .force("link")
        .links(graph.links);

    function ticked() {
        graph.nodes[0].fx = 0;
        graph.nodes[0].fy = 0;

        link
            .attr("x1", function(d) { return d.source.x; })
            .attr("y1", function(d) { return d.source.y; })
            .attr("x2", function(d) { return d.target.x; })
            .attr("y2", function(d) { return d.target.y; });

        node
            .attr("cx", function(d) { return d.x; })
            .attr("cy", function(d) { return d.y; });
        image
            .attr("x", function(d) { return d.x-25; })
            .attr("y", function(d) { return d.y-25; });
    }
});