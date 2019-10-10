# my résumé

This repository is a customized fork of
[jglovier's](https://github.com/jglovier)
[resume-template](https://github.com/jglovier/resume-template),

> A simple Jekyll + GitHub Pages powered résumé template.

## Customizing

First you'll want to fork the repo to your own account, then clone it locally and customize.
Use `jekyll serve` to build a local site for inspection.

### Options/configuration

Most of the basic customization will take place in the `_config.yml` file. From there, you can set
URLs for your myriad social media accounts and toggle each section of the résumé on and off.

### Content

All the information rendered in the résumé can be found under `_data`, stored in YAML files. This is
where you'll add new content, e.g., new work experience or papers. This stripped-down format helps
you focus on the text, which Jekyll will render beautifully for you later on. There's some help on
YAML data files in the [Jekyll docs](https://jekyllrb.com/docs/datafiles/).

Don't forget to run spellcheck!

### Layout

The HTML template that turns into your résumé is `/_layouts/resume.html`. If you want to change what
a section shows, or change the sequence of sections, edit `resume.html`. To modify the appearance of
a section or elements of a section, you'll have to edit the CSS, which is in `_sass/_resume.scss`.
If something isn't showing up, or is rendering in a weird way, your browser's context menu (right
click) should give you the option to "inspect" elements of the page. Check for warnings and error
messages in the console.

## Running locally

To test locally, run the following in your terminal:

1. Clone repo locally
2. `bundle install`
3. `jekyll serve`
4. Open your browser to `localhost:4000`

## Publishing to GitHub Pages for free

[GitHub Pages](https://pages.github.com/) will host this for free with your GitHub account. Just
make sure you're using a `gh-pages` branch, and the site will automatically be available at
`yourusername.github.io/resume-template` (you can rename the repo to résumé for your own use if you
want it to be available at `yourusername.github.io/resume`). You can also add a CNAME if you want it
to be available at a custom domain.

## License

The code and styles are licensed under the [MIT License](LICENSE).
