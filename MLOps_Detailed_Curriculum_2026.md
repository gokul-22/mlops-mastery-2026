# MLOps Mastery 2026: Detailed 6-Month Curriculum

This curriculum is designed to transform you into a senior-level MLOps Engineer, capable of building and scaling "Compound AI Systems."

---

## Phase 1: The Engineering Foundation (Months 1-2)
**Goal:** Master the "Ops" and software engineering required for scalable ML.

### Week 1-2: Advanced Python & AI Engineering
*   **Topics:**
    *   **AsyncIO & FastAPI:** Building high-performance, non-blocking APIs for model serving.
    *   **Pydantic V2:** Strict data validation and settings management.
    *   **Poetry/UV:** Modern dependency management and packaging.
    *   **Design Patterns:** SOLID principles applied to ML pipelines (Factory, Strategy).
*   **Hands-on:** Build a FastAPI microservice that performs image classification using a pre-trained model (PyTorch/TensorFlow).

### Week 3-4: Linux, Bash & Networking
*   **Topics:**
    *   **Shell Scripting:** Automating environment setup and data downloads.
    *   **Process Management:** `systemd`, `cron`, and background tasks.
    *   **Networking for ML:** TCP/IP, DNS, SSL/TLS, and Load Balancing (Nginx/HAProxy).
*   **Hands-on:** Write a Bash script to monitor GPU usage and log it to a central file; set up an Nginx reverse proxy for your FastAPI app.

### Week 5-6: Advanced Containerization (Docker)
*   **Topics:**
    *   **Multi-stage Builds:** Reducing image size from 2GB to 200MB.
    *   **Distroless & Slim Images:** Enhancing security and performance.
    *   **Docker Compose:** Orchestrating multiple services (API + DB + Redis).
    *   **Security Scanning:** Using `Trivy` to find vulnerabilities in images.
*   **Hands-on:** Containerize your FastAPI app using a multi-stage build and optimize it for GPU inference.

### Week 7-8: GitOps & CI/CD
*   **Topics:**
    *   **GitHub Actions:** Writing reusable workflows.
    *   **Automated Testing:** Pytest for ML (testing data shapes, model output ranges).
    *   **Pre-commit Hooks:** Linting (Ruff), formatting (Black), and type checking (MyPy).
*   **Hands-on:** Create a CI/CD pipeline that runs tests, builds a Docker image, and pushes it to a registry on every merge to `main`.

---

## Phase 2: Core MLOps & Infrastructure (Months 3-4)
**Goal:** Automate the model lifecycle from data to deployment.

### Week 9-10: Kubernetes (K8s) for ML
*   **Topics:**
    *   **K8s Primitives:** Pods, Deployments, Services, ConfigMaps, Secrets.
    *   **Helm Charts:** Packaging K8s applications.
    *   **Resource Management:** Setting CPU/Memory/GPU limits and requests.
*   **Hands-on:** Deploy your FastAPI app to a local Kubernetes cluster (Minikube or Kind) using a Helm chart.

### Week 11-12: Data Versioning & Feature Stores
*   **Topics:**
    *   **DVC (Data Version Control):** Managing large datasets in S3/GCS.
    *   **LakeFS:** Git-like operations for your data lake.
    *   **Feast:** Setting up an online/offline feature store.
*   **Hands-on:** Set up a DVC pipeline that versions a 10GB dataset and links it to specific model training runs.

### Week 13-14: Experiment Tracking & Model Registry
*   **Topics:**
    *   **MLflow 3.x:** Logging parameters, metrics, and models.
    *   **Weights & Biases:** Visualizing training progress and system metrics.
    *   **Model Lineage:** Tracking which data and code produced which model.
*   **Hands-on:** Train a model (XGBoost/PyTorch) and log all metadata to MLflow; promote the best model to "Production" in the registry.

### Week 15-16: Workflow Orchestration
*   **Topics:**
    *   **Prefect / Dagster:** Building dynamic, code-as-data pipelines.
    *   **Event-Driven ML:** Triggering retraining based on data drift or new data arrival.
*   **Hands-on:** Build a Prefect flow that: (1) Downloads data, (2) Preprocesses it, (3) Trains a model, and (4) Updates the model registry.

---

## Phase 3: Advanced Serving & LLMOps (Months 5-6)
**Goal:** Mastering LLMs, RAG, and Autonomous Agents.

### Week 17-18: High-Performance Model Serving
*   **Topics:**
    *   **BentoML:** Unified framework for building AI applications.
    *   **Ray Serve:** Distributed inference for multi-model graphs.
    *   **vLLM / TGI:** High-throughput LLM serving (Continuous batching, PagedAttention).
*   **Hands-on:** Deploy a Llama-3 or Phi-4 model using vLLM and benchmark its tokens-per-second.

### Week 19-20: RAG & Vector Databases
*   **Topics:**
    *   **Vector DBs:** Qdrant, Weaviate, or Pinecone (indexing strategies).
    *   **Retrieval Strategies:** Semantic search, Hybrid search, Reranking.
    *   **LangChain / LlamaIndex:** Building complex RAG pipelines.
*   **Hands-on:** Build a "Knowledge Base" API that indexes your company's documentation and answers questions using RAG.

### Week 21-22: LLM Evaluation & Observability
*   **Topics:**
    *   **Arize Phoenix / LangSmith:** Tracing LLM calls and identifying bottlenecks.
    *   **Evaluation Frameworks:** RAGAS (Faithfulness, Relevancy) and G-Eval.
    *   **Semantic Drift:** Monitoring when the "meaning" of user queries changes.
*   **Hands-on:** Implement automated evaluation for your RAG pipeline and log "hallucination" metrics to a dashboard.

### Week 23-24: AgentOps & Autonomous Systems
*   **Topics:**
    *   **ReAct & Tool Use:** Teaching LLMs to use external tools (APIs, SQL).
    *   **State Management:** Managing long-running agent conversations.
    *   **Guardrails:** Using NeMo Guardrails or Guardrails AI for safety and PII protection.
*   **Hands-on:** Build an autonomous SQL Agent that can query a database, summarize the results, and check its own answers for accuracy.

---

## Capstone Project (Final 2 Weeks)
**The "Self-Healing AI System"**
*   **Requirements:**
    1.  A RAG-based API deployed on Kubernetes.
    2.  Automated retraining triggered by drift detection (Evidently AI).
    3.  Full observability (MLflow for training, Arize for LLM traces).
    4.  CI/CD pipeline with automated evaluation tests.
    5.  A public-facing Grafana dashboard showing both system health and AI quality.
