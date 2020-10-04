function zhuxingtu(result) {
    var myChart = echarts.init(document.querySelector(" .col-md-6 .card .card-footer"));
		myChart.setOption({
			title: {
                    text: '各类流量总量',
                    left:"0px",
                    top:"2%",
                    textStyle:{
                        fontStyle:"normal",
                        fontWeight:"lighter",
                        fontSize:"20",
                        fontFamily : 'Microsoft YaHei'
                        }
                    },
            color: ['#3398DB'],
			tooltip: {
                show : true,
                trigger: 'axis',
                axisPointer: {
                type: 'cross',
                crossStyle:{
                    color :'blue',
                    width:'1'
                    },
              label: {
                fontSize:'14',
                backgroundColor: '#BC8F8F'
            }
        }
    },
			legend: {
            show:false
         },
             grid: {
            left: '5%',
            right: '60px',
            bottom: '5%',
            top:'90px',
         containLabel: true
        },
			xAxis: [
            {
            name:'种类',
            nameTextStyle:{
               fontSize:14,
                fontWeight:'lighter'
            },
            type: 'category',
            data: ['业务流量', '网络攻击流量', '恶意软件流量'],
            axisTick: {
                alignWithLabel: true
            }
        }
    ],
			yAxis: [
                {
                name:'数量',
                 nameTextStyle:{
                 fontSize:14,
                 fontWeight:'lighter'
                 },
                type: 'value'
            }
         ],
            series: [
                 {
                    itemStyle:{
                     normal:{
                        color: function (params) {
                    var colorList = ['#00BFFF','#DC143C','#FF8C00'];
                    return colorList[params.dataIndex]
                }
                }
            },
            name: '数量',
            type: 'bar',
            barWidth: '45%',
            data: (function () {
                var res=[];
                var num0=0;num1=0,num2=0;
                for(var i=0;i<result.length;i++){
                    if(result[i].label==0)
                        num0++;
                    if(result[i].label==1)
                        num1++;
                    if(result[i].label==2)
                        num2++;
                }
                res.push(num0);
                res.push(num1);
                res.push(num2);
                return res;
            })()
         }
         ]
		});
}
