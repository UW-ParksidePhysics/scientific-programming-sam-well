"""
Annotate a plot using Pyplot's text function
"""

__author__ = "Sam Rodriguez"

import matplotlib.pyplot as plt


def annotate_plot(annotations):
    """
    Annotate a plot using Pyplot's text function
    :param annotations: dict
        Dictionary whose keys are the labels (strings) to be annotated and
        values are dictionary with the following key-value pairs:
        :'string': str
            Text string for the text function
        :'position': ndarray, shape (2)
            x, y coordinates for the position of the textbox
        :'alignment': list, str, shape (2)
            horizontalalignment and verticalalignment values for the text
            function
        :'fontsize': float
            Value of the font size in pixels
    :return:
    """
    plt.annotate(annotations['string'],
                 annotations['position'],
                 xycoords='figure fraction',
                 horizontalalignment=annotations['alignment'][0],
                 verticalalignment=annotations['alignment'][1],
                 fontsize=annotations['fontsize'])


if __name__ == "__main__":
    from datetime import datetime
    import numpy as np
    annotations = {'string': f"Created by {__author__} {datetime.today().isoformat()}",
                   'position': np.array([0, 0]),
                   'alignment': ['left', 'bottom'], 'fontsize': 10}
    plt.plot(5, 10)
    annotate_plot(annotations)
    plt.show()
