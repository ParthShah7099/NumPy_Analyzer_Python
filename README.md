
# 🚀 NumPy Analyzer

> **Built by THE PARTH SHAH – A Rising Visionary Student-Developer**  
> A next-gen NumPy-powered analytics toolkit using the power of Object-Oriented Python.

---

## 🧠 CEO's Opening Note

Welcome to **NumPy Analyzer** — a tool not just built with code, but with **clarity, curiosity, and command over data**.  
This project is for the dreamers who analyze patterns, solve problems, and reshape how we interact with numbers.  
Whether you're a budding data scientist or a Python aficionado, this toolkit is **your ultimate companion**.

Let’s not just run programs. Let’s engineer insights.

---

## 📚 Table of Contents

- [📖 Introduction](#-introduction)
- [🧪 Tech Stack](#-tech-stack)
- [✨ Features](#-features)
- [🧠 Behind the Code](#-behind-the-code)
- [🔎 How It Works (Demo)](#-how-it-works-demo)
- [📁 Folder Structure](#-folder-structure)
- [⚙️ Setup & Requirements](#️-setup--requirements)
- [❓ FAQs & Troubleshooting](#-faqs--troubleshooting)
- [🖼 Image Upload Guide (For Mac + VS Code)](#-image-upload-guide-for-mac--vs-code)
- [❤️ Let’s Connect](#️-lets-connect)

---

## 📖 Introduction

**NumPy Analyzer** is a console-based toolkit that lets users intuitively create, manipulate, and analyze NumPy arrays using a fully object-oriented design. Built to simplify complex computations and bring statistical insights within reach — this project is your data playground.

---

## 🧪 Tech Stack

| Tech         | Badge                                                                 |
|--------------|------------------------------------------------------------------------|
| Python       | ![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python) |
| NumPy        | ![NumPy](https://img.shields.io/badge/NumPy-%3E=1.24-blue?logo=numpy) |
| Terminal UI  | ![Console](https://img.shields.io/badge/CLI%20Based-Yes-black)        |

---

## ✨ Features

🔧 **Array Management**
- Create 1D, 2D, and 3D arrays.
- Index, slice, and reshape data.

➕ **Mathematical Operations**
- Element-wise addition, subtraction, multiplication, division.
- Dot Product & Matrix Multiplication for 2D arrays.

🔍 **Search, Sort, Filter**
- Locate values in arrays.
- Sort row-wise or full array.
- Filter using custom thresholds.

📊 **Statistics & Aggregation**
- Sum, Mean, Median, Variance, Standard Deviation
- Min/Max, Percentiles, and Correlation Coefficient

🧱 **Combining and Splitting**
- Concatenate arrays vertically or horizontally.
- Split arrays into parts with ease.

🧠 **Object-Oriented Design**
- Fully class-based with encapsulated logic.
- Static and class methods included.

🖥️ **User Interface**
- Intuitive console interface with menu-driven flow.
- Guided prompts and validations.

---

## 🧠 Behind the Code

At the heart of **NumPy Analyzer** lies the class: `DataAnalytics`. Every feature is wrapped in a clean, maintainable object-oriented structure. The constructor initializes your data, while methods are divided into modular operations — making your analytics journey feel like a guided mission.

Here's the vision breakdown:

```python
class DataAnalytics:
    def create_array()     # 1D, 2D, or 3D array creation
    def math_operations()  # Scalar & matrix-level operations
    def combine_split()    # Concatenation or splitting
    def search_sort_filter()  # Data interrogation
    def compute_statistics()  # Stats & aggregates
```

The `main()` function powers the **menu-driven UI**, guiding the user step by step.

---

## 🔎 How It Works (Demo)

### 📌 Welcome Menu
![Welcome Menu](./images/demo_0.png)

### ➕ Array Creation
![Array Creation](./images/demo_1.png)

### 🔢 Mathematical Operations
![Mathematical Operations](./images/demo_2.png)

### 🔗 Combine or Split Arrays
![Combine or Split](./images/demo_3.png)

### 🔍 Search, Sort, or Filter Arrays
![Search, Sort, or Filter](./images/demo_4.png)

### 📊 Aggregation and Statistics
![Aggregation and Statics](./images/demo_5.png)

### 👋 Exit
![Exit](./images/demo_6.png)

---

## 📁 Folder Structure

```
NumPy-Analyzer/
│
├── images/                 # Screenshots and visual assets
│   ├── demo_0.png
│   ├── demo_1.png
│   ├── demo_2.png
│   ├── demo_3.png
│   ├── demo_4.png
│   ├── demo_5.png
│   └── demo_6.png
│
├── numpy_analyzer.py       # Main application code
├── requirements.txt        # Required Python packages
└── README.md               # Project documentation
```

---

## ⚙️ Setup & Requirements

> Make sure Python 3.10+ and NumPy are installed.

### ✅ Installation Steps

```bash
git clone https://github.com/theparthshah/NumPy-Analyzer.git
cd NumPy-Analyzer
pip install -r requirements.txt
python numpy_analyzer.py
```

### 🧾 requirements.txt

```
numpy>=1.24
```

---

## ❓ FAQs & Troubleshooting

<details>
<summary>🧐 I'm getting "No array found. Create array first."</summary>

Make sure to select option 1 (Create Array) before performing any operations like math or search.
</details>

<details>
<summary>📐 Can I perform matrix multiplication with 1D arrays?</summary>

No. Only 2D arrays are supported for matrix operations like dot product or `matmul`.
</details>

<details>
<summary>📦 Will this work on Mac, Linux, and Windows?</summary>

Absolutely! This is a terminal-based Python script. It runs wherever Python runs.
</details>

---

## 🖼 Image Upload Guide (For Mac + VS Code)

Want to add screenshots to your README? Here's how:

1. **Create an `images/` folder** at your project root.
2. **Add images** (like PNGs or JPGs) inside this folder.
3. **Use Markdown syntax** like below:
   ```markdown
   ![Alt Text](./images/demo_1.png)
   ```
4. 💡 *Tip:* Name images meaningfully like `demo_1.png`, `result1.png`, `menu.png`.

---

## ❤️ Let’s Connect

If you found this project insightful or inspiring:

- ⭐ **Star this repo** — it fuels future updates!
- 🔄 Fork and extend it — I’d love to see your spin on it!
- 📬 Reach out: [LinkedIn - Parth Shah](https://www.linkedin.com/in/parth-shah-28387532b?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app)

> “Greatness begins with the boldness to build.” — *THE PARTH SHAH*

---
