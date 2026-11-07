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

## Portfolio images

All 42 portfolio and About image references now use real assets. 24 images were matched from the supplied Site_assets folder; 18 absent files were recovered from the original public Squarespace image URLs. Project-specific folders take precedence over the mixed All_PNG folder when filenames have different versions. `asset-manifest.json` records each page, original URL, local replacement and source. Image files retain their original names.

Local styles and fonts are in assets/. `migration.css` contains standalone overrides; `site.js` controls mobile navigation and the contact form's unconnected state. No build step or package installation is needed.

## Contact form

The form currently validates fields but DOES NOT send messages or save submissions. It explicitly reports that it is not connected and links to LinkedIn. Before launch, connect a form submission service or supply a contact email for a direct email link. Never embed private API keys in these static files.

## Verification

Checked all 12 page files for internal link and asset targets. Browser checked the homepage, mobile navigation, and image loading on all nine case studies; every case-study image decoded successfully. All image references were checked against local files. Connect the form before switching the live domain.
