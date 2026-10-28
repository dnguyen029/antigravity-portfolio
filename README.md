# David Nguyen — Technical Operations & Agent Management Portfolio

**Systems Integrator | AI Solutions Architect | E-Commerce Entrepreneur**  
Santa Ana, CA | [LinkedIn](https://linkedin.com/in/davidnguyen029) | [GitHub](https://github.com/dnguyen029) | dnguyen029@gmail.com

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Google Antigravity](https://img.shields.io/badge/Antigravity%20SDK-2.0.0-purple.svg)](https://antigravity.google/docs)
[![Google ADK](https://img.shields.io/badge/Google%20ADK-1.15.0-orange.svg)](https://google.github.io/agent-development-kit/)
[![Google Cloud Run](https://img.shields.io/badge/Cloud%20Run-Deployed-blue.svg)](https://cloud.google.com/run)
[![Gemini Models](https://img.shields.io/badge/Google%20GenAI-Gemini%20Flash%20Live-purple.svg)](https://cloud.google.com/vertex-ai)
[![Protocol: MCP](https://img.shields.io/badge/Protocol-Model%20Context%20Protocol-green.svg)](https://modelcontextprotocol.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

A production-grade AI systems portfolio showcasing an end-to-end agentic engineering lifecycle built with **Google Antigravity**:

1. **The Multi-Agent Orchestration SDK**: A development harness built inside Google Antigravity IDE and packaged into a Python SDK to coordinate coding, security audits, and testing with human approval gates.  
   *Live Repository*: **[github.com/dnguyen029/antigravity-sdk](https://github.com/dnguyen029/antigravity-sdk)**
2. **The Voice AI Receptionist**: A live 24/7 customer support phone assistant built using the Google Agents ADK/CLI and deployed to Google Cloud Run to answer calls, track orders, and capture leads in real time.  
   *Live Repository*: **[github.com/dnguyen029/receptionist-template](https://github.com/dnguyen029/receptionist-template)**

---

## System Overview & Operational Impact

| Business Challenge | AI Solution Implemented | Operational Impact |
| :--- | :--- | :--- |
| **Missed After-Hours Inquiries** | Automated voice receptionist answers calls 24/7 with pluggable CRM/Database dispatching. | Captures after-hours leads with automated ticket sync into **Zendesk, HubSpot, Salesforce, Airtable, or Google Sheets**. |
| **High Support Ticket Volume** | Self-service order lookup (WISMO) integrated with **Shopify, Medusa, or custom ERPs**. | Deflects ~70% of repetitive tracking calls; enforces **Two-Factor Verification** to protect customer data. |
| **Unreliable LLM Code Generation** | Multi-agent engineering harness with **Human-in-the-Loop Approval Gates**. | Code modifications require an approved Root Cause Analysis (RCA) and user sign-off before modifying files. |
| **Conversational Latency** | Low-latency audio streaming optimized with a **<40-word turn budget**. | Natural spoken conversation cadence without awkward pauses or robotic monologue. |

---

## System 1 — Multi-Agent Conversational Receptionist

A standalone, decoupled AI receptionist handling inbound customer contacts for headless digital storefronts and commerce backends. The system classifies caller intent in real time and routes to a specialized subagent via the **Agents CLI** and **A2A (Agent-to-Agent)** framework while keeping subagent handoffs seamless to the caller.

* **Live Repository**: [github.com/dnguyen029/receptionist-template](https://github.com/dnguyen029/receptionist-template)

### Architecture & Intent Routing

```mermaid
flowchart TD
    Inbound(["Customer Call / Inbound Message"]) --> Router["Intent Router Agent<br/>Intent Classification & Sentiment Analysis"]
    
    Router -->|"Lead Capture / After Hours"| LeadAgent["Lead Capture Specialist<br/>Pluggable CRM Adapter"]
    Router -->|"Order Tracking / WISMO"| WISMOAgent["WISMO Specialist<br/>Two-Factor 2FA Verification"]
    Router -->|"Store Policies / FAQs"| FAQAgent["FAQ Specialist<br/>Contentful / Sanity.io Knowledge Search"]
    Router -->|"Call Complete"| ExitAgent["Exit Specialist<br/>Structured Session Disconnect"]

    subgraph Integrations ["Pluggable SaaS Integrations"]
        LeadAgent --> CRM[("CRMs & Databases<br/>Zendesk, HubSpot, Sheets, Airtable")]
        WISMOAgent --> Storefront[("Storefront & ERPs<br/>Shopify, Medusa, Custom API")]
        FAQAgent --> CMS[("Knowledge Base<br/>Headless CMS / Vector DB")]
    end
```

### Key Engineering Features

* **Headless Commerce Orchestration** — Decoupled frontend built with **Next.js** interacting with **Medusa** and **Shopify** backends via custom webhook event structures.
* **Two-Factor Record Verification** — Requires two-factor verification (Caller ID + PO/Order Number or ZIP code) before disclosing customer PII over telephony.
* **Low-Latency Spoken Cadence** — Voice prompts apply a **<40-word turn budget** to maintain a concise spoken cadence and reduce TTS rendering latency.
* **Dynamic Headless CMS & Next.js Sync** — Connects the **Next.js** storefront and **Headless CMS** layers via webhooks so product updates and store policies sync across both the website and the voice agent without manual redeploys.
* **Idempotent Dispatch** — Generates session idempotency keys for Zendesk and Google Sheets to prevent duplicate records during network retries.

### Production Deployment

| Property | Value |
| :---- | :---- |
| **Platform** | Google Cloud Run |
| **Service Name** | `receptionist-prod` |
| **Region** | `us-west1` / `us-central1` |
| **Authentication** | Google Default Identity (OIDC) |
| **Runtime** | FastAPI + Uvicorn |

### Webhook Endpoints

| Route | Purpose |
| :---- | :---- |
| `/webhook/write-to-sheets` | Lead capture ➔ Google Sheets + Zendesk API |
| `/webhook/wismo-lookup` | Order status lookup by PO number via backend APIs |
| `/webhook/faq-lookup` | Grounded FAQ answer from headless CMS knowledge base |

---

## System 2 — Governed Multi-Agent Orchestration & Lifecycle Harness

A 6-agent engineering harness featuring programmatic **4-stage lifecycle hooks** (`.agents/hooks.json`) and live documentation grounding designed for structured, auditable development workflows.

* **Live Repository**: [github.com/dnguyen029/antigravity-sdk](https://github.com/dnguyen029/antigravity-sdk)

### Multi-Agent Handoff & Governance Flow

```mermaid
flowchart TD
    Goal(["User Engineering Goal"]) --> PreInv["PreInvocation Hook<br/>Semantic Memory Injection & MCP Hygiene"]
    PreInv --> Orchestrator["Orchestrator Agent<br/>Principal Architect<br/>Plan Authoring & RCA Analysis"]
    Orchestrator <-->|"Live Docs & RCA"| Researcher["Researcher Agent<br/>Context7, Modern Web Guidance & Google Dev Knowledge"]
    
    Orchestrator --> RCAGate{"RCA Gate<br/>Root Cause Verified?"}
    RCAGate -->|"No"| Orchestrator
    RCAGate -->|"Yes"| ApprovalGate["User Approval Gate<br/>Mandatory Human Sign-Off"]
    
    ApprovalGate -->|"Approved + SHA-256 Lock"| Builder["Builder Agent<br/>Lead Developer<br/>Doc-Grounded Code Synthesis"]
    Builder --> PostTool["PostToolUse Hook<br/>Ruff Format, Link Audit & Targeted Pytest"]
    PostTool --> Auditor["Auditor Agent<br/>Security & QA Compliance Audit"]
    Auditor --> SRE["SRE / Admin Agent<br/>Environment Alignment & Runtime Verification"]
    SRE --> Librarian["Librarian Agent & Stop Hook<br/>Walkthrough Generation & Supabase Archival"]
```

### Roles and Responsibilities

| Agent | Role | Decision-Making Authority |
| :---- | :---- | :--- |
| **Orchestrator** | Principal Architect | System architecture, RCA enforcement, task delegation |
| **Researcher** | Diagnostic Investigator | Official documentation grounding (`Context7`, `Google Developer Knowledge`, `Exa`), historical memory lookup |
| **Builder** | Lead Developer | Code synthesis, AST validation, systems integration |
| **Auditor** | Security & Compliance | Security hardening, vulnerability audit, quality gate |
| **Admin / SRE** | Infrastructure Management | Environment alignment, test execution, runtime health |
| **Librarian** | Documentation & Memory | Designated record custodian for project documentation and vector memory archival |

### Governance Framework & Enforced Protocols

| Rule | Policy Mandate |
| :---- | :--- |
| **Diagnose Before Fix (RCA Gate)** | Mandatory root cause analysis before modifying code. Blocks file edits without visible symptoms, technical root cause, and resolution plan. |
| **Plan Approval Gate** | Blocks file modifications and mutating terminal commands until the user approves the implementation plan. |
| **Scoped Memory Write Access** | Write access to long-term vector memory is scoped to the Librarian persona and teardown hook to maintain consistent records. |
| **Plan Immutability Fingerprinting** | Computes a SHA-256 hash of `implementation_plan.md` upon user approval; post-approval edits trigger a re-authorization prompt. |
| **Proactive Documentation Gate** | Requires querying authoritative documentation (`Context7`, `Modern Web Guidance`, or `Google Developer Knowledge`) before modifying code files. |
| **3-Strike Loop & Rollback Guard** | Halts execution after 3 consecutive tool errors and rolls back broken code edits via `git checkout`. |
| **Defensive Directory Barriers** | Security hooks physically block access to protected directories (`.git`, `.venv`, `node_modules`). |
| **Resource Optimization (TOON MCP)** | Compresses verbose JSON payloads to reduce token overhead by 40–60% across multi-turn context windows. |
| **Verified Parameter Standard** | Operates on verified parameters; ambiguity triggers a pause-and-clarify prompt rather than guessing. |

### 4-Stage Lifecycle Hook Architecture (`.agents/hooks.json`)

| Lifecycle Event | Hook Script | Enforcement & Automation |
| :--- | :--- | :--- |
| **`PreInvocation`** | `bundle_pre_invocation.py` | Terminates orphaned MCP background processes (`SIGTERM`), flushes queued offline lessons, and embeds the user prompt (`gemini-embedding-001`, 384-dim) to load relevant matches from Supabase into `.agents/lessons_context.md`. |
| **`PreToolUse`** | `safety_gate.py` | Enforces the 150-step loop ceiling, 3-strike error breaker, SHA-256 plan integrity check, destructive command blocks, BigQuery dry-run checks, and the **Documentation Lookup Gate**. |
| **`PostToolUse`** | `bundle_quality_gate.py` | Runs `ruff format` and `ruff check --fix` on modified Python files, validates Markdown links, and runs matching `test_<module>.py` unit suites. |
| **`Stop`** | `bundle_teardown.py` | Hashes completed `walkthrough.md` artifacts (SHA-256) and archives new lessons to the Supabase REST API (with a local `pending_lessons.json` fallback queue). |

---

## Systems Integration Layer

Seven services and documentation tools support organizational memory, live code grounding, token compression, and research:

| Service | Role |
| :---- | :--- |
| **Context7 MCP** | Live, version-specific documentation and code snippet retrieval for third-party SDKs, frameworks, and libraries prior to code edits. |
| **Google Modern Web Guidance** | Pre-implementation lookup tool for modern HTML/CSS, Core Web Vitals (LCP/INP), accessibility, and baseline browser standards. |
| **Google Developer Knowledge MCP** | Official documentation lookup across Google Cloud (`gcloud`, Cloud Run, BigQuery, IAM), Gemini, ADK, Dialogflow CX, and Antigravity. |
| **TOON MCP Server** | Custom Model Context Protocol server executing row-based token payload compression for high-frequency tool outputs. |
| **Supabase Vector Vault** | Secured corporate memory bank storing embeddings and lessons learned across sessions. |
| **Supermemory** | Semantic knowledge retrieval for cross-session project context. |
| **Exa Search** | High-authority web research and documentation scraping engine. |

### 📊 TOON Protocol Empirical Compression Benchmarks

To reduce context window consumption and inference costs during multi-turn agent tool execution, the custom **TOON MCP Server** extracts repetitive dictionary schemas into pipe-delimited matrix vectors:

| Payload Type | Structure & Context | Raw JSON | TOON Format | Token Reduction | Compression Ratio |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Scalar Object** | 3-field response payload | 17 tokens | 13 tokens | **23.5%** | `0.771` |
| **Order History** | 10 e-commerce order entities | 347 tokens | 154 tokens | **55.6%** | `0.444` |
| **Call Telemetry Batch** | 20 telephony event records | 560 tokens | 184 tokens | **67.1%** | `0.329` |

#### Architectural Transformation
* **Raw JSON Overhead (560 tokens)**: Redundantly serializes dictionary keys (`call_id`, `duration`, `disposition`, `agent`, `sentiment`) across every row.
* **TOON Compression (184 tokens — 67.1% reduction)**: Extracts the schema once into a typed header (`logs[20|]{call_id,duration,...}:`) and streams values as pipe-delimited vectors, preserving lossless round-trip structure upon decode.

---

## Live Next.js Web Applications

Production Next.js web applications architected, implemented, and verified using the Antigravity 2.0 multi-agent harness (`Context7` & `Google Modern Web Guidance`):

| Application | Live Deployment | Architecture & Capabilities |
| :--- | :--- | :--- |
| **David Nguyen — Portfolio** | [david-nguyen-bay.vercel.app](https://david-nguyen-bay.vercel.app/) | Interactive Next.js portfolio showcasing AI systems architecture, headless commerce integrations, and technical operations. |
| **Sports Matrix Analytics** | [dashboard-five-tan-52.vercel.app](https://dashboard-five-tan-52.vercel.app/) | Real-time sports analytics and market line-movement dashboard backed by Supabase PostgREST, Cloud Run pollers, and Next.js App Router. |
| **Multi-Agent Agency Platform** | [swarm-agency.vercel.app](https://swarm-agency.vercel.app/) | Next.js web showcase demonstrating multi-agent software engineering workflows and AI automation services. |

---

## Repository Structure

```text
antigravity-portfolio/
├── native_orchestrator.py       # SDK-native Multi-Agent Orchestration Engine 
├── RECEPTIONIST_SOP.md          # Architecture, endpoints, and data schema SOP
├── pyrightconfig.json           # Type checking configuration
└── app_build/
    └── receptionist/
        └── app/
            ├── agent.py                 # ADK multi-agent routing topology 
            ├── agent_runtime_app.py     # FastAPI server deployment entrypoint 
            ├── tools.py                 # Tool declarations and bindings 
            └── tools_lib/
                ├── sheets.py            # Google Sheets client interface
                └── zendesk.py           # Zendesk REST API client interface
```

---

## Project Operations & Architecture Scope

This repository is a portfolio showcase containing stubs and interfaces of the production codebases. To run the full system in a production environment, refer to the private operational repositories.

**Environment**: Design patterns conform to the Google Antigravity 2.0 SDK and Google Agents SDK (ADK) interfaces.

---

## Tech Stack

* **Languages**: Python 3.11+, TypeScript, SQL
* **AI & Agent Frameworks**: Google Antigravity 2.0 SDK, Google Agent Development Kit (ADK), Gemini Live / Flash, Vertex AI
* **Protocols & Standards**: Model Context Protocol (MCP), TOON Protocol, OpenAPI / REST, WebSockets / WebRTC
* **Cloud & Infrastructure**: Google Cloud Run, Cloud Storage, Google Secret Manager, Vercel, Railway
* **Integrations & Data**: Supabase Vector Memory, Google Sheets API, Zendesk API, Medusa, Shopify, Contentful, Sanity.io, Exa Search

---

## License
This portfolio repository is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
