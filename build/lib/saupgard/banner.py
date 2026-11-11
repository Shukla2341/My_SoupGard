from pathlib import Path

def get_banner():
    banner_path = Path(__file__).parent / "data" / "banner.txt"
    return banner_path.read_text()