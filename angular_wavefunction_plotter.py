import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d

# Program that genrates a plot of a specific wavefunction specified by a user input


# takes an input from the user which is used to genrate the plot
def take_input():

    print("This program plots the 3D orbitals, without indication of phase")
    print("Please input the relevent quantum numbers for the orbital that you would like to plot, or exit if you wish to abort\n(so far only 1s, 2s, all 2p, and all 3d are avaliable)")

    quantum_input = input("enter quatum numbers in the form: n l ml \n")

    if quantum_input.lower() == "exit":
        return "exit"

    print("Input Entered")

    return quantum_input

# a function to genrate all of the data needed to make the plot, based on the user's input
def angulaur_wavefunction_maker():

    # take the input from the user, as to what plot they would like to genrate
    quantum_input = take_input()

    # if the user does not want to make a plot, exit
    if quantum_input == "exit":
        return

    # set the range for theta and phi
    phi, theta = np.linspace(0, 2 * np.pi, 1000), np.linspace(0, np.pi, 1000)
    # create a meshgrid over all theta and phi values, so that the data can be plotted over the top
    PHI, THETA = np.meshgrid(theta, phi)

    # stored angular wavefunction plots and titles, corrosponding the the given input by the user
    quantum_dictonary_plot = {"2 1 1" : np.sin(THETA) * np.cos(PHI) * (3 / (4 * np.pi)) ** 0.5,
                              "1 0 0" : (1 / (4 * np.pi) ) ** 0.5,
                              "2 0 0" : (1 / (4 * np.pi) ) ** 0.5,
                              "2 1 -1" : np.sin(THETA) * np.sin(PHI) * (3 / (4 * np.pi)) ** 0.5,
                              "2 1 0" : (3 / (4 * np.pi)) ** 0.5 * np.cos(THETA),
                              "3 2 0" : (0.25 * (5 / np.pi) ** 0.5) *(3 * np.cos(THETA) ** 2 -1),
                              "3 2 1" : (0.5 * (15 / np.pi) ** 0.5) * np.cos(THETA) * np.sin(THETA) * np.cos(PHI),
                              "3 2 -1" : (0.5 * (15 / np.pi) ** 0.5) * np.cos(THETA) * np.sin(THETA) * np.cos(PHI),
                              "3 2 2" : (0.25 * (15 / np.pi) ** 0.5) * np.sin(THETA) ** 2 * np.cos(2 * PHI),
                              "3 2 -2" : (0.25 * (15 / np.pi) ** 0.5) * np.sin(THETA) ** 2 * np.cos(2 * PHI),
                              "4 3 0" : 0.25 * (7 / np.pi) ** 0.5 * (2 - 5 * np.sin(THETA) ** 2) * np.cos(THETA),
                              "4 3 1" : - 1 / 8 * ( 21 / np.pi ) ** 0.5 * ( 5 * np.cos(THETA) ** 2 - 1) * np.sin(THETA),
                              "4 3 -1" : 1 / 8 * ( 21 / np.pi ) ** 0.5 * ( 5 * np.cos(THETA) ** 2 - 1) * np.sin(THETA),
                              "4 3 2" : 0.25 * ( 105 / ( 2 * np.pi ) ) ** 0.5 * np.cos(THETA) * np.sin(THETA) ** 2,
                              "4 3 3" : - 1 / 8 * (35 / np.pi) ** 0.5 * np.sin(THETA) ** 3}

    quantum_dictonary_title = {"2 1 1" : "2Px",
                               "1 0 0" : "1S",
                               "2 0 0" : "2S",
                               "2 1 -1" : "2Py",
                               "2 1 0" : "2Pz",
                               "3 2 0" : "3dz^2",
                               "3 2 1" : "3dxz set",
                               "3 2 -1" : "3dyz set",
                               "3 2 2" : "3dxy set",
                               "3 2 -2" : "3dyx set",
                               "4 3 0" : "4 3 0",
                               "4 3 1" : "4 3 1",
                               "4 3 -1" : "4 3 -1",
                               "4 3 2" : "4 3 2",
                               "4 3 3" : "4 3 3"}

    # if the input is incorrect
    if not quantum_input in quantum_dictonary_plot:
        print("\nIncorrect input\n")
        print("Valid inputs are:\n1 <= n <= 4\n0 <= l <= n - 1\n-l <= ml <= +l")
        return "fail"

    # genrate the data for the plot
    angulaur_part = quantum_dictonary_plot[quantum_input]
    angulaur_probiblity = angulaur_part ** 2

    x_axis = np.sin(THETA) * np.cos(PHI)
    y_axis = np.sin(THETA) * np.sin(PHI)
    z_axis = np.cos(THETA)

    x_plot = angulaur_probiblity * x_axis
    y_plot = angulaur_probiblity * y_axis
    z_plot = angulaur_probiblity * z_axis

    return [x_plot, y_plot, z_plot, quantum_dictonary_title, quantum_input]


# this function plots the relevent wavefunction, dependent of the user's input
def angular_wavefunction_plotter():

    # this line genrates all of the data needed to make a plot, based on the user's input
    plot_lst = angulaur_wavefunction_maker()

    # if the list is empty, the user exited... exit
    if not plot_lst:
        return

    # invalid input
    if plot_lst == "fail":
        return "fail"

    # assign variable names to the data for ease
    x_plot, y_plot, z_plot = plot_lst[0], plot_lst[1], plot_lst[2]
    quantum_dictonary_title, quantum_input = plot_lst[3], plot_lst[4]

    # genrate the figure with a 3D axis on it
    axis_2d = plt.figure()
    axis_3d = axis_2d.add_subplot(111, projection='3d')

    # make the plot and then label it
    axis_3d.plot_surface(x_plot, y_plot, z_plot, cmap="jet")

    axis_3d.set_xlabel("x")
    axis_3d.set_ylabel("y")
    axis_3d.set_zlabel("z")
    axis_3d.set_title(quantum_dictonary_title[quantum_input])

    plt.show()
    return

# this function calls the plotting function and carries out any re-runs or exits
def call():

    go = True

    while go:

        out = angular_wavefunction_plotter()

        # if the run was succesful or the user asked to exit, exit
        if not out == "fail":
            return

        else:

            question = input("Try again? (yes/no)\n")

            if not question.lower() == "yes":
                return

# drives code to ask the user which wavefunction they would like to plot
call()