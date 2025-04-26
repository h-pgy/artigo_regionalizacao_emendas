import os


def solve_folder(folder_name:str, parent=None)->str:
    """
    This function takes a folder name and an optional parent directory.
    It returns the absolute path of the folder, creating it if it doesn't exist.

    Parameters:
        folder_name (str): The name of the folder to create or locate.
        parent (str, optional): The parent directory. Defaults to None.

    Returns:
        str: The absolute path of the folder.
    """
    if parent is None:
        parent = os.getcwd()
    folder_path = os.path.join(parent, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return os.path.abspath(folder_path)


DATA_FOLDER: str = solve_folder('data')
GRAFICOS_FOLDER=solve_folder('graficos', 'static')
DADOS_FINAL: str = os.path.join(solve_folder('base_final'), 'emendas_orcamentarias_regionalizadas.csv')