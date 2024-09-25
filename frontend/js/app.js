document.getElementById('analyzeButton').addEventListener('click', function() {
    const textInput = document.getElementById('textInput').value;
    const aspectInput = document.getElementById('aspectInput').value;

    if (textInput === "" || aspectInput === "") {
        alert("Please enter both text and aspect.");
        return;
    }

    const data = {
        text: textInput,
        aspect: aspectInput
    };

    fetch('http://localhost:5000/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('responseSection').style.display = 'block';
        document.getElementById('resultText').textContent = `The tone is: ${data.result}`;
    })
    .catch(error => console.error('Error:', error));
});
