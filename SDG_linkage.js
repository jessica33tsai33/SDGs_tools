var svg = d3.select("svg"),
    width = +svg.attr("width"),
    height = +svg.attr("height"),
    //filename = "finalData_",
    useOrcause = "",
    headContext = "",
    index;

var i;
var sdgList = ['1.1', '1.2', '1.3', '1.4', '1.5', '1.a', '1.b', '2.1', '2.2', '2.3', '2.4', '2.5', '2.a', '2.b', '2.c', '3.1', '3.2', '3.3', '3.4', '3.5', '3.6', '3.7', '3.8', '3.9', '3.a', '3.b', '3.c', '3.d', '4.1', '4.2', '4.3', '4.4', '4.5', '4.6', '4.7', '4.a', '4.b', '4.c', '5.1', '5.2', '5.3', '5.4', '5.5', '5.6', '5.a', '5.b', '5.c', '6.1', '6.2', '6.3', '6.4', '6.5', '6.6', '6.a', '6.b', '7.1', '7.2', '7.3', '7.a', '7.b', '8.1', '8.2', '8.3', '8.4', '8.5', '8.6', '8.7', '8.8', '8.9', '8.10', '8.a', '8.b', '9.1', '9.2', '9.3', '9.4', '9.5', '9.a', '9.b', '9.c', '10.1', '10.2', '10.3', '10.4', '10.5', '10.6', '10.7', '10.a', '10.b', '10.c', '11.1', '11.2', '11.3', '11.4', '11.5', '11.6', '11.7', '11.a', '11.b', '11.c', '12.1', '12.2', '12.3', '12.4', '12.5', '12.6', '12.7', '12.8', '12.a', '12.b', '12.c', '13.1', '13.2', '13.3', '13.a', '13.b', '14.1', '14.2', '14.3', '14.4', '14.5', '14.6', '14.7', '14.a', '14.b', '14.c', '15.1', '15.2', '15.3', '15.4', '15.5', '15.6', '15.7', '15.8', '15.9', '15.a', '15.b', '15.c', '16.1', '16.2', '16.3', '16.4', '16.5', '16.6', '16.7', '16.8', '16.9', '16.10', '16.a', '16.b', '17.1', '17.2', '17.3', '17.4', '17.5', '17.6', '17.7', '17.8', '17.9', '17.10', '17.11', '17.12', '17.13', '17.14', '17.15', '17.16', '17.17', '17.18', '17.19'];

var color = d3.scaleOrdinal().range(["firebrick", "forestgreen", "lightsteelblue"]);
//var linkType = ["neutral", "positive", "negative"];
var colorLink = d3.scaleOrdinal().range(["#808080", "blue", "red"]);
var head = document.getElementById("heading");

function useFile() {
    filename = "finalData_use.json";
    useOrcause = "use";
    postData();
}

function causeFile() {
    filename = "finalData_cause.json";
    useOrcause = "cause";
    postData();
}

function postData() {
    d3.select("svg").remove();
    document.getElementById("heading").innerText = "";

    window.sdgTarget = document.getElementById("SDG_Input").value;
    //alert("你輸入的使用者帳號為：" + window.username + '\n' + "已輸入密碼：" + window.password);
    //index = findIndex(window.sdgTarget);
    if (useOrcause == "use") {
        drawUse(findIndex(window.sdgTarget), sdgTarget);
    } else if (useOrcause == "cause") {
        drawCause(findIndex(window.sdgTarget, sdgTarget));
    }

    console.log(window.sdgTarget);
}

function findIndex(sdgTarget) {
    console.log("finding index...")
    for (i = 0; i < sdgList.length; i++) {
        console.log(i);
        if (String(sdgTarget) == sdgList[i]) {
            //console.log("index =", i);
            return i;
        }
    }
}


function drawUse(index, sdgTarget) {

    console.log("index =", i);

    headContext = "Use Tree of SDG " + sdgTarget;
    var h3 = document.createElement('h3');
    h3.innerHTML = headContext;
    head.appendChild(h3);

    var svg = d3.selectAll(".container").append("svg")
        .attr("width", 1100)
        .attr("height", 800);

    svg.append('defs')
        .append('marker')
        .attr('id', "arrow0")
        .attr('viewBox', '-0 -5 10 10')
        .attr('refX', 23)
        .attr('refY', 0)
        .attr('orient', 'auto')
        .attr('markerWidth', 10)
        .attr('markerHeight', 10)
        .attr('xoverflow', 'visible')
        .append('svg:path')
        .attr('d', 'M 0,-5 L 10 ,0 L 0,5')
        .attr('fill', colorLink(0))
        .style('stroke', 'none');

    svg.append('defs')
        .append('marker')
        .attr('id', "arrow1")
        .attr('viewBox', '-0 -5 10 10')
        .attr('refX', 23)
        .attr('refY', 0)
        .attr('orient', 'auto')
        .attr('markerWidth', 10)
        .attr('markerHeight', 10)
        .attr('xoverflow', 'visible')
        .append('svg:path')
        .attr('d', 'M 0,-5 L 10 ,0 L 0,5')
        .attr('fill', colorLink(1))
        .style('stroke', 'none');

    svg.append('defs')
        .append('marker')
        .attr('id', "arrow2")
        .attr('viewBox', '-0 -5 10 10')
        .attr('refX', 23)
        .attr('refY', 0)
        .attr('orient', 'auto')
        .attr('markerWidth', 10)
        .attr('markerHeight', 10)
        .attr('xoverflow', 'visible')
        .append('svg:path')
        .attr('d', 'M 0,-5 L 10 ,0 L 0,5')
        .attr('fill', colorLink(2))
        .style('stroke', 'none');

    d3.json(filename, function(error, graph) {
        if (error) throw error;

        var simulation = d3.forceSimulation()
            .force("link", d3.forceLink().id(function(d) { return d.id; }).distance(100))
            .force("charge", d3.forceManyBody())
            .force("center", d3.forceCenter(graph.factors_use[index].nodes[0].x, graph.factors_use[index].nodes[0].y))
            .force("attraceForce", d3.forceManyBody().strength(-250))
            .alphaMin(1);

        var link = svg.append("g")
            .attr("class", "links")
            .selectAll("line")
            .data(graph.factors_use[index].links)
            .enter().append("line")
            .attr('marker-end', function(d) { return "url(#arrow" + d.relation + ")"; })
            .style("stroke", function(d) { return colorLink(d.relation); });

        var node = svg.append("g")
            .attr("class", "nodes")
            .selectAll("circle")
            .data(graph.factors_use[index].nodes)
            .enter().append("circle")
            .attr("r", 13)
            .attr("fill", "#fff")
            .style("stroke-width", 2)
            .style("stroke", function(d) { return color(d.group + 1); });

        // This is the label for each node
        var text = svg.append("g").selectAll("text")
            .data(graph.factors_use[index].nodes)
            .enter().append("text")
            .attr("dx", 0)
            .attr("dy", 3)
            .attr("font-size", "10px")
            .text(function(d) { return d.id; })
            .attr("text-anchor", "middle");

        const edgepaths = svg.selectAll(".edgepath") //make path go along with the link provide position for link labels
            .data(graph.factors_use[index].links)
            .enter()
            .append('path')
            .attr('class', 'edgepath')
            .attr('fill-opacity', 0)
            .attr('stroke-opacity', 0)
            .attr('id', function(d, i) { return 'edgepath' + i })
            .style("pointer-events", "none");

        node.append("title")
            .text(function(d) { return d.id; });

        simulation
            .nodes(graph.factors_use[index].nodes)
            .on("tick", ticked);

        simulation
            .force("link")
            .links(graph.factors_use[index].links);

        function ticked() {
            graph.factors_use[index].nodes[0].fx = 0;
            graph.factors_use[index].nodes[0].fy = 0;

            link
                .attr("x1", function(d) { return d.source.x; })
                .attr("y1", function(d) { return d.source.y; })
                .attr("x2", function(d) { return d.target.x; })
                .attr("y2", function(d) { return d.target.y; })
                .attr("transform", function(d) {
                    return "translate(" + width / 2 + "," + height / 2 + ")";
                });

            node
                .attr("cx", function(d) { return d.x; })
                .attr("cy", function(d) { return d.y; })
                .attr("transform", function(d) {
                    return "translate(" + width / 2 + "," + height / 2 + ")";
                });
            text
                .attr("x", function(d) { return d.x; })
                .attr("y", function(d) { return d.y; })
                .attr("transform", function(d) {
                    return "translate(" + width / 2 + "," + height / 2 + ")";
                });
            edgepaths.attr('d', d => 'M ' + d.source.x + ' ' + d.source.y + ' L ' + d.target.x + ' ' + d.target.y);
        }
    });
}

function drawCause(index) {

    console.log("index =", i);

    headContext = "Cause Tree of SDG " + sdgTarget;
    var h3 = document.createElement('h3');
    h3.innerHTML = headContext;
    head.appendChild(h3);

    var svg = d3.selectAll(".container").append("svg")
        .attr("width", 1100)
        .attr("height", 800);

    svg.append('defs')
        .append('marker')
        .attr('id', "arrow0")
        .attr('viewBox', '-0 -5 10 10')
        .attr('refX', 23)
        .attr('refY', 0)
        .attr('orient', 'auto')
        .attr('markerWidth', 10)
        .attr('markerHeight', 10)
        .attr('xoverflow', 'visible')
        .append('svg:path')
        .attr('d', 'M 0,-5 L 10 ,0 L 0,5')
        .attr('fill', colorLink(0))
        .style('stroke', 'none');

    svg.append('defs')
        .append('marker')
        .attr('id', "arrow1")
        .attr('viewBox', '-0 -5 10 10')
        .attr('refX', 23)
        .attr('refY', 0)
        .attr('orient', 'auto')
        .attr('markerWidth', 10)
        .attr('markerHeight', 10)
        .attr('xoverflow', 'visible')
        .append('svg:path')
        .attr('d', 'M 0,-5 L 10 ,0 L 0,5')
        .attr('fill', colorLink(1))
        .style('stroke', 'none');

    svg.append('defs')
        .append('marker')
        .attr('id', "arrow2")
        .attr('viewBox', '-0 -5 10 10')
        .attr('refX', 23)
        .attr('refY', 0)
        .attr('orient', 'auto')
        .attr('markerWidth', 10)
        .attr('markerHeight', 10)
        .attr('xoverflow', 'visible')
        .append('svg:path')
        .attr('d', 'M 0,-5 L 10 ,0 L 0,5')
        .attr('fill', colorLink(2))
        .style('stroke', 'none');

    d3.json(filename, function(error, graph) {
        if (error) throw error;

        var simulation = d3.forceSimulation()
            .force("link", d3.forceLink().id(function(d) { return d.id; }).distance(100))
            .force("charge", d3.forceManyBody())
            .force("center", d3.forceCenter(graph.factors_cause[index].nodes[0].x, graph.factors_cause[index].nodes[0].y))
            .force("attraceForce", d3.forceManyBody().strength(-250))
            .alphaMin(1);

        var link = svg.append("g")
            .attr("class", "links")
            .selectAll("line")
            .data(graph.factors_cause[index].links)
            .enter().append("line")
            .attr('marker-end', function(d) { return "url(#arrow" + d.relation + ")"; })
            .style("stroke", function(d) { return colorLink(d.relation); });

        var node = svg.append("g")
            .attr("class", "nodes")
            .selectAll("circle")
            .data(graph.factors_cause[index].nodes)
            .enter().append("circle")
            .attr("r", 13)
            .attr("fill", "#fff")
            .style("stroke-width", 2)
            .style("stroke", function(d) { return color(d.group + 1); });

        // This is the label for each node
        var text = svg.append("g").selectAll("text")
            .data(graph.factors_cause[index].nodes)
            .enter().append("text")
            .attr("dx", 0)
            .attr("dy", 3)
            .attr("font-size", "10px")
            .text(function(d) { return d.id; })
            .attr("text-anchor", "middle");

        node.append("title")
            .text(function(d) { return d.id; });

        simulation
            .nodes(graph.factors_cause[index].nodes)
            .on("tick", ticked);

        simulation
            .force("link")
            .links(graph.factors_cause[index].links);

        function ticked() {
            graph.factors_cause[index].nodes[0].fx = 0;
            graph.factors_cause[index].nodes[0].fy = 0;

            link
                .attr("x1", function(d) { return d.source.x; })
                .attr("y1", function(d) { return d.source.y; })
                .attr("x2", function(d) { return d.target.x; })
                .attr("y2", function(d) { return d.target.y; })
                .attr("transform", function(d) {
                    return "translate(" + width / 2 + "," + height / 2 + ")";
                });

            node
                .attr("cx", function(d) { return d.x; })
                .attr("cy", function(d) { return d.y; })
                .attr("transform", function(d) {
                    return "translate(" + width / 2 + "," + height / 2 + ")";
                });
            text
                .attr("x", function(d) { return d.x; })
                .attr("y", function(d) { return d.y; })
                .attr("transform", function(d) {
                    return "translate(" + width / 2 + "," + height / 2 + ")";
                });
        }
    });
}