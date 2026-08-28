# cicd-day4

A simple project for practicing continuous integration and continuous delivery (CI/CD) workflows.

## Member

- Chalanthon Ainthachot
- Chayathorn Apichattham
- Jiraporn Pengtong
- Sriamara Meepring
- Worapol Khunaekanan

## Getting Started

1. Clone the repository.
2. Install the project dependencies, if required.
3. Run the project or tests using the available scripts.

## File Structure

```text
.
├── .github/
│   └── workflows/
│       ├── e01-whoami.yml
│       ├── e02-validate.yml
│       ├── e03-tests.yml
│       ├── e04-deploy-dev.yml
│       ├── e05-deploy-and-run.yml
│       ├── e06-artifacts.yml
│       └── e07-mlflow.yml
├── resources/
│   └── booking_summary.job.yml
├── src/
│   ├── functions/
│   │   └── report.py
│   ├── aggregate.ipynb
│   ├── aggregate.py
│   ├── prepare.ipynb
│   ├── prepare.py
│   ├── report.ipynb
│   └── report.py
├── tests/
│   ├── booking_by_property_type.png
│   ├── booking_by_property_type_20260828_072119.png
│   ├── summary.md
│   └── summary_20260828_072119.md
├── .gitignore
├── databricks.yml
├── explore_data.ipynb
├── pytest.ini
├── requirements.txt
├── test.txt
└── test_file.md
```

- `.github/workflows/`: GitHub Actions workflows for CI/CD automation.
- `resources/`: Databricks job configuration files.
- `src/`: Data preparation, aggregation, reporting scripts, and notebooks.
- `tests/`: Generated reports and test artifacts.

## CI/CD

This repository is intended for learning and experimenting with automated builds, tests, and deployments.

## License

This project is for educational purposes.
