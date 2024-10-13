from IPython.display import display, Latex, Math, HTML  # type: ignore

def printMatrix(M):
    html_table = "<table style='border-collapse: collapse; width: 50%; margin: auto;'>"
    for row in M:
        html_table += "<tr>"
        for cell in row:
            html_table += f"<td style='border: 1px solid black; padding: 10px; text-align: center;'>{cell}</td>"
        html_table += "</tr>"
    html_table += "</table>"

    display(HTML(html_table))

def printVector(V):
    html_table = "<table style='border-collapse: collapse; margin: auto;'>"
    for cell in V:
        html_table += f"<tr><td style='border: 1px solid black; padding: 10px; text-align: center;'>{cell}</td></tr>"
    html_table += "</table>"

    display(HTML(html_table))

def printBig(text):
    text = f'<div style="text-align: center; font-size: 24px;"><p>{text}</p></div>'
    
    display(HTML(text))
