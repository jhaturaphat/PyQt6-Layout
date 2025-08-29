STYLESHEET = """
#sidebar {
    background-color: #2c3e50;
    border: none;
}

#sidebar_title {
    background-color: #34495e;
    color: white;
    font-size: 18px;
    font-weight: bold;
}

#sidebar_list {
    background-color: #2c3e50;
    color: white;
    border: none;
    outline: none;
}

#sidebar_list::item {
    padding: 10px;
    border-bottom: 1px solid #34495e;
}

#sidebar_list::item:selected {
    background-color: #3498db;
    color: white;
}

#sidebar_list::item:hover {
    background-color: #34495e;
}

#header {
    background-color: #ecf0f1;
    border-bottom: 1px solid #bdc3c7;
}

#header_title {
    font-size: 20px;
    font-weight: bold;
}

QPushButton {
    padding: 5px 10px;
    border-radius: 4px;
}

QPushButton:hover {
    background-color: #d6dbdf;
}
"""