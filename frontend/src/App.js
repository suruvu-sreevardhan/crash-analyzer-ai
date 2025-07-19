import React, { useState } from 'react';

function App() {
  const [file, setFile] = useState(null);
  const [timestamp, setTimestamp] = useState('');
  const [result, setResult] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file || !timestamp) {
      alert('Please select a file and enter a timestamp');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);
    formData.append('timestamp', timestamp);

    setLoading(true);

    try {
      const response = await fetch('http://localhost:8000/analyze/', {
        method: 'POST',
        body: formData,
      });

      const data = await response.json();
      setResult(data.summary || 'No summary received.');
    } catch (error) {
      console.error('Error:', error);
      setResult('Error analyzing the log.');
    }

    setLoading(false);
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>Log Analyzer</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <input type="file" onChange={(e) => setFile(e.target.files[0])} />
        </div>
        <div>
          <input
            type="text"
            placeholder="Enter timestamp"
            value={timestamp}
            onChange={(e) => setTimestamp(e.target.value)}
          />
        </div>
        <button type="submit">Analyze</button>
      </form>
      {loading ? <p>Analyzing...</p> : <p><strong>Result:</strong> {result}</p>}
    </div>
  );
}

export default App;
