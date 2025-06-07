# MedBot : RAG based medical AI assisstant 

MedBot is an advanced Retrieval-Augmented Generation (RAG) medical chatbot designed to provide inclusive, context-aware, health information to users in India. Built using modern LLM technologies and LangChain, it focuses on accessibility, empathy, and evidence-based insights — while avoiding diagnoses or panic-inducing language.

---

## 🧩 Features

- 🏥 **Medical Context-Aware Chatbot**
- 📚 **Backed by WHO, ICMR, and Authoritative Sources**
- 🧾 **Triage Severity Score (TSS)** for symptom categorization (TSS-1 to TSS-4)
- 🚫 **Rejects Non-Health-Related Questions Gracefully**
- 💬 **Powered by RAG** using Groq/OpenAI + HuggingFace + LangChain
- 🧠 **Embeddings**: Sentence Transformers
- ☁️ **Vector DB**: Pinecone or FAISS
- 🌍 **Deployed on**: *[Heroku/Render/AWS/GCP]*

---

## 🛠️ Tech Stack

| Layer | Tech |
|------|------|
| 🧠 LLM | Groq (llama3-70b-8192) |
| 🔎 RAG Framework | LangChain |
| 📖 Embeddings | HuggingFace Transformers |
| 📦 Vector Store | Pinecone |
| 🧾 Prompting | System + Human templates (ChatPromptTemplate) |
| 🌐 API & Backend | Flask |
| 🖥️ Deployment | [Render / Vercel / AWS] |
| 📂 Storage | Hugging Face Hub / Local / GCS |
| 🌏 Languages | Python |

---


---

## 📌 Future Enhancements

* 🔊 Add Speech-to-Text + Voice Output (Hindi, Tamil, etc.)
* 📡 Real-time querying of public medical APIs (e.g., Medline, WHO)
* 📊 Symptom logs and health timeline tracker
* 🌟 Fine-tune with domain-specific medical data
* 🧪 Add unit tests, CI/CD pipeline, and rate limiting

---

## 💼 Why This Matters

> In a country with 1.4B people and diverse linguistic backgrounds, Niramaya aims to bridge the gap in basic, empathetic medical awareness and triage — not replace doctors, but empower patients with calm, clear, evidence-based support.

---

## 👩‍💻 Author

**Kashish Rajput**
[LinkedIn](https://www.linkedin.com/in/kashishrajputt) | [GitHub](https://github.com/kashishrajputt)

---

## 🛑 Disclaimer

This assistant does not offer medical advice, treatment, or diagnosis. It is not a substitute for a licensed medical professional.

```


