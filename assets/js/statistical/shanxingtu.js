function shanxingtu(result) {
    function www() {
                    var res=[];
                    var num0=0;num1=0;
                    for(var i=0;i<result.length;i++){
                        if(result[i].label==0)
                            num0++;
                        if(result[i].label==1||result[i].label==2)
                            num1++;
                    }
                    res.push(num0);
                    res.push(num1);
                     return res;
                    }
    var a=www();
    var myChart = echarts.init(document.querySelector(".col-md-6 .card "));
		myChart.setOption({
            title: {
                text: '业务/恶意流量占比',
                left: "17px",
                top: "15px",
                textStyle: {
                    fontStyle: "normal",
                    fontWeight: "lighter",
                    fontSize: "20",
                    fontFamily: 'Microsoft YaHei'
                }
            },
            tooltip: {
                trigger: 'item',
                formatter: '{b} : {c} ({d}%)',
                backgroundColor: 'rgba(219,89,29,0.5)',
                borderColor: 'black',
                borderWidth: "1.2"
            },
            legend: {
                left: '17px',
                bottom: '15px',
                textStyle: {
                    fontSize: 18
                },
                data: ['业务流量', '恶意流量']
            },
            series: [{
                    type: 'pie',
                    radius: '60%',
                    center: ['50%', '55%'],
                    selectedMode: 'single',
                    label: {
                        fontSize: 18
                    },
                    data: [
                {value: a[0], name: '业务流量',itemStyle:{color:'#00BFFF'} },//替换成数据库数据
                {value: a[1], name: '恶意流量',itemStyle:{color:'#FF8C00'}}
            ],
                    emphasis: {
                        itemStyle: {
                            shadowBlur: 10000,
                            shadowOffsetX: 0,
                            shadowColor: 'rgba(0, 0, 0, 0)'
                        }
                    }
                    }]
                });
		//加载数据到option
}
