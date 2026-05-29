# Setup Notes

1. Copy `.env.example` to `.env` and add only the keys needed for the workflow.
2. Install dependencies with `python -m pip install -e .[test]`. Add `[browser]` for Genspark automation or `[vision]` for OCR.
3. Run commands from the repo root.
4. For assisted Genspark paste, start Chrome with remote debugging, open Genspark manually, then run `scripts/genspark_assisted.py`.
5. Generated campaign data belongs in `data/` or `.tmp/`; do not commit private reports or API outputs.
