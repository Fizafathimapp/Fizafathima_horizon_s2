# Level 3 - ROS2 Task (Hard)

This repository contains the completion of Task 3, focusing on the installation of Ubuntu 22.04, ROS2 Humble, and the implementation of a basic Publisher-Subscriber communication system.

## Task Overview

### Part A & B: Environment Setup
* **Operating System:** Ubuntu 22.04 LTS
* **ROS2 Version:** Humble Hawksbill

### Part C: Publisher and Subscriber Communication
I have implemented a simple ROS2 project demonstrating communication between two nodes:

1.  **Node 1: Distance Publisher**
    * Generates random distance values (simulating a rover sensor).
    * Publishes data every 1 second
2.  **Node 2: Distance Subscriber**
    * Listens to the topic.
    * Prints the received distance values to the terminal.

---

## Deliverables in this Folder

| File Name | Description |
| :--- | :--- |
| `Ubuntu 22.04.png` | Screenshot of the successful Ubuntu 22.04 installation. |
| `ros2 humble.png` | Screenshot showing the verified ROS2 Humble environment. |
| `nodes running.mp4` | Screen recording showing the Publisher and Subscriber nodes communicating in real-time. |

---

## How to Run the Nodes
 navigate to your ROS2 workspace and run:

**To run the Publisher:**
```bash
ros2 run <distance_pkg> <publisher>

**To run the subscriber:**
```bash
ros2 run <distance_pkg> <subscriber>
