from cx_Freeze import setup, Executable

executables = [Executable("conversor-pdf-jpg.py")]

setup(
    name="Conversor de PDF para JPG",
    version="1.0",
    description="Descrição do seu programa",
    executables=executables
)
