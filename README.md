# CloudProbe

## Automated service health checks using Docker, GitHub Actions, and AWS S3.

**Live Dashboard:** https://cloudprobe-dashboard.s3.us-east-1.amazonaws.com/index.html

CloudProbe is a lightweight monitoring tool that runs scheduled network checks (HTTP, TCP, DNS) against configurable targets. Tests are executed inside a Docker container via GitHub Actions on a cron schedule, with results published automatically to an S3-hosted static dashboard.


## Diagram
![CloudProbe Architecture](/CloudProbe_Lucidchart.png)

The system is fully automated: GitHub Actions builds and runs the container on a schedule, CloudProbe executes the checks, and results are published to S3 where a static dashboard renders the latest status.


### Core Components and features
- Scheduled health checks via GitHub Actions (cron)

- HTTP, TCP, and DNS test support

- Configurable test definitions via JSON

- Dockerized execution environment

- Automatic result publishing to AWS S3

- Static dashboard with pass/fail status and timings

### How It Works

1. GitHub Actions triggers on a cron schedule

2. Docker image is built and run

3. CloudProbe reads test definitions from sample-test.json

4. Tests are executed against external services

5. Results are written to output/results.json

6. Results are uploaded to an S3 bucket

7. Static dashboard fetches and displays the latest data

### Configuration

All tests live within the config folder of this project. Each test is formatted like this:  
```json
{
  "name": "Cloudflare DNS (TCP 53)",
  "action": "tcp",
  "params": {
    "host": "1.1.1.1",
    "port": 53,
    "timeout": 3
  }
}
```
First, the name is the actual name of the service being tested. Second, is the action. This can be HTTP, HTTPS, DNS or TCP, and determines how tests are performed and what information is returned. Finally, The "params" contain the data necessary to perform the test, like URL (for HTTP and HTTPS), the host and port (for DNS and TCP), and the timeout time. To add a new test, one simply has to edit the JSON in which the tests are contained, and the code will determine which tests to run, meaning adding tests requires no code changes! 

### Tech Stack

- Python (core application)

- Docker (containerized execution)

- GitHub Actions (CI + scheduling)

- AWS S3 (static hosting + artifact storage)

- HTML / CSS / JavaScript (dashboard)

### This project demonstrates:

- Designing an automated, scheduled workflow

- Containerizing a Python application

- Managing CI artifacts and cloud storage

- Building a minimal but functional frontend

- Debugging real-world CI/CD issues