# AI-Diagonsis-Medical-Prescription-Verification-Model

## Overview
Gen AI Prescription Verification is a robust AI-powered application that utilizes an open-source Large Language Model (LLM) and Tesseract OCR to verify prescription details from both image and text inputs. The solution is integrated with Streamlit, providing a user-friendly interface for seamless interaction and enhanced functionality.

## Features
- **OCR Integration:** Utilizes Tesseract OCR to extract text from prescription images.
- **LLM-based Verification:** Employs an open-source LLM to validate extracted prescription details.
- **Multi-Input Support:** Accepts both image and text-based prescription inputs.
- **Streamlit UI:** Provides an interactive web-based interface for real-time processing and results visualization.
- **Error Handling:** Implements robust error detection and handling mechanisms to ensure accurate verification.
- **Lightweight & Scalable:** Designed for efficiency with minimal resource requirements.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Tesseract OCR
- Required Python libraries (listed in `requirements.txt`)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/AI-Diagonsis-Medical-Prescription-Verification-Model
.git
   cd AI-Diagonsis-Medical-Prescription-Verification-Model
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install Tesseract OCR:
   - **Windows:** Download and install from [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)
   - **Linux/macOS:** Install via package manager:
     ```bash
     sudo apt install tesseract-ocr  # Ubuntu/Debian
     brew install tesseract          # macOS
     ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Usage
1. Upload an image of a prescription or enter prescription text manually.
2. Click the "Verify Prescription" button.
3. View extracted details and verification results in real time.


