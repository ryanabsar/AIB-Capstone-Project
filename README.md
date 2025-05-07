# AIB Capstone Project – Group D  
**Imperial College Business School**  
**MSc Business Analytics**

## 📌 Project Overview
This repository contains the work for the *Analytics in Business (AIB) Capstone Project*, undertaken as part of the MSc Business Analytics program at Imperial College London.  

## 👥 Team  
**Group D**  
- Abdulaziz Alfaraj  
- Abu Monguno  
- Adeeb Katib  
- Divya Gupta  
- Kanha Sodani  
- Laotan Faji  
- Nishita Badola  
- Ryan Primadi  

---

## ⚙️ Environment Setup

Before proceeding, ensure you have **Python 3.11** installed. You can install it using one of the following methods:

### ✅ Option A: Using Conda (Recommended)

1. **Create a new environment with Python 3.11**:

   ```bash
   conda create -n aib-project python=3.11
   conda activate aib-project
````

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

---

### ✅ Option B: Using Standard Python

1. **Download and install Python 3.11** from
   [https://www.python.org/downloads/release/python-3110/](https://www.python.org/downloads/release/python-3110/)

2. **Create a virtual environment**:

   ```bash
   python3.11 -m venv venv
   ```

3. **Activate the environment**:

   * On **Windows**:

     ```bash
     .\venv\Scripts\activate
     ```
   * On **macOS/Linux**:

     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

After activating the environment and installing dependencies, run the main notebook with:

```bash
cd 02_notebooks
jupyter notebook 99_main_analysis.ipynb
```

You can also explore other notebooks by week under the same directory.

---

<details>
<summary>📁 Project Structure</summary>

```
project-root/
├── 01_dataset/               # Raw and processed datasets
│   ├── raw/
│   └── processed/
│
├── 02_notebooks/             # Jupyter notebooks
│   ├── 01_week1_intro.ipynb
│   ├── 02_week2_analysis.ipynb
│   └── 99_main_analysis.ipynb  # Final or summary notebook
│
├── 03_scripts/               # Reusable Python scripts
│   ├── __init__.py
│   └── load_data.py
│
├── 04_outputs/               # Generated outputs
│   ├── figures/
│   └── tables/
│
├── README.md                 # Project overview
└── requirements.txt          # Dependencies
```

</details>

---

## 🛠 macOS Users – Fix for XGBoost `libomp.dylib` or 32-bit Error

If you encounter this error when importing XGBoost:

> `Library not loaded: @rpath/libomp.dylib`

You’ll need to install the **OpenMP runtime** (`libomp`) on macOS:

### ✅ Step 1: Install `libomp` using Homebrew

If you don’t have Homebrew installed:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Then:

```bash
brew install libomp
```

### ✅ Step 2: Link the library path (if needed)

If errors persist:

```bash
export DYLD_LIBRARY_PATH="/opt/homebrew/opt/libomp/lib:$DYLD_LIBRARY_PATH"
```

To make this permanent, add the line to your shell config:

* Zsh: `~/.zshrc`
* Bash: `~/.bash_profile` or `~/.bashrc`

Then restart your terminal and re-activate the virtual environment.

---

## 📄 License

**This project is intended for academic purposes only.**

