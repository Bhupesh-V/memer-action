<p align="center">
  <h1 align="center">Memer Action</h1>
  <p align="center">
  <a href=""><img src="https://raw.githubusercontent.com/Bhupesh-V/memer-action/master/images/header.png?token=AIGANF6ODRJK3Z2FQ5BKO6K6TLD2O" alt="memer-action-logo" height="160"></a>
  </p>
</p>

[![Github marketplace](https://img.shields.io/badge/Marketplace-Memer%20Action-blue.svg?colorA=24292e&colorB=0366d6&style=flat&longCache=true&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAM6wAADOsB5dZE0gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAERSURBVCiRhZG/SsMxFEZPfsVJ61jbxaF0cRQRcRJ9hlYn30IHN/+9iquDCOIsblIrOjqKgy5aKoJQj4O3EEtbPwhJbr6Te28CmdSKeqzeqr0YbfVIrTBKakvtOl5dtTkK+v4HfA9PEyBFCY9AGVgCBLaBp1jPAyfAJ/AAdIEG0dNAiyP7+K1qIfMdonZic6+WJoBJvQlvuwDqcXadUuqPA1NKAlexbRTAIMvMOCjTbMwl1LtI/6KWJ5Q6rT6Ht1MA58AX8Apcqqt5r2qhrgAXQC3CZ6i1+KMd9TRu3MvA3aH/fFPnBodb6oe6HM8+lYHrGdRXW8M9bMZtPXUji69lmf5Cmamq7quNLFZXD9Rq7v0Bpc1o/tp0fisAAAAASUVORK5CYII=)](https://github.com/marketplace/actions/memer-action)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/bhupesh-v/memer-action?logo=GitHub)](https://github.com/Bhupesh-V/memer-action/releases) 
[![Lint](https://github.com/Bhupesh-V/memer-action/workflows/Lint/badge.svg?branch=master)](https://github.com/Bhupesh-V/memer-action/actions?query=workflow%3ALint)
[![Integration Test](https://github.com/Bhupesh-V/memer-action/workflows/Integration%20Test/badge.svg?branch=master)](https://github.com/Bhupesh-V/memer-action/actions?query=workflow%3A%22Integration+Test%22)
<a href="https://twitter.com/bhupeshimself">
  <img alt="Twitter: Bhupesh Varshney" src="https://img.shields.io/twitter/follow/bhupeshimself.svg?style=social" target="_blank" />
</a>

## ✨ Demo

![demomemer](https://user-images.githubusercontent.com/34342551/79064573-a6fa9e80-7cc7-11ea-895e-6538c2b8548b.png)

## ❓ Usage

### Example workflow

- You can use the following workflow as it is, just copy/paste in a file named `greetings.yml` inside your [workflows](https://github.com/Bhupesh-V/memer-action/tree/master/.github/workflows) folder.
- The reply action is performed by [create-or-update-comment](https://github.com/peter-evans/create-or-update-comment)

```yaml
name: Memer Workflow

on: [pull_request]

jobs:
  greeting:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@master
      - name: Run Memer Action
        id: memer

        uses: Bhupesh-V/memer-action@master
        with:
          filter: "new"

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
            🎉🎉 Thanks for opening this PR/Issue 🤗
            Please wait while the maintainer(s) review it

            Meanwhile have a look at this 😝 :

            > **${{ steps.memer.outputs.title }}**
            ![meme](${{ steps.memer.outputs.meme }})
            <sub>ℹ️ <a href="${{ steps.memer.outputs.source }}">Source</a> [ Powered By 🔥 <a href="https://github.com/Bhupesh-V/memer-action">Memer Action</a> ]</sub>

```

### Inputs

Memer Action accepts following input variables.

- `filter` (optional) : Sort Memes posts from reddit. Only 4 values are acceptable, **hot**, **top**, **new** & **rising**. By default the memes are "hot".
- `fallback` (optional) : A JSON string for showing a Fallback meme, in case there are no memes available. By default the fallback output is
```python
FALLBACK = {
    "meme_link": "https://raw.githubusercontent.com/Bhupesh-V/memer-action/master/images/header.png",
    "title": "Oops :( looks like we are out of memes.",
    "src": "https://github.com/Bhupesh-V/memer-action",
}
```

```yaml
steps:
- uses: actions/checkout@master
- name: Run action
  id: myaction

  uses: Bhupesh-V/memer-action@master
  with:
    filter: new
    fallback: '{"meme_link":"<meme-url>", "title": "<meme-title>", "src": "<meme-source-url>"}'

- name: Check outputs
    run: |
    echo "Outputs - ${{ steps.myaction.outputs.title }}"
    echo "Outputs - ${{ steps.myaction.outputs.meme }}"
    echo "Outputs - ${{ steps.myaction.outputs.source }}"
```

### Outputs

Memer Action sets 3 outputs.

- `title`: The title of the post on reddit
- `meme`: The meme image link
- `source`: The Source of the Meme (post on reddit)

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

Note: This action does not work in `pull_request` workflows when triggered by a fork opening a pull request in the upstream repository.
This is due to restrictions put in place by GitHub Actions. See [here](https://github.com/peter-evans/create-pull-request/blob/master/docs/concepts-guidelines.md#restrictions-on-forked-repositories) for further explanation.

## Author

👤 **Bhupesh Varshney**

- Web : [bhupesh.codes](https://bhupesh-v.github.io)
- Twitter : [@bhupeshimself](https://twitter.com/bhupeshimself)
- DEV : [bhupesh](https://dev.to/bhupesh)

## 💙 Credits
- [create-or-update-comment](https://github.com/peter-evans/create-or-update-comment)
- [python-container-action](https://github.com/jacobtomlinson/python-container-action)

## ☺️ Show your support

Support me by giving a ⭐️ if this project helped you! or just [![Twitter URL](https://img.shields.io/twitter/url?label=Tweet%20Memer%20Action&logoColor=blue&style=social&url=https%3A%2F%2Ftwitter.com%2Fintent%2Ftweet%3Furl%3Dhttps%3A%2F%2Fgithub.com%2FBhupesh-V%2Fmemer-action%26text%3DA%2520GitHub%2520Action%2520for%2520programmer%2520memes%2520%3B%29)](https://twitter.com/intent/tweet?url=https://github.com/Bhupesh-V/memer-action&text=A%20GitHub%20Action%20for%20programmer%20memes)

<a href="https://liberapay.com/bhupesh/donate">
  <img alt="Donate using Liberapay" src="https://liberapay.com/assets/widgets/donate.svg" width="100">
</a>

<a href="https://www.patreon.com/bhupesh">
  <img src="https://c5.patreon.com/external/logo/become_a_patron_button@2x.png" width="160">
</a>

## 📝 License

Copyright © 2020 [Bhupesh Varshney](https://github.com/Bhupesh-V).<br />
This project is [MIT](https://github.com/Bhupesh-V/memer-action/blob/master/LICENSE) licensed.
