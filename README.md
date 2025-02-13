# 🧠 MentalAssess: Expert System for Mental Health Diagnosis  

## 📌 Introduction  

Mental health issues such as **depression, anxiety, and stress** are increasingly recognized as serious concerns affecting individuals worldwide. However, early diagnosis and treatment remain challenging due to the **subjective nature** of mental health symptoms.  

> 🔹 **MentalAssess** is a **web-based expert system** that assists in diagnosing mental health disorders using a **rule-based approach with Certainty Factor (CF) methodology)**.  
🔹 The system improves diagnostic **accuracy and reliability** by integrating **user-reported symptoms** with expert knowledge.  

## ❗ Problem Statements

Despite advancements in AI and expert systems, existing mental health assessment tools face **several challenges**:  

🔸 **Rigid Rule-Based Systems** – Many systems fail to capture the **complexity and variability** of psychological conditions.  
🔸 **Inconsistent Diagnoses** – Mental health symptoms are **highly subjective**, leading to **potential misdiagnoses**.  
🔸 **Handling Uncertainty** – Many expert systems struggle to manage **uncertainty in symptom reporting** effectively.  

## 🎯 Objectives  

The **MentalAssess** system aims to:  

✅ Enhance **early detection** of mental health disorders.  
✅ Improve **diagnostic reliability** using the **Certainty Factor (CF) approach**.  
✅ Provide a **user-friendly** and **accessible** web-based platform.  
✅ Generate **personalized diagnostic reports** based on user inputs.  

## 🔥 System Features  

🚀 **Web-Based Expert System** – Built with **Python, CLIPS, and Flask** for seamless deployment.  
🧮 **Certainty Factor (CF) Methodology** – Handles **uncertainty** in diagnosing mental health conditions.  
🎨 **User-Friendly Interface** – Developed using **HTML, CSS, and PHP** for an **intuitive** user experience.  
🐳 **Docker Integration** – Ensures **smooth** and **isolated** deployment of the application.  
📧 **Automated Email Reports** – Users can receive their **diagnostic results via email** for future reference.  

## 🛠️ Installation Guide  

### 📌 Prerequisites  

Before running **MentalAssess**, make sure you have:
- 🐍 **Python 3.9+**  
- 🐳 **Docker** (Optional)

### ⚙️ Steps to Install and Run  

1️⃣ **Clone the repository** 🖥️  
 
```bash
git clone https://github.com/rydzze/MentalAssess.git
cd MentalAssess
```

2️⃣ **Install dependencies** 📦

``` bash
pip install -r requirements.txt
```

3️⃣ **Prepare the .env file** 🛠️

Create a .env file in the root directory and configure the following environment variables:

```
SECRET_KEY=MentalAssess
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USE_SSL=False
MAIL_USERNAME=your-email-address@gmail.com
MAIL_PASSWORD=your-app-password
MAIL_DEFAULT_SENDER="MentalAssess Results <your-gmail@gmail.com>"
```

4️⃣ **Run the application**

**1. Using Python** 🐍

```
python run.py
```

**2. Using Docker (Alternative)** 🐳

```
docker build -t mentalassess .
docker run -d -p 988:988 --env-file .env --name mentalassess mentalassess
```

5️⃣ **Access the system via:** 🌍

```
http://localhost:988
```

## 📸 **Screenshots of User Interface**

![image](https://github.com/user-attachments/assets/19bdd134-1275-4c13-bde4-c54974aba875)

![image](https://github.com/user-attachments/assets/d6a11b4e-1ef2-4510-bce7-51b34b92c22f)

![image](https://github.com/user-attachments/assets/19190641-7315-4a35-848c-9c65c7622653)

## 🏆 **Contribution**

We would like to express our gratitude to the following individuals for their contributions to MentalAssess:

- [Muhammad Ariff Ridzlan](https://github.com/rydzze)
- [Muhammad Hafiz](https://github.com/IbnAsmuni)
- [Noor Alia Alisa](https://github.com/alia4lisa)
- [Siti Nur Aisyah](https://github.com/ayesharizani)

Your dedication and expertise have been instrumental in the development of this system. 🚀💡
