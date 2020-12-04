import PyInstaller.__main__


PyInstaller.__main__.run(
    [
        # "--paths=C:/Users/Alexandra/AppData/Local/Programs/Python/Python36/Lib/site-packages",
        "--onefile",
        # "--windowed",
        "--add-data=./build-magic/google_api_python_client-1.12.8.dist-info/*;./google_api_python_client-1.12.8.dist-info",
        "--add-data=client_secret_391891465960_i956mfi2rjc439c8qtdblkgn6ktuhob2_apps.json;.",
        "protocol.py",
    ]
)
