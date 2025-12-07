### Creating Marimo UI Layouts

Source: https://github.com/marimo-team/marimo/blob/main/docs/_static/CLAUDE.md

Demonstrates how to arrange multiple UI elements within a marimo notebook. `mo.hstack()`, `mo.vstack()`, and `mo.tabs()` are provided for creating intuitive and organized layouts.

```python
# Create intuitive layouts with mo.hstack(), mo.vstack(), and mo.tabs()
```

--------------------------------

### Marimo Layout and Utility Functions

Source: https://github.com/marimo-team/marimo/blob/main/tests/_server/ai/snapshots/chat_system_prompts.txt

Describes Marimo functions for controlling layout and displaying various content types. Includes functions for stopping execution conditionally, displaying HTML and images, and arranging elements horizontally or vertically.

```python
# Layout and Utility Functions
mo.stop(predicate, output=None)
mo.Html(html)
mo.image(image)
mo.hstack(elements)
mo.vstack(elements)
mo.tabs(elements)
mo.mpl.interactive()
```

--------------------------------

### Python Layout Example: Horizontal Stack

Source: https://github.com/marimo-team/marimo/blob/main/tests/_server/ai/snapshots/chat_system_prompts.txt

Illustrates how to arrange multiple Marimo UI elements horizontally using the `mo.hstack` function. This is useful for creating compact and organized layouts, such as placing related controls side-by-side.

```python
import marimo as mo

# Create individual UI elements
input_field = mo.ui.text(label='Name:')
submit_button = mo.ui.button(label='Submit')

# Arrange them horizontally
mo.hstack([input_field, submit_button])
```

--------------------------------

### Marimo Layout and Utility Functions Reference

Source: https://github.com/marimo-team/marimo/blob/main/tests/_server/ai/snapshots/chat_system_prompts.txt

This section details layout and utility functions available in the marimo library. These functions assist in controlling execution flow, displaying various content types, and organizing UI elements. Dependencies may vary based on the function used (e.g., HTML, images).

```python
import marimo as mo
import matplotlib.pyplot as plt

# Stop execution conditionally
# mo.stop(predicate, output=None)

# Display HTML content
# mo.Html(html)

# Display an image
# mo.image(image)

# Stack elements horizontally
# mo.hstack(elements)

# Stack elements vertically
# mo.vstack(elements)

# Create a tabbed interface
# mo.tabs(elements)

# Make matplotlib plots interactive
# mo.mpl.interactive()
```

--------------------------------

### Layout Components: Stacks and Containers

Source: https://context7.com/marimo-team/marimo/llms.txt

Organize UI elements using Marimo's layout components. `mo.vstack` and `mo.hstack` create vertical and horizontal arrangements, respectively. `mo.center` centers content, `mo.tabs` organizes content into tabbed views, and `mo.accordion` provides collapsible sections.

```python
import marimo as mo

# Vertical stack
sidebar_content = mo.vstack([
    mo.md("## Controls"),
    mo.ui.slider(0, 100, label="Value 1"),
    mo.ui.slider(0, 100, label="Value 2"),
    mo.ui.button(label="Submit")
], gap=1.5, align="stretch")

# Horizontal stack
metrics_row = mo.hstack([
    mo.stat(label="Users", value=1234),
    mo.stat(label="Revenue", value="$56.7K"),
    mo.stat(label="Growth", value="+12.5%")
], gap=2, justify="space-between", widths="equal")

# Center content
mo.center(mo.md("# Welcome to Dashboard"))

# Tabs for organizing content
tabs = mo.tabs({
    "Overview": mo.md("Dashboard overview content"),
    "Analytics": mo.md("Analytics content"),
    "Settings": mo.md("Settings content")
})
tabs

# Accordion for collapsible sections
accordion = mo.accordion({
    "Section 1": mo.md("Content for section 1"),
    "Section 2": mo.md("Content for section 2"),
    "Section 3": mo.md("Content for section 3")
})
accordion
```

--------------------------------

### Marimo UI Controls for Layout

Source: https://github.com/marimo-team/marimo/blob/main/docs/api/layouts/stacks.md

Implements Marimo UI components for controlling stack layout properties. Includes dropdowns for 'justify' and 'align', a number input for 'gap', and a checkbox for 'wrap'.

```python
@app.cell
def __():
    justify = mo.ui.dropdown(
        ["start", "center", "end", "space-between", "space-around"],
        value="space-between",
        label="justify",
    )
    align = mo.ui.dropdown(
        ["start", "center", "end", "stretch"], value="center", label="align"
    )
    gap = mo.ui.number(start=0, step=0.25, stop=2, value=0.25, label="gap")
    wrap = mo.ui.checkbox(label="wrap")
    return
```

--------------------------------

### Creating Basic Layouts (Streamlit vs. Marimo)

Source: https://github.com/marimo-team/marimo/blob/main/docs/guides/coming_from/streamlit.md

Compares simple horizontal layout creation. Streamlit uses `st.columns` to define side-by-side containers. Marimo achieves a similar effect using `mo.hstack` which takes a list of elements to arrange horizontally.

```python
col1, col2 = st.columns(2)
with col1:
    st.write("Column 1")
with col2:
    st.write("Column 2")
```

```python
mo.hstack([
    mo.md("Column 1"),
    mo.md("Column 2")
])
```

--------------------------------

### Build a grid layout with Marimo vstack and hstack

Source: https://github.com/marimo-team/marimo/blob/main/tests/_utils/snapshots/docstring_complex.md

Shows how to construct a grid layout by nesting `hstack` (horizontal stacking) within `vstack` (vertical stacking). This allows for complex arrangements of UI elements, creating rows and columns.

```python
# Build a grid.
mo.vstack(
    [
        mo.hstack([mo.md("..."), mo.ui.text_area()]),
        mo.hstack([mo.ui.checkbox(), mo.ui.text(), mo.ui.date()]),
    ]
)
```

--------------------------------

### Marimo Layout and Utility Functions

Source: https://github.com/marimo-team/marimo/blob/main/tests/_server/ai/snapshots/chat_system_prompts.txt

Illustrates the use of Marimo's layout and utility functions for organizing UI elements and controlling execution flow. Functions like `mo.hstack`, `mo.vstack`, and `mo.tabs` enable the creation of structured interfaces, while `mo.stop` allows for conditional execution halting. `mo.Html` and `mo.image` are used for embedding custom content.

```python
import marimo as mo

# Example UI elements
button1 = mo.ui.button(label='Action 1')
button2 = mo.ui.button(label='Action 2')
text_area = mo.ui.text_area(label='Description')

# Horizontal stack
h_stack = mo.hstack([button1, button2])

# Vertical stack
v_stack = mo.vstack([h_stack, text_area])

# Tabbed interface
tabs = mo.tabs({
    "Input": v_stack,
    "Output": mo.ui.text(label='Results')
})

# Displaying the layout
mo.display(tabs)

# Conditional stop example
# mo.stop(predicate=lambda: text_area.value == '', output='Please provide a description.')
```

--------------------------------

### Marimo: Create Tabbed Interface (Layout)

Source: https://github.com/marimo-team/marimo/blob/main/tests/_server/ai/snapshots/chat_system_prompts.txt

Creates a tabbed interface from a list of Marimo UI elements. Each element will be placed in its own tab.

```python
import marimo as mo

elements = [mo.ui.text('Content Tab 1'), mo.ui.text('Content Tab 2')]
# Create a tabbed interface
# mo.tabs(elements)

```

--------------------------------

### Marimo UI Element: Array Layout

Source: https://github.com/marimo-team/marimo/blob/main/docs/_static/CLAUDE.md

Shows how to arrange multiple UI elements vertically in a list format within marimo using `mo.ui.array`. It takes a list of UI elements as input.

```python
mo.ui.array(elements: list[mo.ui.Element])
```

--------------------------------

### Layout Task Management UI Components (Python)

Source: https://github.com/marimo-team/marimo/blob/main/docs/guides/state.md

Arranges the previously defined UI components into a coherent layout for the task management application. It uses Marimo's `hstack` and `vstack` for horizontal and vertical arrangement, respectively, creating a user-friendly interface.

```python
inputs = mo.hstack(
    [task_entry_box, add_task_button, clear_tasks_button], justify="start"
)
mo.vstack([inputs, task_list])
```

--------------------------------

### Marimo: Stack Elements Horizontally

Source: https://github.com/marimo-team/marimo/blob/main/tests/_server/ai/snapshots/chat_system_prompts.txt

Arranges a list of Marimo UI elements horizontally. This is useful for creating side-by-side layouts.

```python
import marimo as mo

elements = [mo.ui.button('Left'), mo.ui.button('Right')]
# Stack elements horizontally
# mo.hstack(elements)

```

--------------------------------

### Marimo: Stack Elements Vertically

Source: https://github.com/marimo-team/marimo/blob/main/tests/_server/ai/snapshots/chat_system_prompts.txt

Arranges a list of Marimo UI elements vertically. This is the default layout behavior but can be explicitly used.

```python
import marimo as mo

elements = [mo.ui.text('First'), mo.ui.text('Second')]
# Stack elements vertically
# mo.vstack(elements)

```

--------------------------------

### Marimo UI Element: Tabs Layout

Source: https://github.com/marimo-team/marimo/blob/main/docs/_static/CLAUDE.md

Illustrates the creation of a tabbed interface for organizing UI elements in marimo. It accepts a dictionary where keys are tab titles and values are the UI elements to be placed in each tab.

```python
mo.ui.tabs(elements: dict[str, mo.ui.Element])
```

--------------------------------

### Python Layout Example: Vertical Stack

Source: https://github.com/marimo-team/marimo/blob/main/tests/_server/ai/snapshots/chat_system_prompts.txt

Demonstrates how to stack Marimo UI elements vertically using the `mo.vstack` function. This function is ideal for creating ordered lists of controls or content, ensuring they appear one after another in the notebook.

```python
import marimo as mo

# Create individual UI elements
header = mo.ui.text('Settings')
option1 = mo.ui.checkbox(label='Enable Feature A')
option2 = mo.ui.checkbox(label='Enable Feature B')

# Arrange them vertically
mo.vstack([header, option1, option2])
```

--------------------------------

### Sidebar Navigation for App Layouts

Source: https://context7.com/marimo-team/marimo/llms.txt

Implement sidebar navigation for creating app-like interfaces. The `mo.sidebar` function places content in a collapsible sidebar, suitable for controls, navigation, or supplementary information. A footer can also be added to the sidebar.

```python
import marimo as mo
import altair as alt
from vega_datasets import data

app = marimo.App(width="full")

@app.cell
def __(mo):
    # Create filters
    year = mo.ui.slider(start=1950, stop=2020, step=5, value=2000, label="Year")
    population = mo.ui.range_slider(
        start=0,
        stop=1000000000,
        value=[0, 500000000],
        label="Population"
    )
    return year, population

@app.cell
def __(mo, year, population):
    # Add sidebar with controls
    mo.sidebar([
        mo.md("# Gap Minder Dashboard"),
        mo.md("Explore global health and population data"),
        mo.vstack([
            year,
            mo.md(f"**Selected Year:** {year.value}"),
            population,
            mo.md(f"**Population Range:** {population.value[0]:,} - {population.value[1]:,}")
        ])
    ], footer=[
        mo.md("[GitHub](https://github.com/marimo-team/marimo)")
    ])
    return
```

--------------------------------

### Horizontal Stacking of Elements in Marimo

Source: https://github.com/marimo-team/marimo/blob/main/tests/_server/ai/snapshots/chat_system_prompts.txt

The `mo.hstack` function arranges multiple Marimo elements horizontally. This is useful for creating side-by-side layouts of UI components or visualizations.

```python
import marimo as mo

# Assuming element1 and element2 are valid Marimo elements (e.g., UI components, charts)
# element1 = mo.ui.slider(...)
# element2 = mo.ui.text(...)

# mo.hstack([element1, element2])
```

--------------------------------

### Vertical Stacking of Elements in Marimo

Source: https://github.com/marimo-team/marimo/blob/main/tests/_server/ai/snapshots/chat_system_prompts.txt

The `mo.vstack` function arranges multiple Marimo elements vertically. This is ideal for creating stacked layouts of UI components, text, or visualizations.

```python
import marimo as mo

# Assuming element1 and element2 are valid Marimo elements
# element1 = mo.ui.slider(...)
# element2 = mo.ui.text(...)

# mo.vstack([element1, element2])
```

--------------------------------

### Marimo Vertical Stack Layout

Source: https://github.com/marimo-team/marimo/blob/main/tests/_server/export/snapshots/notebook_with_outputs.ipynb.txt

This Marimo code snippet uses 'mo.vstack' to arrange multiple markdown elements vertically. It displays two lines of text, 'hello' and 'world', stacked on top of each other.

```python
mo.vstack([mo.md("hello"), mo.md("world")])
```

--------------------------------

### Marimo Horizontal and Vertical Stacks

Source: https://github.com/marimo-team/marimo/blob/main/docs/api/layouts/stacks.md

Demonstrates the usage of Marimo's `hstack` and `vstack` functions to arrange previously defined boxes. It dynamically applies layout properties controlled by the UI components defined in another cell.

```python
@app.cell
def __():
    horizontal = mo.hstack(
        boxes,
        align=align.value,
        justify=justify.value,
        gap=gap.value,
        wrap=wrap.value,
    )
    vertical = mo.vstack(
        boxes,
        align=align.value,
        gap=gap.value,
    )

    mo.vstack(
        [
            mo.hstack([justify, align, gap], justify="center"),
            horizontal,
            mo.md("-----------------------------"),
            vertical,
        ],
        align="stretch",
        gap=1,
    )
    return
```

--------------------------------

### Marimo UI Elements Overview

Source: https://github.com/marimo-team/marimo/blob/main/tests/_server/ai/snapshots/chat_system_prompts.txt

Lists available Marimo UI elements for creating interactive user interfaces. These include input controls, data display components, and layout elements. They can be imported and used directly within Marimo notebooks.

```python
# UI Elements
mo.ui.altair_chart(altair_chart)
mo.ui.button(value=None, kind='primary')
mo.ui.run_button(label=None, tooltip=None, kind='primary')
mo.ui.checkbox(label='', value=False)
mo.ui.chat(placeholder='', value=None)
mo.ui.date(value=None, label=None, full_width=False)
mo.ui.dropdown(options, value=None, label=None, full_width=False)
mo.ui.file(label='', multiple=False, full_width=False)
mo.ui.number(value=None, label=None, full_width=False)
mo.ui.radio(options, value=None, label=None, full_width=False)
mo.ui.refresh(options: List[str], default_interval: str)
mo.ui.slider(start, stop, value=None, label=None, full_width=False, step=None)
mo.ui.range_slider(start, stop, value=None, label=None, full_width=False, step=None)
mo.ui.table(data, columns=None, on_select=None, sortable=True, filterable=True)
mo.ui.text(value='', label=None, full_width=False)
mo.ui.text_area(value='', label=None, full_width=False)
mo.ui.data_explorer(df)
mo.ui.dataframe(df)
mo.ui.plotly(plotly_figure)
mo.ui.tabs(elements: dict[str, mo.ui.Element])
mo.ui.array(elements: list[mo.ui.Element])
mo.ui.form(element: mo.ui.Element, label='', bordered=True)
```

--------------------------------

### Marimo UI Elements Reference

Source: https://github.com/marimo-team/marimo/blob/main/tests/_server/ai/snapshots/chat_system_prompts.txt

Lists available Marimo UI elements for creating interactive interfaces. These elements include input widgets, display components, and layout structures. They are designed to work within Marimo's reactive programming model.

```python
import marimo as mo

# Charts
mo.ui.altair_chart(altair_chart)
mo.ui.plotly(plotly_figure)

# Input Widgets
mo.ui.button(value=None, kind='primary')
mo.ui.run_button(label=None, tooltip=None, kind='primary')
mo.ui.checkbox(label='', value=False)
mo.ui.chat(placeholder='', value=None)
mo.ui.date(value=None, label=None, full_width=False)
mo.ui.dropdown(options, value=None, label=None, full_width=False)
mo.ui.file(label='', multiple=False, full_width=False)
mo.ui.number(value=None, label=None, full_width=False)
mo.ui.radio(options, value=None, label=None, full_width=False)
mo.ui.slider(start, stop, value=None, label=None, full_width=False, step=None)
mo.ui.range_slider(start, stop, value=None, label=None, full_width=False, step=None)
mo.ui.text(value='', label=None, full_width=False)
mo.ui.text_area(value='', label=None, full_width=False)

# Data Display & Exploration
mo.ui.table(data, columns=None, on_select=None, sortable=True, filterable=True)
mo.ui.data_explorer(df)
mo.ui.dataframe(df)

# Layout and Structure
mo.ui.refresh(options: List[str], default_interval: str)
mo.ui.tabs(elements: dict[str, mo.ui.Element])
mo.ui.array(elements: list[mo.ui.Element])
mo.ui.form(element: mo.ui.Element, label='', bordered=True)

# Layout and Utility Functions
mo.stop(predicate, output=None)
mo.Html(html)
mo.image(image)
mo.hstack(elements)
mo.vstack(elements)
mo.tabs(elements)
mo.mpl.interactive()
```

--------------------------------

### First Cell in Multicolumn Mode in Markdown

Source: https://github.com/marimo-team/marimo/blob/main/marimo/_tutorials/markdown_format.md

Specifies the first cell in a column for Marimo's multicolumn layout within a Markdown notebook. The `column="1"` attribute is used.

```markdown
````md
```python {.marimo column="1"}
print("First cell in column 1")
```
````
```

--------------------------------

### Build a column of items with Marimo vstack

Source: https://github.com/marimo-team/marimo/blob/main/tests/_utils/snapshots/docstring_complex.md

Demonstrates how to stack Marimo UI elements vertically using the `vstack` function. This is useful for creating simple vertical layouts. It takes a list of Marimo objects as input.

```python
# Build a column of items
mo.vstack([mo.md("..."), mo.ui.text_area()])
```

--------------------------------

### Create Dynamic Boxes with Marimo

Source: https://github.com/marimo-team/marimo/blob/main/docs/api/layouts/stacks.md

Defines a Python function to generate HTML divs with dynamic sizing and styling, used for demonstration within Marimo layouts. It takes an integer argument to control the box size.

```python
@app.cell
def __():
    def create_box(num=1):
        box_size = 30 + num * 10
        return mo.Html(
            f"<div style='min-width: {box_size}px; min-height: {box_size}px; background-color: orange; text-align: center; line-height: {box_size}px'>{str(num)}</div>"
        )




    boxes = [create_box(i) for i in range(1, 5)]
    return
```

--------------------------------

### VStack Function

Source: https://github.com/marimo-team/marimo/blob/main/tests/_utils/snapshots/docstring_complex.md

Stacks UI elements vertically. This function is essential for creating column-based layouts in Marimo applications.

```APIDOC
## `mo.vstack`

### Description
Stacks UI elements vertically in a column. This is useful for organizing elements one below the other. It can be combined with `hstack` to create grid-like layouts.

### Method
Function call

### Endpoint
N/A (Client-side function)

### Parameters
#### Path Parameters
N/A

#### Query Parameters
N/A

#### Request Body
- **items** (Sequence[object]) - Required - A list of Marimo UI elements or markdown objects to stack.
- **align** (Literal["start", "end", "center", "stretch"], optional) - Controls the horizontal alignment of items within the vstack. Defaults to "start".
- **justify** (Literal["start", "center", "end", "space-between", "space-around"], optional) - Controls the vertical justification of items. Defaults to "start".
- **gap** (float, optional) - The spacing between stacked items, specified in `rem` units. Defaults to 0.5.
- **heights** (Union[Literal["equal"], Sequence[float]], optional) - Determines the height distribution of items. Can be "equal" for uniform heights, a list of relative heights (e.g., [1, 2]), or None for default behavior.
- **custom_css** (dict[str, str], optional) - A dictionary to apply custom CSS styles to each column element. Supported keys include `width`, `height`, `background_color`, `border`, `border_radius`, and `padding`.
- **typeless** () - Used to pass unknown types to the underlying stack implementation.
- **code_block** (str) - Renders a code block within the stack. Example: `mo.vstack(), mo.hstack()`.
- **second_code_block** (str) - Renders a second code block within the stack. Example: `mo.vstack([])`.
- ***args** () - Positional arguments passed to the stack function.
- ****kwargs** () - Keyword arguments passed to the stack function.

### Request Example
```python
import marimo as mo

# Example 1: Simple column of text and input
layout1 = mo.vstack([
    mo.md("# Title\nThis is a description."),
    mo.ui.text_area("Enter text:")
])

# Example 2: Grid layout using vstack and hstack
layout2 = mo.vstack([
    mo.hstack([mo.md("Left Column"), mo.ui.text_area("Input 1")]),
    mo.hstack([mo.ui.checkbox("Option A"), mo.ui.text("Input 2"), mo.ui.date("Date")])
], gap=1.0, align="center")
```

### Response
#### Success Response (200)
- **Html** (Html) - Returns an `Html` object representing the stacked UI elements, ready to be rendered in the Marimo interface.

#### Response Example
(The actual HTML output is complex and dynamically generated based on the input items and parameters. It represents the rendered UI layout.)
```html
<!-- This is a conceptual representation of the returned HTML structure -->
<div class="marimo-vstack" style="display: flex; flex-direction: column; align-items: start; justify-content: start; gap: 0.5rem;">
  <!-- Rendered content of the first item -->
  <div>...</div>
  <!-- Rendered content of the second item -->
  <div>...</div>
</div>
```
```

--------------------------------

### Render a basic Switch with a Label

Source: https://github.com/marimo-team/marimo/blob/main/frontend/src/stories/switch.mdx

Demonstrates how to render a standard Switch component alongside a Label. It requires importing Label and Switch components and uses Tailwind CSS classes for layout. The Switch is linked to the Label via the 'htmlFor' attribute.

```jsx
import { Label } from "@/components/ui/label";
import { Switch } from "@/components/ui/switch";

<div className="flex items-center align-middle space-x-2">
  <Switch id="airplane-mode" />
  <Label htmlFor="airplane-mode">Airplane Mode</Label>
</div>
```

--------------------------------

### Import Marimo Library in Python

Source: https://github.com/marimo-team/marimo/blob/main/docs/getting_started/key_concepts.md

This line imports the marimo library, which is essential for utilizing Marimo's interactive UI elements, layout components, and dynamic markdown features within a notebook.

```python
import marimo as mo
```

--------------------------------

### Render a small Switch with a Label

Source: https://github.com/marimo-team/marimo/blob/main/frontend/src/stories/switch.mdx

Illustrates the creation of a smaller variant of the Switch component, paired with a Label. This example highlights the 'size' prop for customization and uses similar import and layout conventions as the basic Switch example.

```jsx
import { Label } from "@/components/ui/label";
import { Switch } from "@/components/ui/switch";

<div className="flex items-center align-middle space-x-2">
  <Switch id="airplane-mode" size="sm" />
  <Label htmlFor="airplane-mode">Small Switch</Label>
</div>
```

--------------------------------

### Create Marimo Sidebar Navigation

Source: https://github.com/marimo-team/marimo/blob/main/docs/api/layouts/routes.md

Configures a vertical sidebar with markdown titles, a navigation menu, and external links. This function requires the marimo library.

```python
mo.sidebar(
    [
        mo.md("# marimo"),
        mo.nav_menu(
            {
                "#/": f"{mo.icon('lucide:home')} Home",
                "#/about": f"{mo.icon('lucide:user')} About",
                "#/contact": f"{mo.icon('lucide:phone')} Contact",
                "Links": {
                    "https://twitter.com/marimo_io": "Twitter",
                    "https://github.com/marimo-team/marimo": "GitHub",
                },
            },
            orientation="vertical",
        ),
    ]
)
return
```

--------------------------------

### Marimo UI: Create a Text Area Input

Source: https://github.com/marimo-team/marimo/blob/main/tests/_server/ai/snapshots/chat_system_prompts.txt

Creates a multi-line text input field for larger text entries. Supports labels and full-width display.

```python
import marimo as mo

# Create a text area input with a default value
# mo.ui.text_area(value='Enter multiple lines of text', label='Description')

```

--------------------------------

### Marimo UI Element: Form

Source: https://github.com/marimo-team/marimo/blob/main/docs/_static/CLAUDE.md

Demonstrates the creation of a form-like structure in marimo to group and manage UI elements. It takes a single UI element (which can be a composite like `hstack` or `vstack`) and allows for a label and border styling.

```python
mo.ui.form(element: mo.ui.Element, label='', bordered=True)
```

--------------------------------

### Marimo CSS Variables for Theming (CSS)

Source: https://github.com/marimo-team/marimo/blob/main/docs/guides/configuration/theming.md

This CSS snippet lists the officially supported CSS variables for Marimo theming. These variables control fundamental aspects of the notebook's appearance, such as monospace font, text font, and heading font. Modifying these variables provides a structured way to customize the notebook's look and feel.

```css
--marimo-monospace-font
--marimo-text-font
--marimo-heading-font
```

--------------------------------

### Marimo UI Element: Text Area

Source: https://github.com/marimo-team/marimo/blob/main/docs/_static/CLAUDE.md

Demonstrates the implementation of a multi-line text input area in marimo. It supports default text, a label, and width control.

```python
mo.ui.text_area(value='', label=None, full_width=False)
```

--------------------------------

### Create Sidebar with Navigation Menu (Python)

Source: https://github.com/marimo-team/marimo/blob/main/docs/api/layouts/sidebar.md

Demonstrates how to define a sidebar in a Marimo application. It includes markdown for a title and a navigation menu with nested links and icons. This function returns nothing but modifies the UI.

```python
import marimo as mo

@app.cell
def __():
    mo.sidebar(
        [
            mo.md("# marimo"),
            mo.nav_menu(
                {
                    "#/home": f"{mo.icon('lucide:home')} Home",
                    "#/about": f"{mo.icon('lucide:user')} About",
                    "#/contact": f"{mo.icon('lucide:phone')} Contact",
                    "Links": {
                        "https://twitter.com/marimo_io": "Twitter",
                        "https://github.com/marimo-team/marimo": "GitHub",
                    },
                },
                orientation="vertical",
            ),
        ]
    )
    return
```

--------------------------------

### Create Tabbed Interfaces in Marimo

Source: https://github.com/marimo-team/marimo/blob/main/tests/_server/ai/snapshots/chat_system_prompts.txt

The `mo.tabs` function allows you to organize Marimo elements into a tabbed interface. Each element in the provided list will be displayed as a separate tab.

```python
import marimo as mo

# Assuming tab1_content and tab2_content are valid Marimo elements
# tab1_content = mo.ui.text("Content for tab 1")
# tab2_content = mo.ui.table(...) 

# mo.tabs({"Tab 1": tab1_content, "Tab 2": tab2_content})
```

--------------------------------

### Marimo UI: Create a Tabbed Interface

Source: https://github.com/marimo-team/marimo/blob/main/tests/_server/ai/snapshots/chat_system_prompts.txt

Creates a tabbed interface from a dictionary of UI elements. Each key-value pair in the dictionary represents a tab title and its corresponding content.

```python
import marimo as mo

# Example elements for tabs
element1 = mo.ui.text('Content for Tab 1')
element2 = mo.ui.number(5, 'Content for Tab 2')

# Create a dictionary of elements
ui_elements = {'Tab 1': element1, 'Tab 2': element2}

# Create the tabbed interface
# mo.ui.tabs(ui_elements)

```

--------------------------------

### Configure marimo-snippets Rendering Behavior Per-Element

Source: https://github.com/marimo-team/marimo/blob/main/docs/guides/publishing/from_code_snippets.md

This snippet illustrates how to configure marimo snippets on an individual element basis using data attributes. This allows for fine-grained control over specific embedded notebooks, such as setting a custom height or disabling code display. The configuration is applied directly to the `<marimo-iframe>` tag.

```html
<marimo-iframe data-height="600px" data-show-code="false">
...
</marimo-iframe>
```

--------------------------------

### Create and Display Marimo Stat Components (Python)

Source: https://github.com/marimo-team/marimo/blob/main/docs/api/layouts/stat.md

Demonstrates how to create and display multiple 'stat' components using the marimo library in Python. It shows how to define value, label, caption, and direction for each stat, and then arrange them horizontally.

```python
@app.cell
def __():
    active_users = mo.stat(
        value="1.2M", 
        label="Active Users", 
        caption="12k from last month", 
        direction="increase"
    )

    revenue = mo.stat(
        value="$4.5M", 
        label="Revenue", 
        caption="8k from last quarter", 
        direction="increase"
    )
    
    conversion = mo.stat(
        value="3.8", 
        label="Conversion Rate", 
        caption="0.5 from last week", 
        direction="decrease",
    )
    
    mo.hstack([active_users, revenue, conversion], justify="center", gap="2rem")
    return
```

--------------------------------

### Example CLAUDE.md File Structure

Source: https://github.com/marimo-team/marimo/blob/main/docs/guides/generate_with_ai/prompts.md

This is an example structure for a CLAUDE.md file, intended to guide Claude in editing marimo notebooks. It serves as a starting point for custom configurations.

```markdown
--8<-- "docs/_static/CLAUDE.md"
```

--------------------------------

### Basic Marimo Cell Structure

Source: https://github.com/marimo-team/marimo/blob/main/docs/_static/CLAUDE.md

Illustrates the fundamental structure of a marimo notebook cell using the `@app.cell` decorator. Edits should be confined within this decorator, with marimo managing parameter and return statements automatically.

```python
@app.cell
def _():
    <your code here>
    return
```

--------------------------------

### Marimo UI: Create a Text Input

Source: https://github.com/marimo-team/marimo/blob/main/tests/_server/ai/snapshots/chat_system_prompts.txt

Creates a single-line text input field for user input. Supports labels and full-width display.

```python
import marimo as mo

# Create a text input with a placeholder value
# mo.ui.text(value='Default text', label='Enter text')

```

--------------------------------

### Configure marimo-snippets Rendering Behavior Globally

Source: https://github.com/marimo-team/marimo/blob/main/docs/guides/publishing/from_code_snippets.md

This example shows how to globally configure the rendering behavior of marimo snippets, such as setting default heights for iframes or customizing button titles. The configuration script must be placed before the main marimo-snippets script is loaded. It takes configuration objects as input to modify default settings.

```html
<!-- Optionally configure how buttons and iframes are rendered. -->
<!-- Configuration must come _before_ the main extractor script is loaded. -->
<script type="text/x-marimo-snippets-config">
configureMarimoButtons({title: "Open in a marimo notebook"});
configureMarimoIframes({height: "400px"});
</script>

<script src="https://cdn.jsdelivr.net/npm/@marimo-team/marimo-snippets@1"></script>
```

--------------------------------

### Marimo UI: Create an Array of UI Elements

Source: https://github.com/marimo-team/marimo/blob/main/tests/_server/ai/snapshots/chat_system_prompts.txt

Creates an array (vertical stack) of UI elements. This allows for arranging multiple UI components sequentially.

```python
import marimo as mo

# Create a list of UI elements
elements_list = [mo.ui.text('First element'), mo.ui.button('Click Me')]

# Create an array of these elements
# mo.ui.array(elements_list)

```

--------------------------------

### Marimo UI: Wrap Element in a Form

Source: https://github.com/marimo-team/marimo/blob/main/tests/_server/ai/snapshots/chat_system_prompts.txt

Wraps a given UI element within a form. This can be used for input validation or submission logic. Supports custom labels and borders.

```python
import marimo as mo

input_element = mo.ui.text('Input field')
# Wrap the input element in a form
# mo.ui.form(input_element, label='User Input Form')

```

--------------------------------

### Vega-Lite Bar Chart Configuration

Source: https://github.com/marimo-team/marimo/blob/main/tests/_data/snapshots/charts_json.txt

This configuration defines a Vega-Lite bar chart. It includes data transformations for aggregation, ranking, and percentage calculation, and specifies encoding for axes, tooltips, and text labels. The chart displays counts and percentages of 'some_column'.

```json
{
  "$schema": "https://vega.github.io/schema/vega-lite/v6.1.0.json",
  "config": {
    "axis": {
      "grid": false
    },
    "view": {
      "continuousHeight": 300,
      "continuousWidth": 300,
      "stroke": null
    }
  },
  "data": {
    "name": "data-afce120bec1de31b50bc39eae2fedbed"
  },
  "datasets": {
    "data-afce120bec1de31b50bc39eae2fedbed": [
      {
        "some_column": 1
      },
      {
        "some_column": 2
      },
      {
        "some_column": 3
      }
    ]
  },
  "layer": [
    {
      "encoding": {
        "tooltip": [
          {
            "field": "some_column",
            "type": "nominal"
          },
          {
            "field": "count",
            "format": ",.0f",
            "title": "Number of records",
            "type": "quantitative"
          }
        ],
        "x": {
          "field": "count",
          "title": "Number of records",
          "type": "quantitative"
        },
        "y": {
          "axis": {
            "title": null
          },
          "field": "some_column",
          "sort": "-x",
          "type": "nominal"
        }
      },
      "mark": {
        "color": "#8ec8f6",
        "type": "bar"
      },
      "transform": [
        {
          "aggregate": [
            {
              "as": "count",
              "op": "count"
            }
          ],
          "groupby": [
            "some_column"
          ]
        },
        {
          "sort": [
            {
              "field": "count",
              "order": "descending"
            },
            {
              "field": "some_column",
              "order": "ascending"
            }
          ],
          "window": [
            {
              "as": "rank",
              "field": "",
              "op": "rank"
            }
          ]
        },
        {
          "joinaggregate": [
            {
              "as": "total_count",
              "field": "count",
              "op": "sum"
            }
          ]
        },
        {
          "as": "percentage",
          "calculate": "datum.count / datum.total_count"
        }
      ]
    },
    {
      "encoding": {
        "text": {
          "field": "percentage",
          "format": ".2%",
          "type": "quantitative"
        },
        "tooltip": [
          {
            "field": "some_column",
            "type": "nominal"
          },
          {
            "field": "count",
            "format": ",.0f",
            "title": "Number of records",
            "type": "quantitative"
          }
        ],
        "x": {
          "field": "count",
          "title": "Number of records",
          "type": "quantitative"
        },
        "y": {
          "axis": {
            "title": null
          },
          "field": "some_column",
          "sort": "-x",
          "type": "nominal"
        }
      },
      "mark": {
        "align": "left",
        "color": "black",
        "dx": 3,
        "type": "text"
      },
      "transform": [
        {
          "aggregate": [
            {
              "as": "count",
              "op": "count"
            }
          ],
          "groupby": [
            "some_column"
          ]
        },
        {
          "sort": [
            {
              "field": "count",
              "order": "descending"
            },
            {
              "field": "some_column",
              "order": "ascending"
            }
          ],
          "window": [
            {
              "as": "rank",
              "field": "",
              "op": "rank"
            }
          ]
        },
        {
          "joinaggregate": [
            {
              "as": "total_count",
              "field": "count",
              "op": "sum"
            }
          ]
        },
        {
          "as": "percentage",
          "calculate": "datum.count / datum.total_count"
        }
      ]
    }
  ],
  "title": "some_column",
  "width": "container"
}
```

--------------------------------

### Python: Chat UI with Templated Prompts

Source: https://github.com/marimo-team/marimo/blob/main/docs/api/inputs/chat.md

Demonstrates using templated prompts with the Marimo chat UI. Users can select from predefined prompts, and variables within these prompts (e.g., '{{country}}') will generate dynamic input fields for the user.

```python
import marimo as mo

mo.ui.chat(
    mo.ai.llm.openai("gpt-4o"),
    prompts=[
        "What is the capital of France?",
        "What is the capital of Germany?",
        "What is the capital of {{country}}?",
    ],
)
```

--------------------------------

### Project-Level Theming with TOML (TOML)

Source: https://github.com/marimo-team/marimo/blob/main/docs/guides/configuration/theming.md

This TOML snippet shows how to configure custom CSS files at the project level using `pyproject.toml`. The `custom_css` field within the `[tool.marimo.display]` section allows you to specify one or more CSS files that will be applied to all notebooks within the project. This theme is local to the project and not shared when notebooks are distributed.

```toml
[tool.marimo.display]
custom_css = ["additional.css"]
```

--------------------------------

### Embed a blank marimo notebook using HTML iframe

Source: https://github.com/marimo-team/marimo/blob/main/docs/guides/publishing/playground.md

This HTML snippet embeds a blank marimo notebook into a web page, serving as an interactive code playground for users. It utilizes an iframe with specific source URL parameters to control the embedding behavior, such as hiding the chrome interface. The `sandbox` attribute is crucial for security, allowing only necessary scripts to run.

```html
<iframe
  src="https://marimo.app/l/aojjhb?embed=true&show-chrome=false"
  width="100%"
  height="500"
  frameborder="0"
  sandbox="allow-scripts"
></iframe>
```

--------------------------------

### Example Usage of TabContainer Component

Source: https://github.com/marimo-team/marimo/blob/main/frontend/src/components/data-table/charts/README.md

Demonstrates the usage of the TabContainer component, which includes TabsContent for different sections like 'data' and 'style'. It shows how to nest FormSection and FieldSection within the 'data' tab and how to include a StyleForm in the 'style' tab.

```jsx
<TabContainer>
    <TabsContent value="data">
        <FormSection>
            <FieldSection>
            </FieldSection>
        </FormSection>
    </TabsContent>
    <TabsContent value="style">
        <StyleForm />
    </TabsContent>
</TabContainer>
```

--------------------------------

### Configure Marimo Application Routes

Source: https://github.com/marimo-team/marimo/blob/main/docs/api/layouts/routes.md

Sets up routing for a Marimo application, mapping URL paths to markdown content. It includes a catch-all route for undefined paths. Requires the marimo library.

```python
mo.routes({
    "#/": mo.md("# Home"),
    "#/about": mo.md("# About"),
    "#/contact": mo.md("# Contact"),
    mo.routes.CATCH_ALL: mo.md("# Home"),
})
return
```

--------------------------------

### LZ-compress marimo notebook code for embedding with URL hash

Source: https://github.com/marimo-team/marimo/blob/main/docs/guides/publishing/playground.md

This JavaScript code demonstrates how to embed large marimo notebooks by using LZ-string compression and a URL hash. It imports the `compressToEncodedURIComponent` function from the `lz-string` package to compress the notebook code and formats it into a URL suitable for embedding. This approach overcomes the URL length limitations associated with directly embedding code.

```javascript
import { compressToEncodedURIComponent } from "lz-string";

const url = `https://marimo.app/#code/${compressToEncodedURIComponent(code)}`
```

--------------------------------

### Markdown Details and Admonitions - Marimo

Source: https://github.com/marimo-team/marimo/blob/main/docs/guides/outputs.md

Illustrates the use of custom markdown syntax for creating expandable details sections and highlighted admonition blocks. These extensions enhance the presentation of information within markdown cells. The `///` syntax denotes these special blocks.

```markdown
/// details | Heads up

Here's some additional context.
///
```

```markdown
/// attention | This is important.

Pay attention to this text!
///
```

--------------------------------

### Marimo UI: Create an Interactive Table

Source: https://github.com/marimo-team/marimo/blob/main/tests/_server/ai/snapshots/chat_system_prompts.txt

Creates an interactive table to display data. Supports sorting, filtering, and row selection. Accepts data and column definitions.

```python
import marimo as mo
import polars as pl

data = pl.DataFrame({"col1": [1, 2], "col2": [3, 4]})
# Create an interactive table
# mo.ui.table(data, columns=['col1', 'col2'])

```

--------------------------------

### Marimo UI Element: Text Input

Source: https://github.com/marimo-team/marimo/blob/main/docs/_static/CLAUDE.md

Shows the creation of a single-line text input field in marimo. It allows for default text, a label, and width control.

```python
mo.ui.text(value='', label=None, full_width=False)
```

--------------------------------

### Create a Form with Multiple UI Elements (Python)

Source: https://github.com/marimo-team/marimo/blob/main/docs/recipes.md

Shows how to create an interactive form using `mo.md` and `.batch()` with various UI elements like sliders and number inputs. The `.form()` method converts the markdown structure into a submitable form. The `.value` attribute of the form object retrieves the submitted values as a dictionary.

```python
import marimo as mo

form = mo.md(
   r"""
   Choose your algorithm parameters:

   - $\epsilon$: {epsilon}
   - $\delta$: {delta}
   """).batch(epsilon=mo.ui.slider(0.1, 1, step=0.1), delta=mo.ui.number(1, 10)).form()
form

# Get the submitted form value.
form.value
```

--------------------------------

### Marimo UI Element: DataFrame Display

Source: https://github.com/marimo-team/marimo/blob/main/docs/_static/CLAUDE.md

Shows the direct display of a DataFrame as a table using the `mo.ui.dataframe` element in marimo. This is a straightforward way to present tabular data.

```python
mo.ui.dataframe(df)
```

--------------------------------

### Vega-Lite Bar Chart with Percentage Labels (JSON)

Source: https://github.com/marimo-team/marimo/blob/main/tests/_data/snapshots/column_preview_str_chart_spec.txt

This JSON object defines a Vega-Lite visualization. It specifies data loading from a base64 encoded CSV, applies transformations for aggregation and percentage calculation, and configures both bar marks and text marks for displaying data. The chart shows the count and percentage for categories in field 'B'.

```JSON
{
  "$schema": "https://vega.github.io/schema/vega-lite/v6.1.0.json",
  "config": {
    "axis": {
      "grid": false
    },
    "view": {
      "continuousHeight": 300,
      "continuousWidth": 300,
      "stroke": null
    }
  },
  "data": {
    "format": {
      "type": "csv"
    },
    "url": "data:text/csv;base64,QgphCmEKYQo="
  },
  "layer": [
    {
      "encoding": {
        "tooltip": [
          {
            "field": "B",
            "type": "nominal"
          },
          {
            "field": "count",
            "format": ",.0f",
            "title": "Number of records",
            "type": "quantitative"
          }
        ],
        "x": {
          "field": "count",
          "title": "Number of records",
          "type": "quantitative"
        },
        "y": {
          "axis": {
            "title": null
          },
          "field": "B",
          "sort": "-x",
          "type": "nominal"
        }
      },
      "mark": {
        "color": "#8ec8f6",
        "type": "bar"
      },
      "transform": [
        {
          "aggregate": [
            {
              "as": "count",
              "op": "count"
            }
          ],
          "groupby": [
            "B"
          ]
        },
        {
          "sort": [
            {
              "field": "count",
              "order": "descending"
            },
            {
              "field": "B",
              "order": "ascending"
            }
          ],
          "window": [
            {
              "as": "rank",
              "field": "",
              "op": "rank"
            }
          ]
        },
        {
          "joinaggregate": [
            {
              "as": "total_count",
              "field": "count",
              "op": "sum"
            }
          ]
        },
        {
          "as": "percentage",
          "calculate": "datum.count / datum.total_count"
        }
      ]
    },
    {
      "encoding": {
        "text": {
          "field": "percentage",
          "format": ".2%",
          "type": "quantitative"
        },
        "tooltip": [
          {
            "field": "B",
            "type": "nominal"
          },
          {
            "field": "count",
            "format": ",.0f",
            "title": "Number of records",
            "type": "quantitative"
          }
        ],
        "x": {
          "field": "count",
          "title": "Number of records",
          "type": "quantitative"
        },
        "y": {
          "axis": {
            "title": null
          },
          "field": "B",
          "sort": "-x",
          "type": "nominal"
        }
      },
      "mark": {
        "align": "left",
        "color": "black",
        "dx": 3,
        "type": "text"
      },
      "transform": [
        {
          "aggregate": [
            {
              "as": "count",
              "op": "count"
            }
          ],
          "groupby": [
            "B"
          ]
        },
        {
          "sort": [
            {
              "field": "count",
              "order": "descending"
            },
            {
              "field": "B",
              "order": "ascending"
            }
          ],
          "window": [
            {
              "as": "rank",
              "field": "",
              "op": "rank"
            }
          ]
        },
        {
          "joinaggregate": [
            {
              "as": "total_count",
              "field": "count",
              "op": "sum"
            }
          ]
        },
        {
          "as": "percentage",
          "calculate": "datum.count / datum.total_count"
        }
      ]
    }
  ],
  "title": "B",
  "width": "container"
}
```

--------------------------------

### Python: Marimo Accordion for Explanations

Source: https://github.com/marimo-team/marimo/blob/main/tests/_convert/snapshots/dataflow.md.txt

This snippet demonstrates using `mo.accordion` to present collapsible explanations within a Marimo notebook, useful for providing context or advanced tips without cluttering the main view.

```python
mo.accordion(
    {
        "Why not track attributes?": ""
        marimo can't reliably trace attributes 
        to cells that define them. For example, attributes are routinely 
        created or modified by library code.
        ""
    }
)
```

```python
mo.accordion(
    {
        "Tip (advanced): mutable state": (
            """
        You can use the fact that marimo does not track attributes or 
        mutations to implement mutable state in marimo. An example of
        this is shown in the `ui` tutorial.
        """
        )
    }
)
```

```python
mo.accordion(tips)
```

--------------------------------

### Python UI Element Examples: Slider, Text Input, and Button

Source: https://github.com/marimo-team/marimo/blob/main/tests/_server/ai/snapshots/chat_system_prompts.txt

Demonstrates the creation and basic usage of Marimo UI elements including a slider, a text input field, and a button. These elements are fundamental for building interactive notebooks. The `.value` attribute is used to access their current states. Note that UI elements cannot be accessed in the same cell where they are defined.

```python
import marimo as mo

# Create a slider with a range from 0 to 100
my_slider = mo.ui.slider(0, 100, label='Select a value:')

# Create a text input field
my_text = mo.ui.text(label='Enter some text:')

# Create a button
my_button = mo.ui.button(label='Click Me', on_click=lambda:
    print(f'Slider value: {my_slider.value}, Text: {my_text.value}')
)

# Display the UI elements
mo.hstack([my_slider, my_text, my_button])
```

--------------------------------

### Python Utility Example: Display HTML

Source: https://github.com/marimo-team/marimo/blob/main/tests/_server/ai/snapshots/chat_system_prompts.txt

Shows how to render raw HTML content within a Marimo notebook using the `mo.Html` function. This allows for the embedding of custom HTML structures, including text formatting, links, and other elements not directly supported by Marimo's standard UI components.

```python
import marimo as mo

# HTML content to display
html_content = """
<h1>Welcome to Marimo!</h1>
<p>This is a paragraph rendered using <strong>HTML</strong>.</p>
<a href="https://marimo.readthedocs.io/">Marimo Docs</a>
"""

# Display the HTML
mo.Html(html_content)
```

--------------------------------

### Render Markdown with Indented Code Block and F-string

Source: https://github.com/marimo-team/marimo/blob/main/tests/_convert/snapshots/unsafe-app.md.txt

Renders markdown with an indented code block that also utilizes an f-string for dynamic output, showcasing advanced formatting and interpolation.

```python
mo.md(f"""
    Not markdown
    ```python {{.marimo}}
    print("1 + 1 = {1 + 1}")
    ```
""")
```
