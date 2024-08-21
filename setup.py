import cx_Freeze
from cx_Freeze import Executable

# List all the Python files that your game depends on
executables = [Executable("main.py")]

# Include any additional files or directories (e.g., assets) if they exist
include_files = [
    ("sounds","sounds")
]  # Add your files or directories here

# Packages your game uses
packages = [
    "pygame",  # Ensure pygame is included
]

cx_Freeze.setup(
    name="Pong_V1_Pygame",
    version="1.0",
    description="A Pygame Pong Clone",
    options={
        "build_exe": {
            "packages": packages,
            "include_files": include_files,
            "includes": ["Class_Ball", "Class_Computer_Striker", "Class_Object", "Class_Striker", "duplicate_ball_mode", "game_setup", "increase_velocity_mode", "menu", "obstacle_mode", "original_mode"],  # List all modules
        }
    },
    executables=executables
)
