import os
import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from tqdm import tqdm
import plotly.graph_objects as go
import matplotlib.patches as patches
from matplotlib.transforms import Bbox
import random


# === SETTINGS === #
IMG_WIDTH = 1200
IMG_HEIGHT = 900
NUM_IMAGES_PER_TYPE = 2000
OUTPUT_DIR = "/content/drive/MyDrive/Learning/stanford/Natural Language Understanding/project/synthetic_data"
IMAGES_DIR = os.path.join(OUTPUT_DIR, "images")
ANNOT_PATH = os.path.join(OUTPUT_DIR, "annotations", "instances.json")
CLASSES_PATH = os.path.join(OUTPUT_DIR, "classes.txt")
image_id = 0
annotation_id = 0
available_colors = ["red", "blue", "green", "yellow", "purple", "orange", "cyan"]


# === CLASSES === #
ALL_CLASSES = [
    "title", "subtitle", "legend", "x-axis", "y-axis", "gridlines",
    "tick-labels", "tick-marks", "chart-body", "data-labels", "bar", "bar-value",
    "stacked-bar", "line", "area", "line-point", "line-value", "scatter-point",
    "axis-label", "scatter-value", "slice", "slice-label", "slice-value", "bin",
    "bin-edge", "bin-frequency", "radar-axis", "radar-point", "radar-line",
    "heatmap-cell", "heatmap-color-bar", "table-header", "table-cell",
    "table-row", "table-column", "annotation", "reference-line", "trendline",
    "error-bars", "watermark", "axis-title", "legend-item","violin",
]

# === GLOBAL COCO STRUCTURE === #
coco_output = {
    "images": [],
    "annotations": [],
    "categories": []
}
annotation_id = 1
class_names = []
# IMAGE_DIR = "generated_charts"
# os.makedirs(IMAGE_DIR, exist_ok=True)
# === UTILITIES === #
def save_classes():
    with open(CLASSES_PATH, "w") as f:
        f.write("\n".join(ALL_CLASSES))
    print(f"[✓] Created {CLASSES_PATH}")

# def get_bbox_from_patch(patch):
#     """Given a Matplotlib patch (e.g., a rectangle or bar), return its bounding box."""
#     bbox = patch.get_bbox()  # This gets the bounding box of the patch
#     return [bbox.x0, bbox.y0, bbox.width, bbox.height]

def get_bbox_from_patch(patch, renderer):
    """Return a bounding box [x, y, width, height] for a matplotlib visual element."""
    if hasattr(patch, 'get_window_extent'):
        bbox = patch.get_window_extent(renderer)
        return [float(bbox.x0), float(bbox.y0), float(bbox.width), float(bbox.height)]
    else:
        # If it doesn't have get_window_extent (like some custom elements), return a dummy box
        return [0, 0, 0, 0]

def get_bbox_from_axes(ax):
    """Given a Matplotlib Axes object, return the bounding box of the entire axes."""
    bbox = ax.get_position()  # This returns the bounding box of the axes (normalized coordinates)
    return [bbox.x0, bbox.y0, bbox.width, bbox.height]

def get_bbox_from_text(text, renderer):
    """Given a Matplotlib text object and a renderer, return the bounding box of the text."""
    bbox = text.get_window_extent(renderer=renderer)
    return [bbox.x0, bbox.y0, bbox.width, bbox.height]



def get_bbox_from_line(line):
    """Given a Matplotlib line (like a spine or axis line), return its bounding box."""
    bbox = line.get_path().get_extents()
    return [bbox.x0, bbox.y0, bbox.width, bbox.height]

def load_classes():
    global class_names
    with open(CLASSES_PATH, "r") as f:
        class_names = [line.strip() for line in f.readlines()]
    coco_output["categories"] = [{"id": i + 1, "name": name} for i, name in enumerate(class_names)]

def class_id(name):
    return class_names.index(name) + 1 if name in class_names else None

def get_bbox(artist, renderer):
    bbox = artist.get_window_extent(renderer=renderer)
    return [bbox.x0, IMG_HEIGHT - bbox.y1, bbox.width, bbox.height]

def flip_y(bbox):
    x, y, w, h = bbox
    flipped_y = IMG_HEIGHT - (y + h)
    # flipped_y=h
    return [x, flipped_y, w, h]

# def get_bbox_from_patch(patch):
#     path = patch.get_path()
#     transform = patch.get_transform()
#     transformed_path = transform.transform_path(path)
#     return transformed_path.get_extents()


def add_annotation(image_id, category_name, bbox):
    global annotation_id
    if class_id(category_name) is None:
        return
    coco_output["annotations"].append({
        "id": annotation_id,
        "image_id": image_id,
        "category_id": class_id(category_name),
        "bbox": [float(b) for b in bbox],
        "area": float(bbox[2] * bbox[3]),
        "iscrowd": 0
    })
    annotation_id += 1




# === CHART GENERATOR FUNCTIONS === #

# Generate Bar Chart
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import random

def generate_bar_chart(num_categories, bar_color):
    global image_id

    fig, ax = plt.subplots(figsize=(IMG_WIDTH / 100, IMG_HEIGHT / 100), dpi=100)
    canvas = FigureCanvas(fig)

    categories = [chr(65 + i) for i in range(num_categories)]
    values = np.random.randint(10, 100, size=num_categories)

    # Randomly choose between vertical or horizontal bars
    is_horizontal = random.choice([True, False])

    if is_horizontal:
        bars = ax.barh(categories, values, color=bar_color)  # Horizontal bars
        ax.set_title("Horizontal Bar Chart Example", fontsize=14)
        ax.set_xlabel("Value")
        ax.set_ylabel("Category")
    else:
        bars = ax.bar(categories, values, color=bar_color)  # Vertical bars
        ax.set_title("Vertical Bar Chart Example", fontsize=14)
        ax.set_xlabel("Category")
        ax.set_ylabel("Value")

    ax.grid(True)

    fig.tight_layout()
    canvas.draw()

    renderer = canvas.get_renderer()

    file_name = f"bar_chart_{image_id}.png"
    coco_output["images"].append({
        "id": image_id,
        "file_name": file_name,
        "width": IMG_WIDTH,
        "height": IMG_HEIGHT
    })

    # === Utility to flip y === #

    # === Annotate chart elements === #
    add_annotation(image_id, "title", flip_y(get_bbox_from_text(ax.title, renderer)))
    add_annotation(image_id, "x-axis", flip_y(get_bbox_from_patch(ax.spines["bottom"], renderer)))
    add_annotation(image_id, "y-axis", flip_y(get_bbox_from_patch(ax.spines["left"], renderer)))
    add_annotation(image_id, "axis-title", flip_y(get_bbox_from_text(ax.xaxis.label, renderer)))
    add_annotation(image_id, "axis-title", flip_y(get_bbox_from_text(ax.yaxis.label, renderer)))
# **************************** annotations for grid lines, tick mark and tick label
    # for tick in ax.xaxis.get_major_ticks():
    #     add_annotation(image_id, "tick-labels", flip_y(get_bbox_from_text(tick.label1, renderer)))
    #     if tick.tick1line.get_visible():
    #         add_annotation(image_id, "tick-marks", flip_y(get_bbox_from_patch(tick.tick1line, renderer)))

    # for tick in ax.yaxis.get_major_ticks():
    #     add_annotation(image_id, "tick-labels", flip_y(get_bbox_from_text(tick.label1, renderer)))
    #     if tick.tick1line.get_visible():
    #         add_annotation(image_id, "tick-marks", flip_y(get_bbox_from_patch(tick.tick1line, renderer)))

    # for line in ax.get_xgridlines() + ax.get_ygridlines():
    #     if line.get_visible():
    #         add_annotation(image_id, "gridlines", flip_y(get_bbox_from_patch(line, renderer)))
# ****************************

    for bar in bars:
        add_annotation(image_id, "bar", flip_y(get_bbox_from_patch(bar, renderer)))

    output_path = os.path.join(IMAGES_DIR, file_name)
    fig.savefig(output_path)
    plt.close()

    # Annotations section, omitted for brevity

    image_id += 1



# # Generate Line Chart
# def generate_line_chart():
#     global image_id
#     fig, ax = plt.subplots(figsize=(IMG_WIDTH / 100, IMG_HEIGHT / 100))
#     canvas = FigureCanvas(fig)

#     x = np.linspace(0, 10, 100)
#     num_series = np.random.choice([1, 2, 3])
#     colors = ['blue', 'green', 'red', 'orange', 'purple']
#     markers = ['o', 's', 'D', '^', 'v']
#     # line_types = ['linear', 'quadratic', 'exponential', 'noisy', 'sine']
#     line_types = ['linear']

#     for i in range(num_series):
#         series_type = np.random.choice(line_types)

#         if series_type == 'linear':
#             slope = np.random.uniform(0.5, 2.0)
#             intercept = np.random.uniform(-5, 5)
#             y = slope * x + intercept

#         elif series_type == 'quadratic':
#             a = np.random.uniform(0.1, 0.5)
#             b = np.random.uniform(-1, 1)
#             c = np.random.uniform(-5, 5)
#             y = a * x**2 + b * x + c

#         elif series_type == 'exponential':
#             base = np.random.uniform(1.01, 1.5)
#             y = np.power(base, x) / 10

#         elif series_type == 'noisy':
#             y = np.cumsum(np.random.randn(len(x))) / 5

#         else:  # sine
#             freq = np.random.uniform(0.5, 2.0)
#             phase = np.random.uniform(0, np.pi)
#             y = np.sin(freq * x + phase)

#         ax.plot(
#             x, y,
#             label=f"Series {i+1} ({series_type})",
#             marker=markers[i % len(markers)],
#             markevery=10,
#             markersize=5,
#             color=colors[i % len(colors)]
#         )

#     ax.set_title("Line Chart Example", fontsize=14)
#     ax.set_xlabel("X Axis")
#     ax.set_ylabel("Y Axis")
#     ax.grid(True)
#     ax.legend()

#     fig.tight_layout()
#     canvas.draw()
#     renderer = canvas.get_renderer()

#     file_name = f"line_chart_{image_id}.png"
#     coco_output["images"].append({
#         "id": image_id,
#         "file_name": file_name,
#         "width": IMG_WIDTH,
#         "height": IMG_HEIGHT
#     })

#     add_annotation(image_id, "title", flip_y(get_bbox_from_text(ax.title, renderer)))
#     add_annotation(image_id, "x-axis", flip_y(get_bbox_from_patch(ax.spines["bottom"], renderer)))
#     add_annotation(image_id, "y-axis", flip_y(get_bbox_from_patch(ax.spines["left"], renderer)))
#     add_annotation(image_id, "axis-title", flip_y(get_bbox_from_text(ax.xaxis.label, renderer)))
#     add_annotation(image_id, "axis-title", flip_y(get_bbox_from_text(ax.yaxis.label, renderer)))

#     for tick in ax.xaxis.get_major_ticks():
#         add_annotation(image_id, "tick-labels", flip_y(get_bbox_from_text(tick.label1, renderer)))
#         if tick.tick1line.get_visible():
#             add_annotation(image_id, "tick-marks", flip_y(get_bbox_from_patch(tick.tick1line, renderer)))

#     for tick in ax.yaxis.get_major_ticks():
#         add_annotation(image_id, "tick-labels", flip_y(get_bbox_from_text(tick.label1, renderer)))
#         if tick.tick1line.get_visible():
#             add_annotation(image_id, "tick-marks", flip_y(get_bbox_from_patch(tick.tick1line, renderer)))

#     for line in ax.get_xgridlines() + ax.get_ygridlines():
#         if line.get_visible():
#             add_annotation(image_id, "gridlines", flip_y(get_bbox_from_patch(line, renderer)))

#     legend = ax.get_legend()
#     if legend:
#         add_annotation(image_id, "legend", flip_y(get_bbox_from_patch(legend, renderer)))

#     output_path = os.path.join(IMAGES_DIR, file_name)
#     fig.savefig(output_path)
#     plt.close()
#     image_id += 1

# # Generate Line Chart
def generate_line_chart():
    global image_id
    fig, ax = plt.subplots(figsize=(IMG_WIDTH / 100, IMG_HEIGHT / 100))
    canvas = FigureCanvas(fig)

    x = np.linspace(0, 10, 100)
    num_series = np.random.choice([1, 2, 3])
    colors = ['blue', 'green', 'red', 'orange', 'purple']
    markers = ['o', 's', 'D', '^', 'v']
    line_types = ['linear', 'quadratic', 'exponential', 'noisy', 'sine']

    for i in range(num_series):
        series_type = np.random.choice(line_types)

        if series_type == 'linear':
            slope = np.random.uniform(0.5, 2.0)
            intercept = np.random.uniform(-5, 5)
            y = slope * x + intercept

        elif series_type == 'quadratic':
            a = np.random.uniform(0.1, 0.5)
            b = np.random.uniform(-1, 1)
            c = np.random.uniform(-5, 5)
            y = a * x**2 + b * x + c

        elif series_type == 'exponential':
            base = np.random.uniform(1.01, 1.5)
            y = np.power(base, x) / 10

        elif series_type == 'noisy':
            y = np.cumsum(np.random.randn(len(x))) / 5

        else:  # sine
            freq = np.random.uniform(0.5, 2.0)
            phase = np.random.uniform(0, np.pi)
            y = np.sin(freq * x + phase)

        # Plot the line
        ax.plot(
            x, y,
            label=f"Series {i+1} ({series_type})",
            marker=markers[i % len(markers)],
            markevery=10,
            markersize=5,
            color=colors[i % len(colors)]
        )

    # Titles and axis labels
    ax.set_title("Line Chart Example", fontsize=14)
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.grid(True)
    ax.legend()

    fig.tight_layout()
    canvas.draw()
    renderer = canvas.get_renderer()

    # --- Accurate marker point bounding boxes ---
    # Get axes bounding box in display coordinates
    ax_bbox_disp = ax.get_window_extent(renderer=renderer)
    ax_pos = ax.get_position()  # normalized [0,1] in figure
    ax_left = ax_pos.x0 * IMG_WIDTH
    ax_bottom = ax_pos.y0 * IMG_HEIGHT
    ax_width = ax_pos.width * IMG_WIDTH
    ax_height = ax_pos.height * IMG_HEIGHT

    for line in ax.get_lines():
        xdata, ydata = line.get_xdata(), line.get_ydata()
        markevery = line.get_markevery()
        if markevery is None:
            marker_indices = range(len(xdata))
        elif isinstance(markevery, int):
            marker_indices = range(0, len(xdata), markevery)
        elif hasattr(markevery, '__iter__'):
            marker_indices = markevery
        else:
            marker_indices = range(len(xdata))

        for idx in marker_indices:
            px, py = xdata[idx], ydata[idx]
            disp = ax.transData.transform((px, py))  # disp in figure pixel coordinates

            # Position within axes in figure pixel coordinates (0-1 relative to axes)
            axes_rel_x = (disp[0] - ax_bbox_disp.x0) / ax_bbox_disp.width
            axes_rel_y = (disp[1] - ax_bbox_disp.y0) / ax_bbox_disp.height

            # Map axes-relative to image coordinates
            img_x = ax_left + axes_rel_x * ax_width
            img_y = ax_bottom + axes_rel_y * ax_height

            bbox = [img_x - 5, img_y - 5, 10, 10]  # Adjust size as needed
            add_annotation(image_id, "line-point", flip_y(bbox))

    file_name = f"line_chart_{image_id}.png"
    coco_output["images"].append({
        "id": image_id,
        "file_name": file_name,
        "width": IMG_WIDTH,
        "height": IMG_HEIGHT
    })

    # Chart annotations
    add_annotation(image_id, "title", flip_y(get_bbox_from_text(ax.title, renderer)))
    add_annotation(image_id, "x-axis", flip_y(get_bbox_from_patch(ax.spines["bottom"], renderer)))
    add_annotation(image_id, "y-axis", flip_y(get_bbox_from_patch(ax.spines["left"], renderer)))
    add_annotation(image_id, "axis-title", flip_y(get_bbox_from_text(ax.xaxis.label, renderer)))
    add_annotation(image_id, "axis-title", flip_y(get_bbox_from_text(ax.yaxis.label, renderer)))

    # Tick labels and marks
    for tick in ax.xaxis.get_major_ticks():
        add_annotation(image_id, "tick-labels", flip_y(get_bbox_from_text(tick.label1, renderer)))
        if tick.tick1line.get_visible():
            add_annotation(image_id, "tick-marks", flip_y(get_bbox_from_patch(tick.tick1line, renderer)))

    for tick in ax.yaxis.get_major_ticks():
        add_annotation(image_id, "tick-labels", flip_y(get_bbox_from_text(tick.label1, renderer)))
        if tick.tick1line.get_visible():
            add_annotation(image_id, "tick-marks", flip_y(get_bbox_from_patch(tick.tick1line, renderer)))

    # Gridlines
    for line in ax.get_xgridlines() + ax.get_ygridlines():
        if line.get_visible():
            add_annotation(image_id, "gridlines", flip_y(get_bbox_from_patch(line, renderer)))

    # Legend
    legend = ax.get_legend()
    if legend:
        add_annotation(image_id, "legend", flip_y(get_bbox_from_patch(legend, renderer)))

    # Save chart
    output_path = os.path.join(IMAGES_DIR, file_name)
    fig.savefig(output_path)
    plt.close()
    image_id += 1






# Generate Pie Chart
def generate_pie_chart():
    global image_id
    fig, ax = plt.subplots(figsize=(IMG_WIDTH / 100, IMG_HEIGHT / 100))
    canvas = FigureCanvas(fig)

    num_slices = np.random.randint(3, 9)
    labels = [chr(65 + i) for i in range(num_slices)]  # e.g., ['A', 'B', ..., 'H']
    sizes = np.random.randint(10, 50, size=num_slices)
    colors = [np.random.rand(3,) for _ in range(num_slices)]  # random RGB

    is_donut = np.random.choice([True, False])  # randomly choose pie or donut

    wedgeprops = dict(width=0.4) if is_donut else None
    wedges, texts, autotexts = ax.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors,
        wedgeprops=wedgeprops
    )

    chart_type = "Donut Chart" if is_donut else "Pie Chart"
    ax.set_title(f"{chart_type} Example", fontsize=14)
    ax.axis('equal')

    fig.tight_layout()
    canvas.draw()
    renderer = canvas.get_renderer()

    file_name = f"pie_chart_{image_id}.png"
    coco_output["images"].append({
        "id": image_id,
        "file_name": file_name,
        "width": IMG_WIDTH,
        "height": IMG_HEIGHT
    })

    add_annotation(image_id, "title", flip_y(get_bbox_from_text(ax.title, renderer)))

    # Annotate slices with correct label
    for wedge in wedges:
        label = "donut-slice" if is_donut else "slice"
        bbox = get_bbox_from_patch(wedge,renderer)
        add_annotation(image_id, label, flip_y(bbox))

    for text in texts + autotexts:
        add_annotation(image_id, "label", flip_y(get_bbox_from_text(text, renderer)))

    output_path = os.path.join(IMAGES_DIR, file_name)
    fig.savefig(output_path)
    plt.close()
    image_id += 1




def generate_stacked_bar_chart():
    global image_id
    fig, ax = plt.subplots(figsize=(IMG_WIDTH / 100, IMG_HEIGHT / 100))
    canvas = FigureCanvas(fig)

    num_bars = np.random.randint(3, 9)
    categories = [chr(65 + i) for i in range(num_bars)]  # ['A', 'B', ..., 'H']
    values1 = np.random.randint(10, 50, size=num_bars)
    values2 = np.random.randint(10, 50, size=num_bars)

    color1 = np.random.rand(3,)
    color2 = np.random.rand(3,)
    is_horizontal = np.random.choice([True, False])

    if is_horizontal:
        bars1 = ax.barh(categories, values1, label='Group 1', color=color1)
        bars2 = ax.barh(categories, values2, left=values1, label='Group 2', color=color2)
        ax.set_xlabel("Value")
        ax.set_ylabel("Category")
    else:
        bars1 = ax.bar(categories, values1, label='Group 1', color=color1)
        bars2 = ax.bar(categories, values2, bottom=values1, label='Group 2', color=color2)
        ax.set_xlabel("Category")
        ax.set_ylabel("Value")

    ax.set_title("Stacked Bar Chart Example", fontsize=14)
    ax.legend()
    ax.grid(True)

    fig.tight_layout()
    canvas.draw()
    renderer = canvas.get_renderer()

    file_name = f"stacked_bar_chart_{image_id}.png"
    coco_output["images"].append({
        "id": image_id,
        "file_name": file_name,
        "width": IMG_WIDTH,
        "height": IMG_HEIGHT
    })

    add_annotation(image_id, "title", flip_y(get_bbox_from_text(ax.title, renderer)))
    add_annotation(image_id, "x-axis", flip_y(get_bbox_from_line(ax.spines["bottom"])))
    add_annotation(image_id, "y-axis", flip_y(get_bbox_from_line(ax.spines["left"])))
    add_annotation(image_id, "axis-title", flip_y(get_bbox_from_text(ax.xaxis.label, renderer)))
    add_annotation(image_id, "axis-title", flip_y(get_bbox_from_text(ax.yaxis.label, renderer)))

    for tick in ax.xaxis.get_major_ticks():
        add_annotation(image_id, "tick-labels", flip_y(get_bbox_from_text(tick.label1, renderer)))
        if tick.tick1line.get_visible():
            add_annotation(image_id, "tick-marks", flip_y(get_bbox_from_patch(tick.tick1line,renderer)))

    for tick in ax.yaxis.get_major_ticks():
        add_annotation(image_id, "tick-labels", flip_y(get_bbox_from_text(tick.label1, renderer)))
        if tick.tick1line.get_visible():
            add_annotation(image_id, "tick-marks", flip_y(get_bbox_from_patch(tick.tick1line,renderer)))

    for line in ax.get_xgridlines() + ax.get_ygridlines():
        if line.get_visible():
            add_annotation(image_id, "gridlines", flip_y(get_bbox_from_line(line)))

    for bar in bars1:
        add_annotation(image_id, "stacked-bar", flip_y(get_bbox_from_patch(bar, renderer)))
    for bar in bars2:
        add_annotation(image_id, "stacked-bar", flip_y(get_bbox_from_patch(bar, renderer)))

    for legend_text in ax.get_legend().get_texts():
        add_annotation(image_id, "legend-item", flip_y(get_bbox_from_text(legend_text, renderer)))

    output_path = os.path.join(IMAGES_DIR, file_name)
    fig.savefig(output_path)
    plt.close()
    image_id += 1

# def generate_area_chart():
#     global image_id
#     fig, ax = plt.subplots(figsize=(IMG_WIDTH / 100, IMG_HEIGHT / 100))
#     canvas = FigureCanvas(fig)

#     x = np.arange(1, 11)
#     y = np.random.randint(20, 100, size=10)

#     ax.fill_between(x, y, color="skyblue", alpha=0.5)
#     ax.plot(x, y, color="Slateblue")

#     ax.set_title("Area Chart Example", fontsize=14)
#     ax.set_xlabel("X-axis")
#     ax.set_ylabel("Y-axis")
#     ax.grid(True)

#     file_name = f"area_chart_{image_id}.png"
#     fig.tight_layout()
#     canvas.draw()
#     renderer = canvas.get_renderer()

#     # Add image info
#     coco_output["images"].append({
#         "id": image_id,
#         "file_name": file_name,
#         "width": IMG_WIDTH,
#         "height": IMG_HEIGHT
#     })

#     # === CHANGED: flip_y added for all annotations ===
#     add_annotation(image_id, "title", flip_y(get_bbox_from_text(ax.title, renderer)))
#     add_annotation(image_id, "x-axis", flip_y(get_bbox_from_line(ax.spines["bottom"])))
#     add_annotation(image_id, "y-axis", flip_y(get_bbox_from_line(ax.spines["left"])))
#     add_annotation(image_id, "axis-title", flip_y(get_bbox_from_text(ax.xaxis.label, renderer)))
#     add_annotation(image_id, "axis-title", flip_y(get_bbox_from_text(ax.yaxis.label, renderer)))

#     for tick in ax.xaxis.get_major_ticks():
#         add_annotation(image_id, "tick-labels", flip_y(get_bbox_from_text(tick.label1, renderer)))

#     for tick in ax.yaxis.get_major_ticks():
#         add_annotation(image_id, "tick-labels", flip_y(get_bbox_from_text(tick.label1, renderer)))

#     for line in ax.get_xgridlines() + ax.get_ygridlines():
#         if line.get_visible():
#             add_annotation(image_id, "gridlines", flip_y(get_bbox_from_line(line)))

#     # Area patch
#     path = ax.collections[0].get_paths()[0]
#     patch = patches.PathPatch(path, transform=ax.transData)
#     add_annotation(image_id, "area", flip_y(get_bbox_from_patch(patch, renderer)))

#     # Save the chart
#     output_path = os.path.join(IMAGES_DIR, file_name)
#     fig.savefig(output_path)
#     plt.close()
#     image_id += 1

def generate_area_chart():
    global image_id
    fig, ax = plt.subplots(figsize=(IMG_WIDTH / 100, IMG_HEIGHT / 100))
    canvas = FigureCanvas(fig)

    x = np.arange(1, 11)
    y = np.random.randint(20, 100, size=10)

    ax.fill_between(x, y, color="skyblue", alpha=0.5)
    # Add markers to the line
    ax.plot(x, y, color="Slateblue", marker='o', markersize=7, linestyle='-', label='Data')

    ax.set_title("Area Chart Example", fontsize=14)
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.grid(True)

    file_name = f"area_chart_{image_id}.png"
    fig.tight_layout()
    canvas.draw()
    renderer = canvas.get_renderer()

    # --- Accurate marker point bounding boxes ---
    # Get axes bounding box in display coordinates
    ax_bbox_disp = ax.get_window_extent(renderer=renderer)
    ax_pos = ax.get_position()  # normalized [0,1] in figure
    ax_left = ax_pos.x0 * IMG_WIDTH
    ax_bottom = ax_pos.y0 * IMG_HEIGHT
    ax_width = ax_pos.width * IMG_WIDTH
    ax_height = ax_pos.height * IMG_HEIGHT

    # Annotate each marker on the line
    for line in ax.get_lines():
        xdata, ydata = line.get_xdata(), line.get_ydata()
        for idx in range(len(xdata)):
            px, py = xdata[idx], ydata[idx]
            disp = ax.transData.transform((px, py))  # disp in figure pixel coordinates

            # Position within axes in figure pixel coordinates (0-1 relative to axes)
            axes_rel_x = (disp[0] - ax_bbox_disp.x0) / ax_bbox_disp.width
            axes_rel_y = (disp[1] - ax_bbox_disp.y0) / ax_bbox_disp.height

            # Map axes-relative to image coordinates
            img_x = ax_left + axes_rel_x * ax_width
            img_y = ax_bottom + axes_rel_y * ax_height

            bbox = [img_x - 7, img_y - 7, 14, 14]  # Adjust size as needed
            add_annotation(image_id, "line-point", flip_y(bbox))

    # Add image info
    coco_output["images"].append({
        "id": image_id,
        "file_name": file_name,
        "width": IMG_WIDTH,
        "height": IMG_HEIGHT
    })

    add_annotation(image_id, "title", flip_y(get_bbox_from_text(ax.title, renderer)))
    add_annotation(image_id, "x-axis", flip_y(get_bbox_from_line(ax.spines["bottom"])))
    add_annotation(image_id, "y-axis", flip_y(get_bbox_from_line(ax.spines["left"])))
    add_annotation(image_id, "axis-title", flip_y(get_bbox_from_text(ax.xaxis.label, renderer)))
    add_annotation(image_id, "axis-title", flip_y(get_bbox_from_text(ax.yaxis.label, renderer)))

    for tick in ax.xaxis.get_major_ticks():
        add_annotation(image_id, "tick-labels", flip_y(get_bbox_from_text(tick.label1, renderer)))

    for tick in ax.yaxis.get_major_ticks():
        add_annotation(image_id, "tick-labels", flip_y(get_bbox_from_text(tick.label1, renderer)))

    for line in ax.get_xgridlines() + ax.get_ygridlines():
        if line.get_visible():
            add_annotation(image_id, "gridlines", flip_y(get_bbox_from_line(line)))

    # Area patch
    path = ax.collections[0].get_paths()[0]
    patch = patches.PathPatch(path, transform=ax.transData)
    add_annotation(image_id, "area", flip_y(get_bbox_from_patch(patch, renderer)))

    # Save the chart
    output_path = os.path.join(IMAGES_DIR, file_name)
    fig.savefig(output_path)
    plt.close()
    image_id += 1

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    if not os.path.exists(IMAGES_DIR):
        os.makedirs(IMAGES_DIR)

    if not os.path.exists(os.path.dirname(ANNOT_PATH)):
        os.makedirs(os.path.dirname(ANNOT_PATH))

    # Save the classes to file
    save_classes()

    # Load classes from file
    load_classes()

    chart_types = [
        "bar_chart", "line_chart", "pie_chart", "stacked_bar_chart", "area_chart","column_chart"

    ]

    for chart_type in tqdm(chart_types, desc="Chart Types"):
      for i in tqdm(range(NUM_IMAGES_PER_TYPE), desc=chart_type, leave=False):
          if chart_type == "bar_chart":
              num_categories = random.randint(2, 26)
              bar_color = available_colors[i % len(available_colors)]

              generate_bar_chart(num_categories, bar_color)
          elif chart_type == "line_chart":
              generate_line_chart()

          elif chart_type == "pie_chart":
              # num_categories = random.randint(2, 26)
              # color = available_colors[i % len(available_colors)]
              generate_pie_chart()

          elif chart_type == "stacked_bar_chart":
              generate_stacked_bar_chart()

          elif chart_type == "area_chart":
              generate_area_chart()



          else:
              print(f"No generator implemented for chart type: {chart_type}")

    with open(ANNOT_PATH, "w") as json_file:
        json.dump(coco_output, json_file, indent=4)

    print(f"[✓] Finished generating images and annotations in {OUTPUT_DIR}.")


if __name__ == "__main__":
    main()


