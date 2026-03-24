# Asteroids: An Object-Oriented Space Shooter

A modern implementation of the classic arcade game, developed as a capstone project for the [Boot.dev](https://www.boot.dev) Backend Development track. This project demonstrates proficiency in Python, game loop architecture, and object-oriented design.

## 🚀 Technical Highlights

- **Object-Oriented Programming (OOP)**: Utilized class inheritance and polymorphism to manage game objects like Players, Asteroids, and Shots.
- **Game Loop Architecture**: Implemented a robust game loop handling real-time input processing, physics updates (delta time), and frame rendering.
- **Vector Mathematics**: Used 2D vectors for movement, rotation, and collision physics.
- **Collision Detection**: Designed a custom circle-to-circle collision detection system to handle interactions between various game entities.
- **Static Assets & Resource Management**: Managed game state and assets efficiently using Pygame's sprite groups.

## 🛠️ Built With

- **Python 3**: Core logic and state management.
- **Pygame**: Graphics rendering and input handling.
- **Git/GitHub**: Version control and project documentation.

## 📥 Installation & Usage

### Prerequisites
- Python 3.10+
- Pygame (`pip install pygame`)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/asteroids.git
   cd asteroids
   
2. Run the application:
```bash
python3 main.py
```
🎮 Gameplay & Controls
Movement: W/S for thrust, A/D for rotation.
Combat: Spacebar to fire lasers.
Objective: Navigate through an increasingly dense asteroid field and destroy targets.

📈 Future Roadmap
- Scoring System: Implementing a persistent high-score database.
- AABB Collisions: Moving from circular hitboxes to more precise bounding boxes.
- Unit Testing: Adding a suite of tests for the physics engine logic.
