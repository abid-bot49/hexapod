# Hexapod Robot — ROS 2 Jazzy

## Overview

This project focuses on the development of a six-legged (hexapod) walking robot using ROS 2 Jazzy.

The primary goal is to develop a modular hexapod robot with 18 Degrees of Freedom (DOF), using Python for control algorithms and ROS 2 for robot communication and integration.

## Development Environment

- OS: Ubuntu 24.04
- ROS 2: Jazzy Jalisco
- Programming Language: Python
- IDE: Visual Studio Code
- Robot Description: URDF / Xacro
- Visualization: RViz 2

## Robot Configuration

| Component | Specification |
|---|---|
| Robot Type | Hexapod |
| Number of Legs | 6 |
| Coxa Joints | 6 |
| Femur Joints | 6 |
| Tibia Joints | 6 |
| Total DOF | 18 |
| Main Controller (planned) | Raspberry Pi 5 |
| Actuators (planned) | Bus Servos |
| Sensors (planned) | Camera and LiDAR |

## Project Structure

```text
hexapod_ws/
├── src/
│   └── hexapod_description/
│       ├── urdf/
│       ├── launch/
│       ├── meshes/
│       ├── rviz/
│       ├── package.xml
│       └── setup.py
├── .gitignore
└── README.md
```

## Current Progress

- [x] ROS 2 Jazzy installation
- [x] Workspace setup
- [x] Hexapod URDF/Xacro model
- [x] 18 revolute joints
- [x] Robot State Publisher
- [x] Joint State Publisher GUI
- [x] RViz 2 visualization
- [ ] Forward Kinematics
- [ ] Inverse Kinematics
- [ ] Tripod Gait
- [ ] Gazebo simulation
- [ ] ROS 2 robot controller
- [ ] Raspberry Pi 5 integration
- [ ] Bus servo integration
- [ ] Camera and LiDAR integration

## Build and Run

Source ROS 2:

```bash
source /opt/ros/jazzy/setup.bash
```

Build the workspace:

```bash
cd ~/hexapod_ws
colcon build --symlink-install
```

Source the workspace:

```bash
source install/setup.bash
```

Launch the robot visualization:

```bash
ros2 launch hexapod_description display.launch.py
```

## Development Roadmap

1. Robot description and visualization
2. Forward and inverse kinematics
3. Gait generation and tripod walking
4. Gazebo simulation
5. ROS 2 control integration
6. Raspberry Pi 5 hardware integration
7. Camera and LiDAR integration

## Project Status

Currently in the robot description and visualization development stage.

The project will be developed incrementally, starting with simulation and moving toward physical hardware implementation.