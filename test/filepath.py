from pathlib import Path

if __name__ == "__main__":
    p = Path('.')
    print([x for x in p.iterdir() if x.is_dir()])

    p = Path('../')
    print([x for x in p.iterdir() if x.is_dir()])

    p = Path('../example_file/')
    print([x for x in p.iterdir() if x.is_dir()])

    p = Path('example_file/')
    print([x for x in p.iterdir() if x.is_dir()])

    open("../example_file/blank_white.png")
