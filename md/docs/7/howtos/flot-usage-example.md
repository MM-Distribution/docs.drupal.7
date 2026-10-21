---
title: "Flot Usage Example"
source_url: "https://www.drupal.org/docs/7/howtos/flot-usage-example"
page_type: page
last_updated: "Last updated on 25 January 2018"
published: "2009-02-28T04:56:53+00:00"
modified: "2018-01-25T23:57:10+00:00"
breadcrumb: ["Drupal 7", "Site building and development HowTos for Drupal 7"]
fetched: "2026-10-21T08:04:39Z"
raw: "raw/docs/7/howtos/flot-usage-example.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Flot Usage Example

It took me a little while to figure out how to use Flot (<http://drupal.org/project/flot>) with Drupal. I post the following example to make it easier for others interested in using the Flot API with Drupal. The following code produces the sample graph displayed at <http://people.iola.dk/olau/flot/examples/basic.html> in a Drupal page. The Flot module needs to be installed first, obviously. I hope this is helpful.

``` php
<?php   
theme_flot_graph('placeholder');
?>

<div id="placeholder" style="width:600px;height:300px;"></div>

<script id="source" language="javascript" type="text/javascript">
$(function () {

    var d2 = [[0, 3], [4, 8], [8, 5], [9, 13]];

    // a null signifies separate line segments
    var d3 = [[0, 12], [7, 12], null, [7, 2.5], [12, 2.5]];
    
    $.plot($("#placeholder"), [ d2, d3 ]);
});
</script>
```

------------------------------------------------------------------------

This next example uses PHP to create the Flot Chart and JS for hover tooltip and custom CSS for the legend.  
[![](/files/graph1_thumb.png)](http://drupal.org/files/graph1_0.png)  
It uses Drupal 7 and the newest Flot Module and Library (2012/05/02).  
The data is acquired from a custom node.  
You can copy and pasted it into a page's body after enabling PHP input.  
This code was from a Brazillian intranet, so some texts are in PT.

``` php
<?php
print("<p>Mova o mouse sobre os pontos do gráfico abaixo para obter informações referentes à produtividade.</br>".
"Faça uma seleção no gráfico ou sua miniatura, clicando e arrastando com o mouse para dar zoom em uma região do gráfico.</p>"
);

    $query = new EntityFieldQuery();
    $query->entityCondition('entity_type', 'node')
            ->entityCondition('bundle', 'produtividade')
            ->propertyCondition('status', 1);
    $result = $query->execute();

    $js_data;
    $filtered_items;

    if (isset($result['node'])) {
        $news_items_nids = array_keys($result['node']);
        $news_items = entity_load('node', $news_items_nids);

        $data = array();
        $data2 = array();
        

        // Remove unneded data and set date as key.
        foreach ($news_items as $record)
        {
            $filtered_items[strtotime(date("Y-m", $record->field_data['und'][0]['value'])) * 1000] = array(
                "field_receita_liquida" => $record->field_receita_liquida['und'][0]['value'],
                "field_despesa_total" => $record->field_despesa_total['und'][0]['value'],
                "field_classe_1" => $record->field_classe_1['und'][0]['value'],
                "field_classe_2" => $record->field_classe_2['und'][0]['value'],
                "field_classe_3" => $record->field_classe_3['und'][0]['value'],
                "field_classe_4" => $record->field_classe_4['und'][0]['value'],
            );
        }

        foreach ($filtered_items as $key=>$record)
        {
            $data[] = array($key, $record["field_receita_liquida"]);
            $data2[] = array($key, $record["field_despesa_total"]);
        }

        $d1 = new flotData($data);
        $d1->label = 'Receita Bruta';
        $d1->points = new flotPoint(array('radius' => 5));
        $d1->lines = new flotLine(array('fill' => true));
        $d1->color = "#008a00";

        $d2 = new flotData($data2);
        $d2->label = 'Despesas';
        $d2->points = new flotPoint(array('radius' => 5));
        $d2->lines = new flotLine(array('fill' => true));
        $d2->color = "#D6121F";

        $style = new flotStyle();
        $style->xaxis->mode = 'time';
        $style->xaxis->tickSize = array(1, "month");
        $style->yaxis->ticks = 15;
        $style->grid->labelMargin = 5;
        $style->legend->position = "ne";
        
        // Configure graph
        $produtividade_data = array(
            'element' => array(
                'id' => 'flot-produtividade',
                'class' => 'flot-produtividade',
                'style' => 'width:940px;height:300px'
            ),
            'data' => array($d1, $d2),
            'options' => $style,
            'legend' => TRUE,
            'zoom' => TRUE,
        );
          
        // Now we show the graph.
        print theme('flot_graph', $produtividade_data);
    }
?>




<script>
jQuery(document).ready(function($){
    function showTooltip(x, y, contents) {
        $('<div id="tooltip">' + contents + '</div>').css( {
            position: 'absolute',
            display: 'none',
            top: y + 5,
            left: x + 5,
            border: '1px solid #E1E1E1',
            padding: '4px',
            'background-color': '#fff',
            'border-radius': '6px',
            'box-shadow': '0 0 10px #999999',
        }).appendTo("body").fadeIn(200);
    }

    var data = <?php echo json_encode($filtered_items); ?>;

    var previousPoint = null;
    $("#flot-view-zoomable-0").bind("plothover", function (event, pos, item) {
        if (item) {
            if (previousPoint != item.dataIndex) {
                previousPoint = item.dataIndex;

                $("#tooltip").remove();

                var produtividade;
                var x = item.datapoint[0].toString();
                var y = item.datapoint[1].toFixed(2);

                produtividade = gep(parseFloat(data[x]["field_receita_liquida"]),
                        parseFloat(data[x]["field_despesa_total"]),
                        parseFloat(data[x]["field_classe_1"]),
                        parseFloat(data[x]["field_classe_2"]),
                        parseFloat(data[x]["field_classe_3"]),
                        parseFloat(data[x]["field_classe_4"]));

                var xpos = item.pageX;

                if (item.pageX > 800)
                {
                    xpos = 700;
                }

                showTooltip(xpos, item.pageY,
                            "<table>" +
                            "    <tbody>" +
                            "       <tr>" +
                            "           <td style=\"color: green;\">Receita Bruta:</td>" +
                            "           <td>R$ " + parseFloat(data[x]["field_receita_liquida"]).toFixed(2) + "</td>" +
                            "       </tr>" +
                            "       <tr>" +
                            "           <td style=\"color: red;\">Despesas:</td>" +
                            "           <td>R$ " + parseFloat(data[x]["field_despesa_total"]).toFixed(2) + "</td>" +
                            "       </tr>" +
                            "       <tr>" +
                            "           <td style=\"color: blue;\">Receita Líquida:</td>" +
                            "           <td>R$ " + (parseFloat(data[x]["field_receita_liquida"]) - parseFloat(data[x]["field_despesa_total"])).toFixed(2) + "</td>" +
                            "       </tr>" +
                            "    </tbody>" +
                            "</table>" +
                            "<table class=\"iba_borders sticky-enabled tableheader-processed sticky-table sticky-header\">" +
                            "   <thead>" +
                            "       <tr>" +
                            "           <th>Classe</th>" +
                            "           <th>Valor Bruto</th>" +
                            "       </tr>" +
                            "   </thead> " +
                            "   <tbody>" +
                            "       <tr class=\"even\">" +
                            "           <td>4</td>" +
                            "           <td>R$ " + produtividade[0].toFixed(2) + "</td>" +
                            "       </tr>" +
                            "       <tr class=\"odd\">" +
                            "           <td>3</td>" +
                            "           <td>R$ " + produtividade[1].toFixed(2) + "</td>" +
                            "       </tr>" +
                            "       <tr class=\"even\">" +
                            "           <td>2</td>" +
                            "           <td>R$ " + produtividade[2].toFixed(2) + "</td>" +
                            "       </tr>" +
                            "       <tr class=\"odd\">" +
                            "           <td>1</td>" +
                            "           <td>R$ " + produtividade[3].toFixed(2) + "</td>" +
                            "       </tr>" +
                            "    </tbody>" +
                            "</table>");
            }
        }
        else {
            $("#tooltip").remove();
            previousPoint = null;
        }
    });

    function gep(receita, despesa, qtd_gp_1, qtd_gp_2, qtd_gp_3, qtd_gp_4) {
        // Many calculation later...

        var result = new Array();
        result[0] = 10;//grupo4;
        result[1] = 20;//grupo3;
        result[2] = 30;//grupo2;
        result[3] = 40;//grupo1;

        return result;
    }



    //CSS
    $(window).bind('load', function() {
        $('div.legend > div').css({
            'width': '108px'
        });

        $('div.legend > table, div.legend > table > tbody').css({
            'width': '105px'
        });

        $('div.legend > div, div.legend > table').css({
            'top': '5px',
            'right': '6px'
        });

        $('div.legend > table').css({
            'margin': '0'
        });

        $('div.legend > table > tbody').css({
            'border': 'none'
        });

        $('div.legend > table > tbody > tr > td').css({
            'padding-left': '0',
            'padding-right': '0'
        });

        $('div.legend > table > tbody > tr > td > div').css({
            'width': '14px'
        });
    });
});
</script>
```
