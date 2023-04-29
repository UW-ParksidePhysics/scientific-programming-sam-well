import PySimpleGUI as sg


def generate_layout(title, resistor_count=1):
    """
    Generates a layout from this template, adding resistors according to
    the resistor_count.
    """
    layout = [[sg.Graph(canvas_size=(500, 500), graph_bottom_left=(0, 0), graph_top_right=(500, 500),
                        background_color='black', enable_events=True, key=title)],
              [sg.Text('Voltage', size=(10, 1)), sg.InputText(default_text='5', key=f"{title}_voltage")]]

    for i in range(1, resistor_count+1):  # Add resistor_count (n) resistors
        layout.append(
            [sg.Text(f"Resistor{i}", size=(10, 1)),
             sg.InputText(default_text=str(i*100), key=f"{title}_resistor{i}")]
        )

    return layout


def user_input_is_valid(list_of_inputs):
    """Returns True if all inputs in list_of_inputs are digits."""
    return all(user_input.isdigit() for user_input in list_of_inputs)
