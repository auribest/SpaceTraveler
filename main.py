"""
SpaceTraveler.

@author         Andrés Uribe Stengel
@lastModified   10.08.2021
"""

# Imports
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from src.space import Space
from src.ufo import UFO
from src.utils import read_json_config, init_plot, update_plot


class Start(tk.Frame):
    """
    Wrapper for the Tkinter graphic user interface.
    """
    def __init__(self, master=None):
        # Initialize parent frame
        tk.Frame.__init__(self, master)

        # Set resizeability of the parent frame
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Setup the canvas
        self.setup()

    def setup(self):
        """
        Setup the GUI and run the SpaceTraveler.
        """
        # Initialize an empty plot
        fig, ax = init_plot()

        # Initialize the canvas with the empty plot
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.get_tk_widget().grid(row=0, column=0, padx='0', pady='0')
        canvas.draw()

        # Frame for the buttons
        frame = tk.Frame(master=root)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid(row=1, column=0, padx='0', pady='0', sticky='nswe')

        # Define and add the restart button
        restart_button = tk.Button(master=frame, text='RESTART', command=lambda: self.restart(canvas, ax))
        restart_button.grid(row=0, column=0, padx='5', pady='5', sticky='nswe')

        # Define and add the quit button
        quit_button = tk.Button(master=frame, text='QUIT', command=lambda: [root.destroy, quit()])
        quit_button.grid(row=0, column=1, padx='5', pady='5', sticky='nswe')

        # Start the space traveler and fill the canvas
        self.restart(canvas, ax)

    def restart(self, canvas, ax):
        """
        Start the SpaceTraveler and plot the trajectory with planets on the canvas.
        """
        # Start the space traveler
        space, ufo = self.run()

        # Clear the plot
        ax.clear()

        # Update the canvas with the newly plotted space traveler trajectory
        update_plot(canvas, ax, space, ufo)

    def run(self):
        """
        Start the SpaceTraveler trajectory.

        :return: tuple: (UFO) The generated space object and the generated UFO object.
        """
        # Read and set the user-defined parameters
        max_coordinate, n_planets = read_json_config()

        # Initialize the space object with the parameters
        space = Space(max_coordinate=max_coordinate, n_planets=n_planets)

        # Initialize the ufo object within space
        ufo = UFO(space=space)

        # Start the ufo's trajectory
        ufo.move()

        return space, ufo


if __name__ == '__main__':
    # Initialize Tkinter
    root = tk.Tk()
    root.wm_title("SpaceTraveler")
    root.resizable(False, False)

    # Initialize the GUI and the first run
    app = Start(master=root)

    # Halt python execution for Tkinter GUI
    app.mainloop()
