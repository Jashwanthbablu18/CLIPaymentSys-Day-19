# 💳 Day 19 - Payment System: Polymorphism & Encapsulation

Hey there! 👋  
Welcome to **Day 19** of my **#30DaysOfPythonChallenge**. Today I built a secure payment system using Object-Oriented Programming concepts like polymorphism and encapsulation to simulate real-world payment behavior.

---

## 📌 What’s This About?
Today’s focus: **Polymorphism** and **Encapsulation** in Python — enabling flexibility and security in class-based applications.

---

## 💭 Why Is This Useful?
When building apps that involve multiple behaviors (like different payment methods), **polymorphism** allows each method to define its own version of an action (like `pay()`).  
Meanwhile, **encapsulation** protects sensitive data like wallet balance from external interference — crucial for secure systems!

---

## ✨ Features

Here’s what the app can do:
- 💳 Supports multiple payment types: UPI, Card, Wallet
- 🔁 Uses the same `pay()` interface across all payment methods
- 🔐 Keeps wallet balance secure using encapsulation
- 🚫 Validates sufficient balance before wallet deductions

---

## 🛠️ Tech Stuff

Built with:
- 🐍 **Python 3**
- 🧱 Classes & Inheritance
- 🔁 Polymorphism via method overriding
- 🔒 Encapsulation using private attributes (`__balance`)

---

## 🚀 Getting It Running

### ✅ What You’ll Need
Just Python 3!  
Run the program with:
```bash
python Day-19Code.py
