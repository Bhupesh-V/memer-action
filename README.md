# Memer Action

[![Lint](https://github.com/Bhupesh-V/memer-action/workflows/Lint/badge.svg)](https://github.com/Bhupesh-V/memer-action/actions)
[![Integration Test](https://github.com/Bhupesh-V/memer-action/workflows/Integration%20Test/badge.svg)](https://github.com/Bhupesh-V/memer-action/actions)
<a href="https://twitter.com/bhupeshimself">
  <img alt="Twitter: Bhupesh Varshney" src="https://img.shields.io/twitter/follow/bhupeshimself.svg?style=social" target="_blank" />
</a>


## Usage

Describe how to use your action here.

### Example workflow

```yaml
name: Memer Workflow

on: [pull_request]

jobs:
  greeting:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@master
      - name: Run Memer Action
      - id: memer

        uses: Bhupesh-V/memer-action@master

      - name: Check Outputs
        run: |
          echo "${{ steps.memer.outputs.meme }}"
          echo "${{ steps.memer.outputs.title }}"
          echo "${{ steps.memer.outputs.source }}"

      - name: Create comment
        uses: peter-evans/create-or-update-comment@v1.3.0
        id: couc
        with:
          issue-number: ${{ github.event.number }}
          body: |
            Thanks for opening this PR 🤗, Pls wait while the maintainer(s) review it

            Meanwhile have a look at this meme :)

            > ${{ steps.memer.outputs.title }}
            ![meme](${{ steps.memer.outputs.meme }})
            <sub><a href="${{ steps.memer.outputs.source }}">Source</a>

            <p><a href="https://github.com/Bhupesh-V/memer-action">:star:  on github</a></p>

```


### Outputs

Memer Action sets 3 outputs.

- `title`: The title of the post on reddit
- `meme`: The meme image link
- `source`: The Source of the post on reddit

```yaml
steps:
- uses: actions/checkout@master
- name: Run action
  id: myaction

  uses: Bhupesh-V/memer-action@master

- name: Check outputs
    run: |
    echo "Outputs - ${{ steps.myaction.outputs.title }}"
    echo "Outputs - ${{ steps.myaction.outputs.meme }}"
    echo "Outputs - ${{ steps.myaction.outputs.source }}"
```


## Author

👤 **Bhupesh Varshney**

- Twitter : [@bhupeshimself](https://twitter.com/bhupeshimself)
- DEV : [bhupesh](https://dev.to/bhupesh)


## ☺️ Show your support

Support me by giving a ⭐️ if this project helped you! or just [![Twitter URL](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2F)](https://twitter.com/intent/tweet?url=https://github.com/Bhupesh-V/til&text=til%20via%20@bhupeshimself)

<a href="https://www.patreon.com/bhupesh">
  <img src="https://c5.patreon.com/external/logo/become_a_patron_button@2x.png" width="160">
</a>

## 📝 License

Copyright © 2020 [Bhupesh Varshney](https://github.com/Bhupesh-V).<br />
This project is [MIT](https://github.com/Bhupesh-V/til/blob/master/LICENSE) licensed.
