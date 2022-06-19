# auto-pr-action

`.github/workflows/enable-auto-pr.yml`

```yml
name: Enable auto pr

on:
  push:
    branches:
      - '*'
      - '!master'

jobs:
  hashtags:
    name: Enable auto pr
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v1
      - uses: wix-playground/auto-pr-action@master
        with:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

```
!!!!
