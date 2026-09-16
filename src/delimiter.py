from textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    new_nodes: list[TextNode] = []

    for node in old_nodes:
        val = node.text
        spl = val.split(delimiter)
        if len(spl) == 1:
            new_nodes.append(node)
            continue
        elif len(spl) % 2 == 0:
            raise ValueError(f"missing a closing {delimiter} in {node}")

        for i, section in enumerate(spl):
            if i == 0 and section == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(section, TextType.TEXT))
            else:
                new_nodes.append(TextNode(section, text_type))

    return new_nodes
