# Shervan Jassim portfolio

Standalone static recreation of the public Squarespace site, captured 7 November 2026. Includes the homepage, About, Contact and nine case studies at their original URL paths. Swedish text, original layout markup, responsive styles and local fonts are retained. Squarespace runtime scripts and form integration have been removed.

## Preview locally

From this folder run:

    python3 -m http.server 8000

Open http://localhost:8000. A local server is required because links and assets use root-relative paths.

## Publish with GitHub Pages

1. Create a repository named YOUR-USERNAME.github.io (public if using GitHub Free).
2. Upload this folder's contents directly to its root, including `.nojekyll`.
3. In Settings → Pages, choose Deploy from a branch, main, / (root).
4. Test the resulting https://YOUR-USERNAME.github.io site.
5. Only when ready, configure shervanjassim.com in Pages settings and update your domain DNS. No domain records have been changed by this recreation.

Root-relative links target a user Pages site or a custom domain. A project Pages site at /repository-name/ needs its paths adjusted.

## Replace image placeholders

The existing logo is included. Portfolio images are local SVG placeholders with descriptive source filenames. `asset-manifest.json` maps every placeholder to its source page, original public image URL and alt text. Replace the corresponding image references in HTML with the supplied final assets. Repeated references can share one asset. Preserve aspect ratios, and add descriptive alt text for meaningful images.

Local styles and fonts are in assets/. `migration.css` contains standalone overrides; `site.js` controls mobile navigation and the contact form's unconnected state. No build step or package installation is needed.

## Contact form

The form currently validates fields but DOES NOT send messages or save submissions. It explicitly reports that it is not connected and links to LinkedIn. Before launch, connect a form submission service or supply a contact email for a direct email link. Never embed private API keys in these static files.

## Verification

Checked all 12 page files for internal link and asset targets. Browser checked desktop homepage, mobile homepage, mobile navigation and a case-study page. Image placeholders deliberately differ from the original artwork. Review all final assets and connect the form before switching the live domain.
