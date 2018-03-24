function optionChanged(value){

    sampleMetaData(value);
    pieChart(value);
    // bubbleChart(value);
    

}

function sampleMetaData(value){
    // sample meta data
    url = "/metadata/";
    Plotly.d3.json(url + value, (error, data) => {
        if (error) return console.log(error);

        $cardText = Plotly.d3.select('.card-text');
        // clear the current displayed data
        $cardText.html('');

        // populate table with selected data
        Object.keys(data).forEach((key) => {

            $cardText
                .append('text')
                    .html(key + ": " + data[key])
                .append('br')
                .append('br')
                .append('br')
                .append('br')
                .append('br')
                .append('br')
                .append('br')
                .append('br');
        });
    });
}

function pieChart(value){
    // pie chart data
    url = "/samples/";
    console.log("formated url: ", url + value)
    Plotly.d3.json(url + value, (error, data) => {
        // console.log(JSON.stringify(data));
        if (error) return console.log(error);

        Plotly.d3.json('/otu', (e,d) => {
          if (e) return console.log(e);

            console.log("d is: " + d)
            console.log("data is: " + data)

            data=data[0][0]

          var labelIndex = data.otu_id.slice(0,10);

          var trace1 = {
            values: data.sample_values.slice(0,10),
            labels: data.otu_id.slice(0,10),
            marker: {colors: ['rgba(10, 84, 0, .5)', 'rgba(12, 97, 0, .5)', 'rgba(13, 113, 0, .5)', 'rgba(14, 127, 0, .5)', 'rgba(110, 154, 22, .5)', 'rgba(170, 202, 42, .5)', 'rgba(202, 209, 95, .5)', 'rgba(210, 206, 145, .5)', 'rgba(232, 226, 202, .5)', 'rgba(245, 240, 222, .5)']},
            hole: .4,
            type: 'pie',
            text: labelIndex.map( x => d[x]),
            textinfo: 'percent',
            hoverinfo: 'label+text+value'
          };

          var plotData = [trace1];

          var layout = {
            title: value + "'s Top 10 OTU Microbiomes"
          };
          console.log("created pie chart!")


          return Plotly.newPlot("pie", plotData, layout);
        });
    });
}

function bubbleChart(value){
    // bubble chart data
    url = "/samples/";
    Plotly.d3.json(url + value, (error, data) => {
        if (error) return console.log(error);

        Plotly.d3.json("/otu", (e, d) => {
          if (e) return console.log(e);

          data=data[0][0]

          var trace1 = {
              x: data.otu_id,
              y: data.sample_values,
              text: d,
              hoverinfo: "x+y+text",
              mode: "markers",
              marker: {
                  size: data.sample_values,
                  color: data.otu_id
              }
          };

          var plotData = [trace1]

          var layout = {
              title: value  + "'s Operational Taxonimical Unit's (OTU) Volume and Spread",
              showLegend: false
          }


          return Plotly.newPlot("bubble", plotData, layout)
        });
    });
}

