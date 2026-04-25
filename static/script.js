const form = document.getElementById('risk-form');
const result = document.getElementById('result');

form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = new FormData(form);
    const data = {
        attendance: formData.get('attendance'),
        assignments: formData.get('assignments'),
        sleep_hours: formData.get('sleep_hours')
    };

    const response = await fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });

    const json = await response.json();
    result.textContent = `Predicted Academic Risk Score: ${json.risk_score}%`;
});
