# 🤖 Wall-Following Robot in a Maze using Webots

## 📌 Overview

This project is a **wall-following robot simulation developed using Webots**.

The robot navigates through a maze by continuously detecting and following the wall beside it. Its movement is controlled based on sensor readings, allowing it to adjust its direction while moving through the maze.

The project demonstrates the fundamentals of **robot sensing, motion control, and autonomous navigation** in a simulated environment.

## 🎯 Objectives

* To simulate a robot navigating through a maze using Webots.
* To implement a wall-following approach for maze navigation.
* To use sensors to detect the nearby wall.
* To control the robot's movement based on sensor readings.
* To understand the basic principles of autonomous robot navigation.

## 🛠️ Technologies Used

* **Webots** – Robotics simulation platform
* **Python** – Robot controller programming
* **Robot Sensors** – Wall detection
* **Git & GitHub** – Project version control

## ⚙️ How It Works

The robot continuously reads the values from its sensors to detect the wall beside it.

Based on the sensor readings, the robot adjusts its movement so that it can **stay alongside the wall while moving through the maze**.

The basic process is:

```text
Start
  ↓
Read sensor values
  ↓
Detect nearby wall
  ↓
Adjust robot direction
  ↓
Move along the wall
  ↓
Continue through the maze
  ↓
Repeat
```

This allows the robot to autonomously follow the maze walls without requiring manual control.

## 📂 Project Structure

```text
Wall-Following-Robot/
│
├── worlds/
│   └── maze.wbt
│
├── controllers/
│   └── wall_follower/
│       └── wall_follower.py
│
├── screenshots/
│   └── simulation.png
│
└── README.md
```

## 🧠 Key Concepts

* Robot simulation
* Wall following
* Sensor-based navigation
* Autonomous movement
* Maze navigation
* Robot motion control
* Python programming
* Webots simulation

## 📚 Learning Outcomes

Through this project, I gained practical experience in:

* Creating and working with robotic simulations in Webots
* Programming a robot controller using Python
* Using sensor readings to control robot movement
* Implementing a basic wall-following approach
* Understanding autonomous navigation in a maze
* Testing and debugging robot behavior in simulation

## 🚀 Future Improvements

* Improve the robot's wall-following accuracy.
* Optimize its movement around corners.
* Add more complex maze environments.
* Experiment with different maze-solving algorithms.
* Compare wall-following with other navigation techniques.

## 👩‍💻 Author

**QuantumPanda82**
