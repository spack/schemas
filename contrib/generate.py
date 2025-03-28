#!/usr/bin/env python3

from spack.config import SECTION_SCHEMAS
import spack.schema.env
import json

# individual config file schemas
for section in SECTION_SCHEMAS:
    with open(f"{section}.json", "w") as f:
        f.write(json.dumps(SECTION_SCHEMAS[section], indent=0, separators=(",", ":")))

# spack.yaml environment file
with open("spack.json", "w") as f:
    f.write(json.dumps(spack.schema.env.schema, indent=0, separators=(",", ":")))