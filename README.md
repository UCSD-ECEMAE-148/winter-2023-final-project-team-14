**Software and Hardware Description:**
The OAK-D and depthAI are AI-enabled stereo cameras that allow for depth perception and 3D mapping. They are powerful tools for computer vision applications, such as object detection and tracking. The depthAI is a board that enables faster processing of images by offloading the computational workload from the main processor to dedicated hardware. 
YOLO (You Only Look Once) is a real-time object detection system that is capable of detecting objects in an image or video feed. It is a popular deep learning model that is used in many computer vision applications, including self-driving cars and robotics.
PyVesc is a Python library for controlling VESC-based motor controllers. The VESC is an open-source ESC (Electronic Speed Controller) that is widely used in DIY robotics projects. PyVesc allows for easy communication with the VESC and provides an interface for setting motor parameters and reading sensor data.

**Project Overview:**
We first used the OAK-D and depthAI to detect stop signs in the robot's field of view. Then, we executed the deep learning model YOLO to process the camera feed and identify the stop sign. Once the stop sign is detected, we implemented PyVesc to send a command to the motor controller to stop the robot and started to set up the OAK-D and depthAI cameras by installing the necessary software libraries. YOLO is capable of detecting multiple objects simultaneously, so we needed to filter out the stop sign from other detected objects. It was also useful to combine the lane following model with stop sign model;however, we needed a blob converter to take different data types and convert them into a Binary Large Object (BLOB) needed for our code. Finally, once the stop sign is detected, we accessed PyVesc to send a command to the motor controller to stop the robot. In summary, the integration of OAK-D, depthAI, YOLO, and PyVesc allows for efficient and accurate stop sign detection and safe stopping of the robot. This implementation can be further customized and optimized for specific robotic platforms and use cases.

**Final Projet Presentation:** https://docs.google.com/presentation/d/1BTMwfktHvDzfzYd6oSnHeaQTEBbtYg8wEMnqoWkamHE/edit?usp=sharing

**Final Project Video:** https://drive.google.com/file/d/1OnO5qWczQbH_aVrgKAtejwLMw6-fFSRW/view?usp=share_link

**Team Members: Anish Kulkarni, Manuel Abitia, Zizhe Zhang.**

**ECE - MAE 148 Team 14 Winter 2023**
