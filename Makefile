brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install --upgrade dist/*.whl
