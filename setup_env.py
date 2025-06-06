import os
import shutil
import subprocess
import sys
import sysconfig

VENV_DIR = '.venv'


def run(cmd: list[str]) -> None:
    """Run a command and display it."""
    print(' '.join(cmd))
    subprocess.check_call(cmd)


def venv_python() -> str:
    """Return the path to the Python executable inside the venv."""
    if os.name == 'nt':
        return os.path.join(VENV_DIR, 'Scripts', 'python.exe')
    return os.path.join(VENV_DIR, 'bin', 'python')


def ensure_venv() -> None:
    """Create the virtual environment if it does not exist."""
    if not os.path.isdir(VENV_DIR):
        run([sys.executable, '-m', 'venv', VENV_DIR])


def install_requirements() -> None:
    py = venv_python()
    run([py, '-m', 'pip', 'install', '--upgrade', 'pip'])
    run([py, '-m', 'pip', 'install', '-r', 'requirements.txt'])


def copy_sitecustomize() -> None:
    py = venv_python()
    # Determine site-packages directory
    code = 'import sysconfig, json; print(json.dumps(sysconfig.get_path("purelib")))'
    site_packages = subprocess.check_output([py, '-c', code], text=True).strip().strip('"')
    target = os.path.join(site_packages, 'sitecustomize.py')
    shutil.copy2('sitecustomize.py', target)
    print(f'Copied sitecustomize.py -> {target}')


def pull_default_model() -> None:
    model = os.environ.get('OLLAMA_MODEL')
    if not model:
        print('OLLAMA_MODEL not set; skipping model download.')
        return
    try:
        run(['ollama', 'pull', model])
    except FileNotFoundError:
        print('ollama command not found; skipping model download.')


def main() -> None:
    ensure_venv()
    install_requirements()
    copy_sitecustomize()
    pull_default_model()
    print('Setup complete. Activate with:\n  source .venv/bin/activate  (or .venv\\Scripts\\activate on Windows)')


if __name__ == '__main__':
    main()
