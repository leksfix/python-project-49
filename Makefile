brain-games:
	uv run brain-games

lint:
	uv run ruff check brain_games

build:
	uv build

package-install:
	uv tool install --force-reinstall dist/*.whl
