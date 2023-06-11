$(function () {
    // 请求数据
    $.ajax({
        type: 'get',
        url: '/system/get_echart_data',
        dataType: 'json',
        success: function (returnData) {
            echarts_1(returnData);
            echarts_2(returnData);
            echarts_3(returnData);
            echarts_4(returnData);
            echarts_5(returnData);
            echarts_6(returnData);
        }
    });

    function map(data) {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('map_1'));
        // var data = data['map']['data'];
        var option = {
            xAxis: {
                type: 'category',
                data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
            },
            yAxis: {
                type: 'value'
            },
            series: [
                {
                    data: [150, 230, 224, 218, 135, 147, 260],
                    type: 'line'
                }
            ]
        };


        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }

    function echarts_1(data) {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('echart1'));

        option = {
            // backgroundColor: "#0f375f",
            tooltip: {
                trigger: "axis",
                axisPointer: {
                    type: 'cross',
                    label: {
                        backgroundColor: '#6a7985'
                    }
                }
            },
            grid: {
                left: '0',
                right: '4%',
                bottom: '0',
                top: '8%',
                containLabel: true
            },

            legend: {

                top: "2%",
                right: '10',
                textStyle: {
                    color: "rgba(253,253,255,0.5)",
                    fontSize: "12"
                },

            },

            xAxis: {
                name: "类别",
                type: 'category',

                data: data['echart_1']['x_data'],

                axisLine: {
                    show: true, //隐藏X轴轴线
                    lineStyle: {
                        color: '#26D9FF',
                        width: 2
                    }
                },
                axisTick: {
                    show: true //隐藏X轴刻度
                },
                axisLabel: {
                    show: true,
                    textStyle: {
                        color: "rgba(113,204,161,0.6)", //X轴文字颜色
                        fontSize: 12
                    },
                    interval: 0,
                    rotate: 30
                },

            },
            yAxis: [{
                color: "rgba(255,255,255,.6)",
                type: "value",
                name: "",
                interval: 100,
                nameTextStyle: {
                    color: "#ebf8ac",
                    fontSize: 16
                },
                splitLine: {
                    show: false
                },
                axisTick: {
                    show: true
                },
                axisLine: {
                    show: true,
                    lineStyle: {
                        color: '#26D9FF',
                        width: 2
                    }
                },
                axisLabel: {
                    show: true,
                    textStyle: {
                        color: "rgba(250,250,250,0.6)",
                        fontSize: 16
                    }
                },

            },
                {
                    show: false

                }
            ],
            series: [
                {
                    name: "发行数量",
                    type: "line",
                    yAxisIndex: 1, //使用的 y 轴的 index，在单个图表实例中存在多个 y轴的时候有用
                    smooth: true, //平滑曲线显示
                    showAllSymbol: true, //显示所有图形。
                    symbol: "circle", //标记的图形为实心圆
                    symbolSize: 12, //标记的大小
                    itemStyle: {
                        //折线拐点标志的样式
                        color: "#eb2bd1",
                        borderColor: "#3D7EEB",
                        width: 2,
                        shadowColor: "#3D7EEB",
                        shadowBlur: 4
                    },
                    lineStyle: {
                        color: "#c1ff38",
                        width: 2,
                        shadowColor: "#3D7EEB",
                        shadowBlur: 4
                    },
                    areaStyle: {
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                            offset: 0,
                            color: "rgba(61,126,235, 0.5)"
                        },
                            {
                                offset: 1,
                                color: "rgba(61,126,235, 0)"
                            }
                        ])
                    },
                    data: data['echart_1']['y_data'],

                },
                {
                    name: "发行数量",
                    type: "bar",
                    barWidth: 15,
                    tooltip: {
                        show: false
                    },
                    itemStyle: {
                        normal: {
                            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                offset: 0,
                                color: "#d427ff"
                            },
                                {
                                    offset: 1,
                                    color: "rgba(61,126,235, 0)"
                                }
                            ]),
                            borderColor: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                offset: 0,
                                color: "rgba(160,196,225, 1)"
                            },
                                {
                                    offset: 1,
                                    color: "rgba(61,126,235, 1)"
                                }
                            ]),
                            borderWidth: 2
                        }
                    },
                    data: data['echart_1']['y_data'],
                }

            ]
        };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }

    function echarts_2(data) {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('echart2'));

        option = {
            // backgroundColor:"#0f375f",
            grid: {
                left: '3%',
                right: '4%',
                bottom: '3%',
                top: '8%',

                containLabel: true
            },
            legend: {
                top: "2%",
                right: '10',
                textStyle: {
                    color: "rgba(253,253,255,0.5)",
                    fontSize: "12"
                },

            },
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'cross',
                }
            },

            xAxis: {
                type: 'category',
                // boundaryGap: false,
                data: data['echart_2']['x_data'],
                triggerEvent: true,
                splitLine: {
                    show: false
                },
                axisLine: {
                    show: true,
                    lineStyle: {
                        width: 2,
                        color: 'rgba(255,255,255,.6)'
                    }
                },
                axisTick: {
                    show: false
                },
                axisLabel: {
                    textStyle: {
                        color: "rgba(250,250,250,0.6)", //X轴文字颜色
                        fontSize: 12
                    },
                    color: '#fff',
                    fontSize: 16,
                    fontWeight: 'bold',
                    textShadowColor: '#000',
                    textShadowOffsetY: 2,
                    interval: 0,
                    rotate: 30
                }
            },
            yAxis: {
                name: '',
                nameTextStyle: {
                    color: '#fff',
                    fontSize: 16,
                    textShadowColor: '#000',
                    textShadowOffsetY: 2
                },
                type: 'value',
                splitLine: {
                    show: true,
                    lineStyle: {
                        color: 'rgba(255,255,255,.2)'
                    }
                },
                axisLine: {
                    show: true,
                    lineStyle: {
                        width: 2,
                        color: 'rgba(255,255,255,.6)'
                    }
                },
                axisTick: {
                    show: true
                },
                axisLabel: {
                    textStyle: {
                        color: "rgba(250,250,250,0.6)", //X轴文字颜色
                        fontSize: 16
                    },
                    color: '#fff',
                    fontSize: 16,
                    textShadowColor: '#000',
                    textShadowOffsetY: 2
                }
            },
            series: [{
                data: data['echart_2']['y_data'],
                type: 'line',
                symbol: 'none',
                symbolSize: 12,
                color: '#0b1eff',
                lineStyle: {
                    color: "#d0e3f2"
                },
                label: {
                    show: false,
                    position: 'top',
                    textStyle: {
                        color: '#FEC201',
                        fontSize: 18,
                        fontWeight: 'bold'
                    }
                },
                areaStyle: {
                    color: 'rgba(1,98,133,0.6)'
                }
            },
                {
                    type: 'bar',
                    animation: false,
                    barWidth: 3,
                    hoverAnimation: false,
                    data: data,
                    tooltip: {
                        show: false
                    },
                    itemStyle: {
                        normal: {
                            color: {
                                type: 'linear',
                                x: 0,
                                y: 0,
                                x2: 0,
                                y2: 1,
                                colorStops: [{
                                    offset: 0,
                                    color: '#91EAF2' // 0% 处的颜色
                                }, {
                                    offset: 1,
                                    color: '#074863' // 100% 处的颜色
                                }],
                                globalCoord: false // 缺省为 false
                            },
                            label: {
                                show: true
                            }
                        }
                    }
                }
            ]
        }

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }

    function echarts_3(data) {
        var optionFour = {
            tooltip: {
                show: true
            },
            series: [{
                 type: 'wordCloud',
                sizeRange: [10, 50],//文字范围
                rotationRange: [-45, 90],
                rotationStep: 45,
                textRotation: [0, 45, 90, -45],
                shape: 'circle',
                textStyle: {
                    normal: {
                        color: function () {//文字颜色的随机色
                            return 'rgb(' + [
                                Math.round(Math.random() * 250),
                                Math.round(Math.random() * 250),
                                Math.round(Math.random() * 250)
                            ].join(',') + ')';
                        }
                    },
                    //悬停上去的字体的阴影设置
                    emphasis: {
                        shadowBlur: 10,
                        shadowColor: '#333'
                    }
                },
                data: data['echart_3']['data'],
            }]
        };
        var myChartFour = echarts.init(document.getElementById('echart3'));
        myChartFour.setOption(optionFour);
    }

    function echarts_4(data) {
        var myChart = echarts.init(document.getElementById('echart4'));
        option = {
            toolbox: {
                show: true,
                feature: {}
            },
            series: [
                {
                    name: '发行数量',
                    type: 'pie',
                    radius: [20, 70],
                    center: ['50%', '50%'],
                    roseType: 'area',
                    itemStyle: {
                        borderRadius: 8,
                        emphasis: {
                            shadowBlur: 10,
                            shadowOffsetX: 0,
                            shadowColor: 'rgba(0, 0, 0, 0.5)'
                        },
                        normal: {
                            color: function (params) {
                                //自定义颜色
                                var colorList = [
                                    '#C1232B', '#B5C334', '#FCCE10', '#E87C25', '#27727B',
                                    '#FE8463', '#9BCA63', '#FAD860', '#F3A43B', '#60C0DD',
                                    '#D7504B', '#C6E579', '#F4E001', '#F0805A', '#26C0C0'
                                ];
                                return colorList[params.dataIndex]
                            }
                        }
                    },
                    data: data['echart_4']['data'],
                }
            ]
        };
        myChart.setOption(option);
        // window.addEventListener("resize", function () {
        //     myChart.resize();
        // });
    }

    function echarts_5(data) {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('echart5'));

        option = {
            // backgroundColor: '#061326',
            title: {
                x: "center",
                y: "6%",
                textStyle: {
                    color: '#FFF',
                    fontSize: 30
                }
            },
            grid: {
                "top": "20%",
                "left": "5%",
                "bottom": "5%",
                "right": "5%",
                "containLabel": true
            },
            tooltip: {
                show: true,
            },
            animation: false,
            "xAxis": [{
                "type": "category",
                "data": data['echart_5']['x_data'],
                "axisTick": {
                    "alignWithLabel": true
                },
                "nameTextStyle": {
                    "color": "#FEC201"
                },
                "axisLine": {
                    show: false,
                    "lineStyle": {
                        "color": "#82b0ec"
                    }
                },
                "axisLabel": {
                    "textStyle": {
                        "color": "rgba(113,204,161,0.6"
                    },
                    margin: 30,
                    interval: 0,
                    rotate: 40
                }
            }],
            "yAxis": [{
                show: true,
                "type": "value",
                "axisLabel": {
                    "textStyle": {
                        "color": "rgba(113,204,161,0.6"
                    },
                },
                "splitLine": {
                    "lineStyle": {
                        "color": "#0c2c5a"
                    }
                },
                "axisLine": {
                    "show": false
                }
            }],
            "series": [{
                "name": "评分",
                type: 'pictorialBar',
                symbolSize: [40, 10],
                symbolOffset: [0, -6],
                symbolPosition: 'end',
                z: 12,
                "barWidth": "0",
                "label": {
                    "normal": {
                        "show": true,
                        "position": "top",
                        // "formatter": "{c}%"
                        fontSize: 25,
                        fontWeight: 'bold',
                        color: '#ffeb7b'
                    }
                },
                color: "#2DB1EF",
                data: data['echart_5']['y_data'],
            },
                {
                    name: '',
                    type: 'pictorialBar',
                    symbolSize: [40, 10],
                    symbolOffset: [0, 7],
                    // "barWidth": "20",
                    z: 12,
                    "color": "#2DB1EF",
                    "data": data['echart_5']['y_data'],
                },
                {
                    name: '',
                    type: 'pictorialBar',
                    symbolSize: [50, 15],
                    symbolOffset: [0, 12],
                    z: 10,
                    itemStyle: {
                        normal: {
                            color: 'transparent',
                            borderColor: '#2EA9E5',
                            borderType: 'solid',
                            borderWidth: 1
                        }
                    },
                    data: data['echart_5']['y_data'],
                },
                {
                    name: '',
                    type: 'pictorialBar',
                    symbolSize: [70, 20],
                    symbolOffset: [0, 18],
                    z: 10,
                    itemStyle: {
                        normal: {
                            color: 'transparent',
                            borderColor: '#19465D',
                            borderType: 'solid',
                            borderWidth: 2
                        }
                    },
                    data: data['echart_5']['y_data'],
                },
                {
                    type: 'bar',
                    //silent: true,
                    "barWidth": "40",
                    barGap: '10%', // Make series be overlap
                    barCateGoryGap: '10%',
                    itemStyle: {
                        normal: {
                            color: new echarts.graphic.LinearGradient(0, 0, 0, 0.7, [{
                                offset: 0,
                                color: "#38B2E6"
                            },
                                {
                                    offset: 1,
                                    color: "#0B3147"
                                }
                            ]),
                            opacity: .8
                        },
                    },
                    data: data['echart_5']['y_data'],
                }
            ]
        };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }

    function echarts_6(data) {
        var myChart = echarts.init(document.getElementById('echart6'));
        var option = {
            color: ["#00FFF7FF", "#66FF99", "#FF9966", "#A3E2F4"],
            grid: {
                left: -100,
                top: 50,
                bottom: 10,
                right: 10,
                containLabel: true
            },
            tooltip: {
                trigger: 'item',
                formatter: "{b} : {c} ({d}%)"
            },
            legend: {
                type: "scroll",
                orient: "vartical",
                // x: "right",
                top: "center",
                right: "15",
                bottom: "0%",
                itemWidth: 16,
                itemHeight: 8,
                itemGap: 16,
                textStyle: {
                    color: '#A3E2F4',
                    fontSize: 12,
                    fontWeight: 0
                },
                data: data['echart_6']['x_data']
            },
            polar: {},
            angleAxis: {
                interval: 1,
                type: 'category',
                data: [],
                z: 10,
                axisLine: {
                    show: false,
                    lineStyle: {
                        color: "#0B4A6B",
                        width: 1,
                        type: "solid"
                    },
                },
                axisLabel: {
                    interval: 0,
                    show: true,
                    color: "#0B4A6B",
                    margin: 8,
                    fontSize: 16
                },
            },
            radiusAxis: {
                min: 40,
                max: 120,
                interval: 20,
                axisLine: {
                    show: false,
                    lineStyle: {
                        color: "#0B3E5E",
                        width: 1,
                        type: "solid"
                    },
                },
                axisLabel: {
                    formatter: '{value} %',
                    show: false,
                    padding: [0, 0, 20, 0],
                    color: "#0B3E5E",
                    fontSize: 16
                },
                splitLine: {
                    lineStyle: {
                        color: "#0B3E5E",
                        width: 2,
                        type: "solid"
                    }
                }
            },
            calculable: true,
            series: [{
                type: 'pie',
                radius: ["5%", "10%"],
                hoverAnimation: false,
                labelLine: {
                    normal: {
                        show: false,
                        length: 30,
                        length2: 55
                    },
                    emphasis: {
                        show: false
                    }
                },
                data: [{
                    name: '',
                    value: 0,
                    itemStyle: {
                        normal: {
                            color: "#0B4A6B"
                        }
                    }
                }]
            }, {
                type: 'pie',
                radius: ["90%", "95%"],
                hoverAnimation: false,
                labelLine: {
                    normal: {
                        show: false,
                        length: 30,
                        length2: 55
                    },
                    emphasis: {
                        show: false
                    }
                },
                name: "",
                data: [{
                    name: '',
                    value: 0,
                    itemStyle: {
                        normal: {
                            color: "#0B4A6B"
                        }
                    }
                }]
            }, {
                stack: 'a',
                type: 'pie',
                radius: ['20%', '80%'],
                roseType: 'area',
                zlevel: 10,
                label: {
                    normal: {
                        show: true,
                        formatter: "{c}",
                        textStyle: {
                            fontSize: 12,
                        },
                        position: 'outside'
                    },
                    emphasis: {
                        show: true
                    }
                },
                labelLine: {
                    normal: {
                        show: true,
                        length: 20,
                        length2: 55
                    },
                    emphasis: {
                        show: false
                    }
                },
                data: data['echart_6']['y_data']
            },]
        }

        myChart.setOption(option)
    }
})
;