/*var endpoint = '/api';

$.ajax({
	method: "GET",
	url: endpoint,
	success: function (data) {
		console.log(data);
	},
	error: function (error_data) {
		console.log(error_data);
	}
})*/

JSC.Chart('chart', {
	debug: true,
	legend_position: 'bottom right',
	type: 'area spline',
	defaultSeries: { shape_opacity: 0.5 },
	xAxis: {
		crosshair_enabled: true,
		scale: { type: 'time' }
	},
	title_label_text: 'Number of trucks',
	title_label_color: "orange",
	//yAxis: { formatString: 'c' }, 
	yAxis_label_color: "#FF0000",
	series: [
		{
			name: 'Truck entered',
			points: [
				['1/1/2020', 1005],
				['2/1/2020', 3202],
				['3/1/2020', 1345],
				['4/1/2020', 2341],
				['5/1/2020', 1440],
				['6/1/2020', 1780]
			]
		},
		{
			name: 'Truck Leave ',
			points: [
				['1/1/2020', 2698],
				['2/1/2020', 2795],
				['3/1/2020', 1954],
				['4/1/2020', 2702],
				['5/1/2020', 1230],
				['6/1/2020', 1110]
			]
		}
	]
});
