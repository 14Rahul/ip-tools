

# IP-Tool

## Overview

**IP-Tool** is a Python-based utility designed to explore IP range collisions in a Kubernetes cluster. It performs two primary functions:

1. **Default Mode:** Reports the configured IP networks on the container where the tool is deployed.
2. **Collision Check:** Analyzes a concatenated list of IP networks (collected from all containers in the cluster) to detect any overlapping (colliding) IP networks using the `--check-collision <file_path>` switch.

For bonus points, a Kubernetes deployment YAML file is included to help deploy the container running IP-Tool.

---

## Repository Structure

```
ip-tool/
├── Dockerfile
├── README.md
├── ip_tool.py
├── requirements.txt
├── k8s_deployment.yaml
└── tests
    ├── __init__.py
    └── test_ip_tool.py
```

- **`ip_tool.py`**: The main script implementing both the default and collision check functionalities.
- **`Dockerfile`**: Builds the container image that runs the script.
- **`requirements.txt`**: Lists the required Python libraries (e.g., `psutil`).
- **`k8s_deployment.yaml`**: Sample Kubernetes deployment configuration.
- **`tests/`**: Contains unit tests for the IP-Tool script.

---

## Getting Started

### Prerequisites

- **Python 3.8+**  
- **Docker** (if building/running the container)
- **Kubernetes** (optional, for deploying via `k8s_deployment.yaml`)

### Setup

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd ip-tool
   ```

2. **Install Python Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Default Mode

To display the container's configured IP networks:

```bash
python ip_tool.py
```

### Collision Check Mode

To check for overlapping IP networks from a file (each network should be on a new line):

```bash
python ip_tool.py --check-collision path/to/ip_list.txt
```

---

## Running Tests

Ensure your tests directory is treated as a package by having an empty `__init__.py` file in the `tests/` folder.

Run tests using Python’s `unittest`:

```bash
python -m unittest discover -s tests
```

Or run a specific test module:

```bash
python -m unittest tests.test_ip_tool
```

---

## Docker Instructions

### Build the Docker Image

From the project root:

```bash
docker build -t ip-tool .
```

### Run the Docker Container

To run in default mode:

```bash
docker run --rm ip-tool
```

For collision check mode (assuming you have an IP networks file inside the container):

```bash
docker run --rm ip-tool --check-collision /path/to/ip_list.txt
```

*Note:* Adjust the file path inside the container as needed.

---

## Kubernetes Deployment (Bonus)

If you have a Kubernetes cluster, update the image name in `k8s_deployment.yaml` and deploy the IP-Tool container:

```bash
kubectl apply -f k8s_deployment.yaml
```

This deployment creates a pod running IP-Tool which will report the container’s IP networks.

---

## Additional Notes

- **Error Handling:** The script includes error handling for file access and IP network parsing.
- **Testing:** Basic unit tests are provided in `tests/test_ip_tool.py` to ensure collision detection functionality.
- **Improvements:** Feel free to expand the tool by adding logging, enhanced error handling, or more extensive tests.

---

## License

This project is provided under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This README provides a clear overview, setup instructions, usage examples, and additional context for the IP-Tool assignment. Feel free to modify it to better suit your specific needs or deployment environment.
