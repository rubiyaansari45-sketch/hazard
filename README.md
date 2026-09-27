# Intelligent Identification of Hazard-Based Red Zones

A demo Flask application for:
- Hazard-based red-zone identification
- Carrying-capacity assessment
- Vulnerability scoring
- Immediate relocation prioritization
- Emergency alert generation

## Structure

```text
hazard_red_zone_demo/
├── app.py
├── config.py
├── requirements.txt
├── .env
├── README.md
├── templates/
│   └── index.html
└── alert/
    ├── __init__.py
    └── alert_manager.py
```

## Run

### 1. Create environment
```bash
python -m venv venv
```

### 2. Activate
Windows:
```bash
venv\Scripts\activate
```

Linux/macOS:
```bash
source venv/bin/activate
```

### 3. Install
```bash
pip install -r requirements.txt
```

### 4. Start
```bash
python app.py
```

Open:
http://127.0.0.1:5000

## Important

This is a demonstration scoring model, not a disaster-management decision system. The thresholds and weights are illustrative and must be validated using local hazard data, engineering standards, evacuation plans, and qualified emergency-management professionals before any real-world use.
