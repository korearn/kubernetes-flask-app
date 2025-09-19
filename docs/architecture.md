┌─────────────────┐    ┌─────────────────┐
│   Ingress       │    │   MySQL         │
│   Controller    │    │   Database      │
│                 │    │   (StatefulSet) │
└─────────────────┘    └─────────────────┘
         │                    │
         ▼                    ▼
┌─────────────────┐    ┌─────────────────┐
│   Flask App     │◄───┤   Service       │
│   (Deployment)  │    │   Discovery     │
└─────────────────┘    └─────────────────┘
         │
         ▼
┌─────────────────┐
│   Auto-Scaling  │
│   (HPA)         │
└─────────────────┘

Components

    Flask Application: Web server with REST API

    MySQL Database: Persistent data storage

    Ingress: HTTP routing and load balancing

    HPA: Automatic scaling based on CPU usage

    ConfigMap/Secrets: Configuration management
    EOF