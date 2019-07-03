
    var width = $(".graph").width()   //comma!!!!
    var height = $(".graph").height();



    var nodes = {{ nodes|safe }}; //it works this way
    var links = {{ links|safe }};
    var articles = {{ articles|safe }}

    function loadHeadlines() {
            for(var i in articles){
                $(".accord1 ul").append('<li><p>'+ articles[i] + '</p><div class="accord-content">' + nodes[i]['label'] + '</div></li>');
            }
        }
    loadHeadlines();


    $(".accord-content").hide();
    $('.accord1 li p').click(function () {
            $(this).next(".accord-content").slideToggle();
            $(this).closest("li").siblings().find('.accord-content').slideUp();

        });















































      var svg = d3.select(".graph").append("svg")
      .attr("width", width)
      .attr("height", height);


      var linkForce = d3
      .forceLink()
      .id(function (link) { return link.id })
      .strength(function (link) { return 0.125});


      const forceX = d3.forceX(width / 2).strength(0.05);
      const forceY = d3.forceY(height / 2).strength(0.06);


      var simulation = d3
      .forceSimulation()
      .force('link', linkForce)
      .force('charge', d3.forceManyBody().strength(-40))
      .force('center', d3.forceCenter(width / 2, height / 2))
      .force('x', forceX)
      .force('y', forceY);


      var dragDrop = d3.drag().on('start', function (node) {
      node.fx = node.x
      node.fy = node.y
      }).on('drag', function (node) {
      simulation.alphaTarget(0.7).restart()
      node.fx = d3.event.x
      node.fy = d3.event.y
      }).on('end', function (node) {
      if (!d3.event.active) {
      simulation.alphaTarget(0)
      }
      node.fx = null
      node.fy = null
      })

      function getNeighbors(node) {
      return links.reduce(function (neighbors, link) {
      if (link.target.id === node.id) {
      neighbors.push(link.source.id)
      } else if (link.source.id === node.id) {
      neighbors.push(link.target.id)
      }
      return neighbors
      },
      [node.id]
      )
      }

      function getNodeColor(node, neighbors) {
      if (Array.isArray(neighbors) && neighbors.indexOf(node.id) > -1) {
      return node.level === 1 ? 'black': 'green'
      }

      return node.level === 1 ? 'red' : 'gray'
      }

      function isNeighborLink(node, link) {
      return link.target.id === node.id || link.source.id === node.id
      }

      function selectNode(selectedNode) {
      var neighbors = getNeighbors(selectedNode)

      // we modify the styles to highlight selected nodes
      nodeElements.attr('fill', function (node) { return getNodeColor(node, neighbors) })
      textElements.attr('fill', function (node) { return getTextColor(node, neighbors) })
      linkElements.attr('stroke', function (link) { return getLinkColor(selectedNode, link) })
      }

      function getLinkColor(node, link) {
      return isNeighborLink(node, link) ? 'green' : '#d8d9de'
      }

      function getTextColor(node, neighbors) {
      return Array.isArray(neighbors) && neighbors.indexOf(node.id) > -1 ? 'white' : 'black'
      }

      var nodeElements = svg.append("g")
      .attr("class", "nodes")
      .selectAll("circle")
      .data(nodes)
      .enter().append("circle")
      .attr("r", 8)
      .attr("fill", getNodeColor)
      .call(dragDrop)
      .on('click',function(d){
      selectNode(d);
      console.log(d.id);
      })
      .style("opacity", 1)
      .style('stroke' , 'white');

      var linkElements = svg.append("g")
      .attr("class", "links")
      .selectAll("line")
      .data(links)
      .enter().append("line")
      .attr("stroke-width", 0.6)
      .style("opacity", 0.4)
      .attr("stroke", "#d8d9de");

      var textElements = svg.append("g")
      .attr("class", "texts")
      .selectAll("text")
      .data(nodes)
      .enter().append("text")
      .text(function (node) {
      return node.label
      })
      .on('click',function(d){
      selectNode(d);
      console.log(d.id);
      })
      .attr("font-size", 11.5)
      .attr("font-family", "courier")
      .attr("dx", 15)
      .attr("dy", 4);



      simulation.nodes(nodes).on('tick', () => {
      nodeElements
      .attr('cx', function (node) { return node.x })
      .attr('cy', function (node) { return node.y })
      textElements
      .attr('x', function (node) { return node.x })
      .attr('y', function (node) { return node.y })
      linkElements
      .attr('x1', function (link) { return link.source.x })
      .attr('y1', function (link) { return link.source.y })
      .attr('x2', function (link) { return link.target.x })
      .attr('y2', function (link) { return link.target.y })
      });

      simulation.force("link").links(links);