function zhexiantu1(result) {
    var a0=[],a1=[],a2=[];
    function www(result) {
                    if (result) {
                        for(var i=0;i<result.length;i++){
                           if(result[i].label==0.0)
                               a0.push(result[i].time.split(' ')[1].split(':')[0]);
                           else if(result[i].label==1.0)
                               a1.push(result[i].time.split(' ')[1].split(':')[0]);
                           else if(result[i].label==2.0)
                               a2.push(result[i].time.split(' ')[1].split(':')[0]);
                        }
                    }
                    return a0,a1,a2;
                }
    www(result);
    a0.sort(function(a, b){return a - b});
    a1.sort(function(a, b){return a - b});
    a2.sort(function(a, b){return a - b});
    var a,b;
  function arrayCnt(arr) {
      var newArr = [];
    newArr =[...new Set(arr)];
    var newarr2 = new Array(newArr.length);
  for(var t = 0; t < newarr2.length; t++) {
   newarr2[t] = 0;
  }
  for(var p = 0; p < newArr.length; p++) {
   for(var j = 0; j < arr.length; j++) {
   if(newArr[p] == arr[j]) {
    newarr2[p]++;
   }
   }
  }
  a=newArr;
  b=newarr2;
  }
  arrayCnt(a0);
  var b0=a;
  var c0=b;
  arrayCnt(a1);
  var b1=a;
  var c1=b;
  arrayCnt(a2);
  var b2=a;
  var c2=b;
    var myChart = echarts.init(document.querySelector(".col-md-6 .card .card-body"));
		myChart.setOption({
            title: {
                    text: '各类流量进入量',
                    left:"0px",
                    top:"0px",
                    textStyle:{
                        fontStyle:"normal",
                        fontWeight:"lighter",
                        fontSize:"20",
                        fontFamily : 'Microsoft YaHei'
                    }
            },
			tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'cross',
                    crossStyle:{
                        color :'blue',
                        width:'1'
                    },
                    label: {
                        fontSize:'13',
                    backgroundColor: 'blue'
                     }
                }
            },
			color:['#00BFFF','#DC143C','#FF8C00'],
            legend: {
                left: '5%',
                bottom: '5px',
                textStyle:{
                fontSize:14
            }

        },
            grid: {
                left: '0%',
                right: '12%',
                bottom: '8%',
                containLabel: true
            },
			xAxis: [
        {
            name:'时间/小时',
            type: 'category',
            boundaryGap: false,
            data:b0
        }
    ],
    yAxis: [
        {
            name:'数量',
            type: 'value'
        }
    ],
            series: [
            {
                smooth:true,
                name: '业务流量',
                type: 'line',
                stack: '总量',
                areaStyle: {
                color:'#00BFFF'
                },
                data: c0
            },
            {
                smooth:true,
                name: '网络攻击流量',
                type: 'line',
                stack: '总量',
                areaStyle: {
                    color:	'#DC143C'
                },
                data: c1
            },

            {
                smooth:true,
                name: '恶意软件流量',
                type: 'line',
                stack: '总量',
                areaStyle: {
                    color:'#FF8C00'
                },
                data: c2
            }

            ]
		});
		//加载数据到option
}
