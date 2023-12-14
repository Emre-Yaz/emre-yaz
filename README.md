I'm Ibrahim Emre Yaz

- 🔭 I’m currently working on building my first website.
- 🌱 I’m currently learning back-end development.
- 📫 How to reach me ## https://www.linkedin.com/in/ibrahim-emre-yaz/

<!--START_SECTION:waka-->

name: Waka Readme

on:
  schedule:
    # Runs at 12am IST
    - cron: '30 18 * * *'
  workflow_dispatch:
jobs:
  update-readme:
    name: Update Readme with Metrics
    runs-on: ubuntu-latest
    steps:
      - uses: anmol098/waka-readme-stats@master
        with:
          WAKATIME_API_KEY: ${{ secrets.WAKATIME_API_KEY }}
          GH_TOKEN: ${{ secrets.GH_TOKEN }}

<!--END_SECTION:waka-->


<!--
**Emre-Yaz/emre-yaz** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.
-->
