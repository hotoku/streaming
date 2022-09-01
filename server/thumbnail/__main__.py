import json

import click


def convert(d: str):
    pass


@click.command()
@click.argument("config", type=click.Path(exists=True, dir_okay=False, readable=True))
def main(config: str):
    with open(config) as f:
        cfg = json.load(f)
    print(cfg)


if __name__ == "__main__":
    main()
