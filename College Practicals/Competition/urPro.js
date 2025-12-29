new Chart(document.getElementById('skillRadarChart'), {
    type: 'radar',
    data: {
        labels: ['Reading', 'Writing', 'Listening', 'Speaking', 'Grammar'],
        datasets: [{
            label: 'Skill Score',
            data: [80, 65, 70, 55, 75],
            backgroundColor: 'rgba(16,185,129,0.2)',
            borderColor: '#10b981',
            pointBackgroundColor: '#10b981'
        }]
    },
    options: {
        scales: {
            r: {
                suggestedMin: 0,
                suggestedMax: 100
            }
        }
    }
});