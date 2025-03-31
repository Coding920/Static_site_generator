
def md_to_blocks(text) -> list[str]:
    if not text:
        return []

    list_to_return = []
    blocks = text.split("\n\n")
    blocks = list(map(lambda text: text.strip().lstrip("\n"), blocks))
    for block in blocks:
        if not block.strip("\n").strip():
            continue

        lines = []
        for line in block.split("\n"):
            line = line.strip()
            lines.append(line)

        new_block = "\n".join(lines)
        list_to_return.append(new_block)

    return list_to_return
