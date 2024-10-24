import os
from modules.animation import SimulationAnimation
from Van_Loan_schemes.Ellipse.system import System

def get_next_filename(folder='',prefix='simulation', ext='.gif'):
    num = len([file for file in os.listdir(folder) if file.lower().endswith(ext)])
    return os.path.join(folder,f'{prefix}{num}{ext}')

def main():
    # Configuration
    N = 20
    dt = 1

    # Initialize the system
    system = System(N)
    animation = SimulationAnimation(system, dt, limits=(-1,1), showLines=False)

    ani = animation.run_animation(frames=100, interval=100)
    ani.save(get_next_filename(folder='Van_Loan_schemes/Ellipse'), writer='pillow', fps=10)

if __name__ == "__main__":
    main()
