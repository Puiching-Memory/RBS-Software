import pylint.lint
pylint_opts = ['main.py --files-output y --output-format json']
pylint.lint.Run(pylint_opts)