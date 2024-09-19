import click

@click.command()
@click.option("--a", type=str, required=True, help="A string")
@click.option(
    "--b", type=int, required=True, help="An integer"
)
def func(a:str, b: int, c: float = 1.5):
    """_summary_

    Args:
        a (str): _description_
        b (int): _description_
        c (float, optional): _description_. Defaults to 1.5.

    Returns:
        _type_: _description_
    """
    print(f'Input a is {a}, and the sum of b and c is {b+c}')

if __name__ == '__main__':
    func()
    