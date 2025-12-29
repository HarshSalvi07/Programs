new Chart(document.getElementById('xpLineChart'), {
    type: 'line',
    data: {
        labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        datasets: [{
            label: 'XP Earned',
            data: [40, 70, 60, 20, 80, 50, 90],
            fill: true,
            borderColor: '#3b82f6',
            backgroundColor: 'rgba(59,130,246,0.2)',
            tension: 0.4
        }]
    }
});