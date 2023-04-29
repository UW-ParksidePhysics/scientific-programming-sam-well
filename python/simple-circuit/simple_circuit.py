"""
simple_circuit.py

This program calculates the current in each resistor for five predefined
circuits, given the user's input values for voltage and resistance.
"""

import sys
import PySimpleGUI as sg
from tools import *
import math

def main():
    # Ensure using Python version 3.11 or greater
    if sys.version_info < (3, 10):
        sys.exit('Sorry, Python < 3.10 is not supported')

    # Define layouts for each window
    layout1 = generate_layout('graph1')
    layout2 = generate_layout('graph2', resistor_count=2)
    layout3 = generate_layout('graph3', resistor_count=2)
    layout4 = generate_layout('graph4', resistor_count=3)
    layout5 = generate_layout('graph5', resistor_count=3)

    # Define base layout
    layout = [
        [
            sg.Column(layout1, key='-COL1-'),
            sg.Column(layout2, key='-COL2-', visible=False),
            sg.Column(layout3, key='-COL3-', visible=False),
            sg.Column(layout4, key='-COL4-', visible=False),
            sg.Column(layout5, key='-COL5-', visible=False)
        ],
        [
            [
                sg.Button('1', key='1'), sg.Button('2', key='2'), sg.Button('3', key='3'),
                sg.Button('4', key='4'), sg.Button('5', key='5')
            ],
            sg.Submit('Update', key='-UPDATE-')
        ]
    ]

    # Create master window
    window = sg.Window('Simple Circuit', layout, finalize=True)

    # Set starting window
    graph = window['graph1']
    layout = 1
    graph.draw_image(filename='assets/SimpleCircuits-1.png', location=(0, 500))

    output = None  # Initialize for later use
    while True:  # PySimpleGui main loop
        event, values = window.read()
        # print(event, values)  # DEBUG
        if event == sg.WIN_CLOSED:
            break
        if event == '-UPDATE-':  # On update, redraw image and clear old output
            graph_index = graph.key[-1]  # Returns current window number
            graph.draw_image(filename=f"assets/SimpleCircuits-{graph_index}.png", location=(0, 500))
            graph.delete_figure(output)
        elif event in '12345':  # Toggles window visibility
            window[f'-COL{layout}-'].update(visible=False)
            layout = int(event)
            window[f'-COL{layout}-'].update(visible=True)

        # Window switch: Set window and draw appropriate image
        match event:
            case '1':
                graph = window['graph1']
                circuit = graph.draw_image(filename='assets/SimpleCircuits-1.png', location=(0, 500))
            case '2':
                graph = window['graph2']
                circuit = graph.draw_image(filename='assets/SimpleCircuits-2.png', location=(0, 500))
            case '3':
                graph = window['graph3']
                circuit = graph.draw_image(filename='assets/SimpleCircuits-3.png', location=(0, 500))
            case '4':
                graph = window['graph4']
                circuit = graph.draw_image(filename='assets/SimpleCircuits-4.png', location=(0, 500))
            case '5':
                graph = window['graph5']
                circuit = graph.draw_image(filename='assets/SimpleCircuits-5.png', location=(0, 500))

        voltage = None
        resistors = None
        currents = None
        # Check which layout is currently displayed, validate user input, then calculate current(s)
        match graph.key:
            case 'graph1':
                user_inputs = [values['graph1_voltage'],
                            values['graph1_resistor1']]
                if user_input_is_valid(user_inputs):
                    voltage = float(values['graph1_voltage'])
                    resistors = [float(values['graph1_resistor1'])]

                    currents = [float(voltage) / float(resistors[0])]
            case 'graph2':
                user_inputs = [values['graph2_voltage'],
                            values['graph2_resistor1'],
                            values['graph2_resistor2']]
                if user_input_is_valid(user_inputs):
                    voltage = float(values['graph2_voltage'])
                    resistors = [float(values['graph2_resistor1']),
                                float(values['graph2_resistor2'])]

                    currents = [(voltage / sum(resistors)),
                                (voltage / sum(resistors))]
            case 'graph3':
                user_inputs = [values['graph3_voltage'],
                            values['graph3_resistor1'],
                            values['graph3_resistor2']]
                if user_input_is_valid(user_inputs):
                    voltage = float(values['graph3_voltage'])
                    resistors = [float(values['graph3_resistor1']),
                                float(values['graph3_resistor2'])]

                    currents = [(voltage / resistors[0]), (voltage / resistors[1])]
            case 'graph4':
                user_inputs = [values['graph4_voltage'],
                            values['graph4_resistor1'],
                            values['graph4_resistor2'],
                            values['graph4_resistor3']]
                if user_input_is_valid(user_inputs):
                    voltage = float(values['graph4_voltage'])
                    resistors = [float(values['graph4_resistor1']),
                                float(values['graph4_resistor2']),
                                float(values['graph4_resistor3'])]

                    currents = [(voltage / resistors[0]),
                                (voltage / (resistors[1] + resistors[2])),
                                (voltage / (resistors[1] + resistors[2]))]
            case 'graph5':
                user_inputs = [values['graph5_voltage'],
                            values['graph5_resistor1'],
                            values['graph5_resistor2'],
                            values['graph5_resistor3']]
                if user_input_is_valid(user_inputs):
                    voltage = float(values['graph5_voltage'])
                    resistors = [float(values['graph5_resistor1']),
                                float(values['graph5_resistor2']),
                                float(values['graph5_resistor3'])]

                    currents = [(voltage / resistors[0]),
                                (voltage / resistors[1]),
                                (voltage / resistors[2])]

        # If currents are calculated, add values to image
        if currents is not None:
            graph_index = graph.key[-1]  # Returns current window number
            graph.draw_image(filename=f"assets/SimpleCircuits-{graph_index}b.png", location=(0, 500))

            # Add text according to window number
            match graph.key:
                case 'graph1':
                    output = [
                        graph.draw_text(f"{voltage} V", (40, 250), color='white'),
                        graph.draw_text(f"{resistors[0]} Ω", (450, 250), color='white'),
                        graph.draw_text(f"{currents[0]:.6f} A", (300, 250), color='white')
                    ]
                case 'graph2':
                    output = [
                        graph.draw_text(f"{voltage} V", (40, 250), color='white'),
                        graph.draw_text(f"{resistors[0]} Ω", (250, 440), color='white'),
                        graph.draw_text(f"{currents[0]:.6f} A", (250, 290), color='white'),
                        graph.draw_text(f"{resistors[1]} Ω", (470, 250), color='white'),
                        graph.draw_text(f"{currents[1]:.6f} A", (320, 250), color='white')
                    ]
                case 'graph3':
                    output = [
                        graph.draw_text(f"{voltage} V", (40, 260), color='white'),
                        graph.draw_text(f"{resistors[0]} Ω", (200, 310), color='white'),
                        graph.draw_text(f"{currents[0]:.6f} A", (300, 160), color='white'),
                        graph.draw_text(f"{resistors[1]} Ω", (350, 310), color='white'),
                        graph.draw_text(f"{currents[1]:.6f} A", (430, 160), color='white')
                    ]
                case 'graph4':
                    output = [
                        graph.draw_text(f"{voltage} V", (90, 290), color='white'),
                        graph.draw_text(f"{resistors[0]} Ω", (190, 300), color='white'),
                        graph.draw_text(f"{currents[0]:.6f} A", (190, 200), color='white'),
                        graph.draw_text(f"{resistors[1]} Ω", (350, 410), color='white'),
                        graph.draw_text(f"{currents[1]:.6f} A", (320, 280), color='white'),
                        graph.draw_text(f"{resistors[2]} Ω", (450, 140), color='white'),
                        graph.draw_text(f"{currents[2]:.6f} A", (390, 210), color='white')
                    ]
                case 'graph5':
                    output = [
                        graph.draw_text(f"{voltage} V", (95, 310), color='white'),
                        graph.draw_text(f"{resistors[0]} Ω", (220, 310), color='white'),
                        graph.draw_text(f"{currents[0]:.6f} A", (210, 170), color='white'),
                        graph.draw_text(f"{resistors[1]} Ω", (310, 310), color='white'),
                        graph.draw_text(f"{currents[1]:.6f} A", (300, 170), color='white'),
                        graph.draw_text(f"{resistors[2]} Ω", (420, 310), color='white'),
                        graph.draw_text(f"{currents[2]:.6f} A", (410, 170), color='white')
                    ]

    window.close()

if __name__ == "__main__":
    main()

