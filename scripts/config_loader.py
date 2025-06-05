import json
from pathlib import Path

import yaml


class ConfigLoader:
    def __init__(self, src_path: Path):
        self.src_path = src_path

    def load_translations(self):
        with open(
            self.src_path / "data" / "translations.yaml", "r", encoding="utf-8"
        ) as f:
            return yaml.safe_load(f)

    def load_projects(self):
        with open(self.src_path / "data" / "projects.yaml", "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    def load_site_config(self):
        with open(
            self.src_path / "config" / "site_config.yaml", "r", encoding="utf-8"
        ) as f:
            return yaml.safe_load(f)

    def load_factions(self):
        factions = {}
        for lang in ["fr", "en"]:
            try:
                with open(
                    self.src_path / "data" / f"factions_{lang}.json",
                    "r",
                    encoding="utf-8",
                ) as f:
                    factions[lang] = json.load(f)
            except FileNotFoundError:
                print(f"Warning: factions_{lang}.json not found")
                factions[lang] = {"factions": []}
        return factions
