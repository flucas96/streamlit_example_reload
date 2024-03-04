import streamlit as st

from st_customer_journey import st_customer_journey

st.set_page_config(layout="wide")

# Data for the Customer Journey Map
main_node_size = 20
child_node_size = 5
label_style_main = "font-weight: bold; font-size:15px;"
label_style_child = "font-size:13px;"
icon_style = "color: white;"

input_data = [
    { "id": 1,
        "name": "customer",
        "label": "Customer",
        "color": "white",
        "return_value": "customer",
       # "tooltip": "<b>NPS: child_node_size</b><br>Customer: Max Must",
        "disabled": True,
        "icon": "fa fa-user",
       # "icon_style": "color: white; background-color: red; border-radius: 50%;",
        "expand_direction": "up",
        "size": main_node_size,
        "label_position": "bottom",
        "label_style": label_style_main,
        "node_style": "stroke: black; stroke-width: 2px;",
},
{
    "id": 2,
    "name":"r&d",
    "label": "Research & Discover",
    "color": "#A3D2CE",
    "icon": "fa fa-magnifying-glass",
    "return_value": "r&d",
    "size": main_node_size,
    "label_position": "top",
    "expand_direction": "down",
    "label_style": label_style_main,
    "icon_style": icon_style,
    "children": [
        {
            "id": 3,
            "name": "advertising",
            "label": "See advertising",
            "color": "#A3D2CE",
            "return_value": "advertising",
            "size": child_node_size,
            "label_position": "right",
            "label_style": label_style_child,
        },
        {
            "id": 4,
            "name": "read_marketing",
            "label": "Read marketing content on website",
            "color": "#A3D2CE",
            "return_value": "read_marketing",
            "size": child_node_size,
            "label_position": "right",
            "label_style": label_style_child,
            "disabled": True,
        },
    ],
},
{
    "id": 5,
    "name":"fist_contact",
    "label": "First Contact",
    "color": "#A3D2CE",
    "icon": "fa fa-phone",
    "return_value": "first_contact",
    "size":main_node_size,
    "label_position": "bottom",
    "expand_direction": "up",
    "label_style": label_style_main,
        "icon_style": icon_style,

    "children": [
        {
            "id": 6,
            "name": "contact_form",
            "label": "Fill out registration form",
            "color": "#A3D2CE",
            "return_value": "contact_form",
            "size": child_node_size,
            "label_position": "right",
            "label_style": label_style_child,
        },
        {
            "id": 7,
            "name": "call",
            "label": "Call / Email from Sales Rep.",
            "color": "#A3D2CE",
            "return_value": "call",
            "size": child_node_size,
            "label_position": "right",
            "label_style": label_style_child,
        },
        {
            "id": 8,
            "name": "session",
            "label": "Fist discovery session",
            "color": "#A3D2CE",
            "return_value": "session",
            "size": child_node_size,
            "label_position": "right",
            "label_style": label_style_child,
        },
      
    ],
},
{
    "id": 11,
    "name":"Scoping_Contract",
    "label": "Scoping & Contract",
    "color": "#66B4AE",
    "icon": "fa fa-file-signature",
    "return_value": "Scoping_Contract",
    "size":main_node_size,
    "label_position": "top",
    "label_style": label_style_main,
    "expand_direction": "down",
        "icon_style": icon_style,

    "children": [
        {
            "id": 12,
            "name": "scoping",
            "label": "Scoping & POC",
            "color": "#66B4AE",
            "return_value": "scoping",
            "size": child_node_size,
            "label_position": "right",
            "label_style": label_style_child,
        },
        {
            "id": 13,
            "name": "offer",
            "label": "Preliminary offer",
            "color": "#66B4AE",
            "return_value": "offer",
            "size": child_node_size,
            "label_position": "right",
            "label_style": label_style_child,
        },
        {
            "id": 14,
            "name": "contract_review",
            "label": "Contract review & legal redlining",
            "color": "#66B4AE",
            "return_value": "contract_review",
            "size": child_node_size,
            "label_position": "right",
            "label_style": label_style_child,
        },
        {
            "id": 15,
            "name": "sign_contract",
            "label": "Contract signing",
            "color": "#66B4AE",
            "return_value": "sign_contract",
            "size": child_node_size,
            "label_position": "right",
            "label_style": label_style_child,
        },
        {
            "id": 16,
            "name": "providing_po",
            "label": "Providing PO for initial project",
            "color": "#66B4AE",
            "return_value": "providing_po",
            "size": child_node_size,
            "label_position": "right",
            "label_style": label_style_child,
        },
    ],
},

]
custom_css = """
body {
    margin: 10px;
    padding: 10px;
    border-radius: 10px;
    border: 1px solid #D3D3D3;
    box-shadow: 0 0 10px #D3D3D3;
    overflow: visible !important;
    }
}
"""

tooltipStyle = {
    "backgroundColor": "#f9f9f9",
    "color": "#333333",
    "border": "1px solid #d1d1d1",
    "padding": "8px 12px",
    "borderRadius": "10px",
    "fontSize": "14px",
    "fontWeight": "normal",
    "boxShadow": "3px 4px 10px rgba(0, 0, 0, 0.1)"
}

clicked_cj = st_customer_journey(input_data,key="cj", height=600, max_width = 1000, space_main_nodes = 130, space_between_child_nodes = 55,
                                 custom_css=custom_css, tooltipStyle=tooltipStyle,)


if clicked_cj == None:
    st.write("No node clicked")

else:
    st.write(f'Node clicked: {clicked_cj["node"]["label"]}')