import networkx as nx
import matplotlib.pyplot as plt
from urllib.parse import urlparse


def create_graph_visualization(pages, base_url, output_file="website_graph.png"):
    """Creates a visual graph representation of the website's link structure."""
    G = nx.DiGraph()
    base_domain = urlparse(base_url).netloc

    # Add nodes and edges
    for url in pages.keys():
        G.add_node(url, color="lightblue" if base_domain in url else "lightgray")

    # Add edges based on found links
    for source, count in pages.items():
        for target in pages.keys():
            if source != target:
                G.add_edge(source, target)

    # Create the visualization
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G, k=1, iterations=50)

    # Draw nodes
    node_colors = [G.nodes[node]["color"] for node in G.nodes()]
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=500)

    # Draw edges
    nx.draw_networkx_edges(G, pos, edge_color="gray", arrows=True)

    # Add labels
    labels = {url: urlparse(url).path for url in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels, font_size=8)

    plt.title(f"Website Link Structure: {base_domain}")
    plt.axis("off")
    plt.tight_layout()

    # Save the graph
    plt.savefig(output_file, dpi=300, bbox_inches="tight")
    plt.close()

    print(f"\nGraph visualization saved as {output_file}")


def print_report(pages, base_url):
    print("=============================")
    print(f"REPORT for {base_url}")
    print("=============================")

    sorted_pages = sort_pages(pages)
    for url, count in sorted_pages:
        print(f"Found {count} internal links to {url}")

    create_graph_visualization(pages, base_url)


def sort_pages(pages):
    # Convert the dictionary to a list of [url, count] pairs
    pages_list = list(pages.items())

    # Sort the list by count (highest first), then by URL (alphabetically)
    pages_list.sort(key=lambda x: (-x[1], x[0]))

    return pages_list
