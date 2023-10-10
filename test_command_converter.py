name: Continuous Integration

on:
  push:
    branches:
      - main  # or the name of your default branch

jobs:
  test:
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest]
        python-version: [3.7, 3.8, 3.9, 3.10]
    runs-on: ${{ matrix.os }}
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
      
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: ${{ matrix.python-version }}
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          # If you have any dependencies, install them here
      
      - name: Run tests
        run: python -m unittest discover

      - name: Create Issue on Failure
        if: failure()
        uses: actions/github-script@v5
        with:
          script: |
            const issue = {
              title: "Test Failure",
              body: `Tests failed on ${{ matrix.os }} with Python ${{ matrix.python-version }}`,
              labels: ["bug", "CI"]
            };
            github.rest.issues.create(issue);
