document.getElementById('analyzeForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const form = e.target;
    const formData = new FormData(form);

    const res = await fetch('/analyze', {
        method: 'POST',
        body: formData
    });

    const data = await res.json();
    const resultDiv = document.getElementById('result');
    resultDiv.textContent = data.response;
    resultDiv.classList.remove('hidden');
    // document.getElementById('result').textContent = data.response;
});
