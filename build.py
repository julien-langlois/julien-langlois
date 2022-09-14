from profile_readme import get_github_context, ProfileGenerator
import requests
from datetime import datetime


def get_weather(city):
    # declare the client. format defaults to the metric system (celcius, km/h, etc.)
    url = "https://wttr.in/{}?m&format=3".format(city)
    res = requests.get(url)
    return res.text


def date():
    date = datetime.now()
    return date.strftime("%d %B %Y at %H:%M:%S")


if __name__ == "__main__":
    weather = get_weather("Montpellier")
    date = date()
    context = {
        "weather": weather,
        "date": date,
        "linkedin": {
            "url": "https://www.linkedin.com/in/langloisjulien/",
            "badge": "![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)",
        },
        "twitter": {
            "url": "https://twitter.com/tidodawiseolman/",
            "badge": "![Twitter](https://img.shields.io/badge/Twitter-%231DA1F2.svg?style=for-the-badge&logo=Twitter&logoColor=white)",
        },
        "keybase": {
            "url": "https://keybase.io/julienlanglois",
            "badge": "![Keybase](https://img.shields.io/badge/-julienlanglois-red?style=for-the-badge&logo=keybase&logoColor=white&link=https://keybase.io/julienlanglois)",
        },
        "stats": [
            "![Github Stats](https://github-readme-stats.vercel.app/api?username=julien-langlois&count_private=true&show_icons=true&include_all_commits=true&theme=github_dark&hide_border=true)",
            "![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=julien-langlois&layout=compact&theme=github_dark&hide_border=true&langs_count=10)",
        ],
        "badges": [
            "![Drupal](https://img.shields.io/badge/-Drupal-black?style=for-the-badge&logo=drupal)",
            "![Lando](https://img.shields.io/badge/Lando-794993?style=for-the-badge&logo=lando&LogoColor=white)",
            "![Vagrant](https://img.shields.io/badge/vagrant-%231563FF.svg?style=for-the-badge&logo=vagrant&logoColor=white)",
            "![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)",
            "![Ansible](https://img.shields.io/badge/ansible-%231A1918.svg?style=for-the-badge&logo=ansible&logoColor=white)",
            "![Terraform](https://img.shields.io/badge/terraform-%235835CC.svg?style=for-the-badge&logo=terraform&logoColor=white)",
            "![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)",
            "![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)",
            "![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)",
            "![MariaDB](https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=mariadb&logoColor=white)",
            "![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)",
            "![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)",
            "![SolR](https://img.shields.io/badge/Solr-%23E30000.svg?style=for-the-badge&logo=apache-solr&logoColor=white)",
            "![Apache](https://img.shields.io/badge/apache-%23D42029.svg?style=for-the-badge&logo=apache&logoColor=white)",
            "![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)",
            "![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)",
            "![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)",
            "![GitLab](https://img.shields.io/badge/gitlab-%23181717.svg?style=for-the-badge&logo=gitlab&logoColor=white)",
            "![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)",
            "![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)",
            "![GitLab CI](https://img.shields.io/badge/gitlab%20ci-%23181717.svg?style=for-the-badge&logo=gitlab&logoColor=white)",
            "![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)",
            "![Alpine Linux](https://img.shields.io/badge/Alpine_Linux-%230D597F.svg?style=for-the-badge&logo=alpine-linux&logoColor=white)",
            "![Cent OS](https://img.shields.io/badge/cent%20os-002260?style=for-the-badge&logo=centos&logoColor=F0F0F0)",
            "![Debian](https://img.shields.io/badge/Debian-D70A53?style=for-the-badge&logo=debian&logoColor=white)",
            "![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)",
        ],
    }
    # If you don't need the GitHub data you can remove the next line
    context.update(**get_github_context("julien-langlois"))
    ProfileGenerator.render(
        template_path="README-TEMPLATE.j2", output_path="README.md", context=context
    )
