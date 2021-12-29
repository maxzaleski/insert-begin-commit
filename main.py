import os

INPUT_DIR = "./input"
OUTPUT_DIR = "./output"


def main(base_dir: str) -> None:
    """
    Loop through all entries in the input directory, if the entry is a directory, call main() on it,
    otherwise, process the file.

    :param base_dir: the initial directory
    """
    for entity in os.listdir(base_dir):
        entity_path = os.path.join(base_dir, entity)
        if os.path.isdir(entity_path):
            main(entity_path)
        else:
            with open(entity_path, "r") as f:
                content = f.read()
                f.close()

            entity_path = entity_path.replace(INPUT_DIR, OUTPUT_DIR)
            if not os.path.exists(os.path.dirname(entity_path)):
                os.makedirs(os.path.dirname(entity_path))

            # Objective is to insert the transaction keywords "BEGIN" and "COMMIT" at both ends of the file.
            with open(entity_path, "w") as f:
                # Some may already contain the keywords, in which case we don't want to add them again.
                if content.startswith("BEGIN;"):
                    continue
                else:
                    # Rewrite the file with the keywords inserted.
                    if not content.endswith("\n"):
                        content += "\n"
                    f.write(f"BEGIN;\n\n{content}\nCOMMIT;")
                    f.close()


if __name__ == '__main__':
    # Check if the relevant directories exists.
    for val in [INPUT_DIR, OUTPUT_DIR]:
        if not os.path.exists(val):
            os.mkdir(val)

    main(INPUT_DIR)
