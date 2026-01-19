# LLM-SrcLog

This repository contains the implementation of the paper: **"LLM-SrcLog: Towards Proactive and Unified Log Template Extraction via Large Language Models"**. For more details on the methodology and experimental results, please refer to the `LLM-SrcLog.pdf` document in the root directory.

## Project Overview

LLM-SrcLog is a proactive and unified framework for log template extraction. It leverages Large Language Models (LLMs) to extract templates from both source code and existing logs, providing a more accurate and comprehensive solution for log analysis.

## Directory Structure

- `codebases/`: Contains the target source code repositories for template extraction.
- `dataset/`: Includes a subset of the LogPAI datasets used for evaluation.
- `log_template/`: Stores the extracted log templates in structured formats.
- `report/`: Contains evaluation reports and performance metrics.

## Core Modules

- **`static_ana` (Static Analysis Module)**: Handles the parsing of source code to identify and extract logging statements.
- **`LLM_ana` (LLM Template Extraction & Post-processing)**: Utilizes LLMs to generate log templates and performs refinement/post-processing to ensure quality.
- **`match` (Matching & Evaluation)**: Matches extracted templates against logs and calculates evaluation metrics (e.g., Precision, Recall, F1-Score).

## Examples

The repository provides a complete example using the **Zookeeper** subset from the LogPAI dataset. This example demonstrates the full pipeline from source code analysis to final evaluation.

## Usage Instructions

### 1. Install Dependencies

Ensure you have Python installed, then install the required packages:

```bash
pip install -r requirements.txt
```

### 2. Run LLM Template Extraction

Open the `LLM_ana.ipynb` notebook. Configure your LLM API settings and run all cells to extract log templates and perform post-processing.

### 3. Run Matching and Evaluation

Open the `match.ipynb` notebook and run all cells. This will evaluate the extracted templates against the provided logs and generate a detailed report in the `report/` directory.
