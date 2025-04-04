<h2>🧠 Run Local LLMs in Python with Ollama + Mistral</h2>

<p>
  <strong>Ollama</strong> is a powerful open-source platform that allows you to run large language models (LLMs) <strong>locally on your machine</strong> — with zero API keys, no cloud dependencies, and complete privacy.
</p>

<p>
  It's perfect for developers, researchers, and data scientists who want to experiment with models like <code>mistral</code>, <code>llama2</code>, <code>codellama</code>, <code>gemma</code> and many more.
</p>

<p>
  👉 Explore the full model library here: <a href="https://ollama.com/library" target="_blank">https://ollama.com/library</a>
</p>

<h3>🚀 Quick Python Example:</h3>

<pre>
<code>
import ollama

client = ollama.Client()
model = "Mistral:latest"
prompt = "enlist the genes involved in the cancer"

response = client.generate(model=model, prompt=prompt)
print("Response from Ollama:")
print(response.response)
</code>
</pre>

<h3>🔧 Benefits of Using Ollama</h3>
<ul>
  <li>🖥️ <strong>Runs entirely offline</strong> — after initial download</li>
  <li>🔒 <strong>Secure and private</strong> — no data leaves your machine</li>
  <li>🧬 <strong>Ideal for research & bioinformatics</strong></li>
  <li>📦 <strong>Simple integration</strong> with <code>pip install ollama</code></li>
  <li>⚡ <strong>Fast inference</strong> with GPU or CPU</li>
  <li>🧠 Supports a wide variety of open models: <a href="https://ollama.com/library" target="_blank">View Library</a></li>
</ul>

<h3>🔌 Get Started:</h3>
<ol>
  <li>Install Ollama 👉 <a href="https://ollama.com/download">https://ollama.com/download</a></li>
  <li>Run a model: <code>ollama run mistral</code></li>
  <li>Install Python bindings: <code>pip install ollama</code></li>
  <li>Run the code above and get local AI responses instantly!</li>
</ol>

<p><em>Build offline AI tools, bioinformatics workflows, or personal coding copilots — all powered by Ollama.</em></p>
