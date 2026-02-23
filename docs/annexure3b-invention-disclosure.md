# Annexure 3B — Full Submission

## Invention Disclosure Document

### 1) Title
**Real-Time Cyber Threat Monitoring and Alert System for Indian Cyberspace (RTCMAS-IC)**

### 2) Internal Inventor / Student Details
- **Complete Name:** Ruppa Giridhar
- **Mobile Number:** +91 8978304323
- **Email (Personal):** giriruppa964@gmail.com
- **UID / Registration Number:** 12207968
- **Location of Internal Inventor:** Lovely Professional University, Punjab-144411, India
- **Signature:** Required

---

### 3) Description of the Innovation
The Real-Time Cyber Threat Monitoring and Alert System for Indian Cyberspace (RTCMAS-IC) is an integrated, national-scale cybersecurity intelligence platform designed to detect, record, analyze, and respond to cyber incidents in real time.

The system combines:
- Artificial Intelligence (AI)
- Machine Learning (ML)
- Federated Learning
- Permissioned, quantum-resistant blockchain
- Smart-contract-driven automation

#### Core capabilities
- Continuous ingestion of telemetry from government networks, enterprises, cloud platforms, IoT ecosystems, and public cyber sources.
- AI-assisted anomaly detection and threat ranking for phishing, ransomware, DDoS, data breaches, and advanced intrusions.
- Immutable cyber incident logging with metadata, timestamps, threat classifications, and forensic references.
- Predictive threat modelling to detect emerging attack campaigns before full-scale escalation.
- Role-based dashboards and near real-time alerting for CERT-In, government agencies, and participating security operations teams.
- National Cyber Threat Map for geolocated situational awareness and strategic cyber-readiness planning.
- Public-facing anonymized advisories for scams, phishing campaigns, and compromised infrastructure.

The architecture is designed for interoperability with existing SOC/SIEM/XDR systems through APIs and standards such as REST and STIX/TAXII, while aligning with NIST and ISO 27001-oriented operating principles.

---

## A) Problem Addressed by the Invention
India’s expanding digital infrastructure faces persistent cyber risks including ransomware, phishing, DDoS, data theft, and state-sponsored intrusions. Current incident reporting and intelligence sharing are fragmented across organizations and sectors.

### Key limitations in current ecosystem
- Siloed incident data with low cross-organization visibility.
- Delayed detection and response due to weak real-time correlation.
- Centralized repositories vulnerable to manipulation, loss, and unilateral control.
- Lack of a trusted, national, tamper-resistant incident ledger.
- Limited predictive intelligence at country scale.

**RTCMAS-IC** addresses this by creating a decentralized incident management architecture with blockchain-backed trust and AI-driven predictive cyber intelligence.

---

## B) Objectives of the Invention
1. **National real-time monitoring framework:** Integrate diverse cyber telemetry into a decentralized and tamper-resistant infrastructure.
2. **AI/ML-based threat intelligence:** Enable automated detection, classification, and prediction of attack patterns.
3. **National Cyber Threat Intelligence Map:** Provide anonymized geospatial awareness of ongoing and historical threats.
4. **Transparent yet privacy-protective reporting:** Support trusted inter-agency collaboration, forensic traceability, and law-enforcement workflows.
5. **Strategic R&D leadership:** Advance AI-blockchain integration for sovereign national cybersecurity capability.

---

## C) State of the Art / Research Gap / Novelty

| Sr. No. | Patent ID | Prior Art Summary | Research Gap | RTCMAS-IC Novelty |
|---|---|---|---|---|
| 1 | US20200106547A1 | AI anomaly detection focused on enterprise network defense. | Lacks national integration, tamper-proof logging, and multi-stakeholder real-time coordination. | National-scale, blockchain-backed, predictive threat collaboration across public and private sectors in India. |
| 2 | US20210184432A1 | Blockchain-based incident logging in organizational settings. | Limited AI analytics, weak interoperability, no national visual intelligence layer. | Integrates AI/ML, federated intelligence, and permissioned blockchain for countrywide cyber governance. |
| 3 | WO2020197360A1 | Global cyber incident reporting with domain reputation focus. | Not India-specific; limited policy/regulatory alignment with domestic frameworks. | India-specific architecture aligned to national governance needs and operational standards. |

---

## D) Detailed Description

### 1. System Architecture Components
1. **Edge/Local Data Collection Modules**
   - Collect telemetry from traffic logs, endpoints, IoT assets, and cloud workloads.
   - Normalize incoming data into a standard threat-event schema.

2. **Local AI/ML Threat Analysis Node**
   - Performs anomaly detection and local behavior analysis.
   - Generates **Threat DNA** (behavioral fingerprints).
   - Escalates high-confidence incidents.

3. **Federated Learning Network**
   - Shares encrypted model updates (not raw data).
   - Uses privacy-preserving methods such as secure aggregation and differential privacy.

4. **Blockchain Ledger Layer**
   - Stores validated incidents on a permissioned, quantum-resistant blockchain.
   - Captures incident hash, metadata, timestamps, and forensic references.

5. **Smart Contract & Automated Response Module**
   - Encodes validation rules, consensus thresholds, and response actions.
   - Supports automated policy push (firewall updates, containment, alerting) where authorized.

6. **Threat Correlation & National Cyber Threat Map**
   - Correlates incidents through a graph-based Threat DNA/IOC intelligence layer.
   - Produces near real-time geospatial threat visibility.

7. **Predictive Cyber Twin Simulation**
   - Models propagation scenarios and impact forecasts.
   - Supports proactive containment planning and resource allocation.

8. **Dashboard & API Layer**
   - Role-based dashboards for organizations and national authorities.
   - API integration with SOC/SIEM/SOAR tooling.

### 2. Operational Flow
1. Telemetry collection and normalization at participant nodes.
2. Local AI analysis and Threat DNA generation.
3. Submission of high-confidence incidents to blockchain workflow.
4. Validation via decentralized reputation-based consensus.
5. Ledger commit and correlation with historical campaign data.
6. Predictive simulation and risk scoring.
7. Smart-contract-assisted automated/manual response actions.
8. Continuous federated model improvement and redistribution.

### 3. Security and Privacy Features
- Federated learning (no raw data sharing)
- Differential privacy and encryption
- Quantum-resistant blockchain design
- Immutable chain-of-custody for incident records
- Decentralized governance to reduce tampering and misinformation risk

### 4. Advantages over Prior Art
- National-scale operational visibility.
- Integrated AI prediction + blockchain immutability + privacy-preserving collaboration.
- Faster response and improved policy-readiness.
- Trusted collaboration across government and private infrastructure operators.

### 5. Industrial Applicability
- CERT and government cybersecurity operations
- Critical infrastructure (telecom, energy, banking, defense)
- Enterprise and cloud security operations
- Forensics and cybercrime investigation workflows

---

## E) Advantages
1. **National intelligence sharing without privacy compromise** through federated methods.
2. **Tamper-proof and future-ready trust model** using permissioned ledger and post-quantum cryptography.
3. **Predictive + automated defense** via Cyber Twin simulations and smart-contract-triggered containment.
4. **Decentralized governance and resilience** with proof-of-reputation incident validation.

---

## F) Expansion Variables (Coverage Goals)
- Sector integration depth (SCADA/ICS, 5G, fintech, cloud providers)
- Modular post-quantum cryptography adoption
- Advanced privacy layers (SMC, differential privacy, homomorphic encryption)
- Reputation-based decentralized governance model
- Edge/IoT-ready local node deployment
- SOAR/XDR interoperability for Indian SOC deployments

---

## G) Working Prototype Status
- **Status:** Not ready; research ongoing
- **Core stack (proposed):**
  - Permissioned blockchain (e.g., Hyperledger Fabric + PQC module)
  - Federated AI frameworks (e.g., TensorFlow Federated / PySyft)
  - Graph intelligence (e.g., Neo4j)
  - Cyber Twin simulation (Python-based, Kubernetes-deployable)
- **MVP target:** 1 aggregator + 3 ledger nodes + 5 local AI nodes demonstrating end-to-end flow
- **Estimated MVP time:** 9–12 months
- **Scalability path:** cloud-native microservices and horizontal scale-out

---

## H) Existing / Comparative Positioning
RTCMAS-IC distinguishes itself from conventional SIEM/global threat feeds through:
- Nationwide, privacy-preserving intelligence generation
- Immutable and cryptographically verifiable incident trust layer
- Predictive cyber twin simulation and policy orchestration
- Decentralized, reputation-weighted governance for incident validation

---

## 5) Use and Disclosure
- Public revelation/display: **No**
- Market outreach/licensing attempt: **No**
- Published/public internet disclosure: **No**
- Collaboration with external institute/organization: **No**
- Potential required regulatory interfaces: **CERT-In, NCIIPC, MeitY**

## 6) Public Links and Dates
No prior public disclosure links or dates available; invention remains confidential.

## 7) Collaboration / MOU Details
No MOU or external collaboration finalized to date.

## 8) Commercialization Opportunities
- Cyber Defense-as-a-Service (CDaaS) platform potential
- Target users: national governments, critical infrastructure operators, large enterprises
- High-value defensible IP: federated learning + PQC blockchain + cyber twin simulation

## 9) Potential Commercialization Outreach Firms
- Tata Consultancy Services — https://www.tcs.com
- Wipro — https://www.wipro.com
- Infosys — https://www.infosys.com
- Palo Alto Networks — https://www.paloaltonetworks.com
- CrowdStrike — https://www.crowdstrike.com
- Tech Mahindra — https://www.techmahindra.com

## 10) Fundamental Patents / Royalty Dependencies
No direct foundational patent identified that mandates royalty for this exact integrated architecture at the current stage.

## 11) Filing Options
- **Provisional filing:** Recommended immediately for priority date protection.
- **Complete filing:** Target within 12 months after MVP validation.
- **PCT filing:** High potential for international protection and exportable sovereign cybersecurity model.

## 12) Keywords
Decentralized Cyber Threat Intelligence Fabric; Federated Learning Cybersecurity; Quantum-Resistant Blockchain Ledger; Cyber Twin Engine Simulation; Threat DNA Generation; Proof-of-Reputation Governance; National Cyberspace Protection; Smart Contract Security Automation; Privacy-Preserving Threat Sharing; Critical Infrastructure Defense.
