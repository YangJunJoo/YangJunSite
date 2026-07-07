# Yang-Jun Joo, Ph.D. - Applied Researcher Portfolio

This is a professional, industry-facing personal portfolio website for **Yang-Jun Joo, Ph.D.** built using Astro, TypeScript, and Tailwind CSS. The website is positioned specifically for roles in **autonomous driving safety, mobility AI, transportation safety analytics, and large-scale mobility data science**.

## Tech Stack
* **Framework:** Astro (Static Site Architecture)
* **Styling:** Tailwind CSS (Vanilla styling and grid systems)
* **Language:** TypeScript
* **Content Source:** Static YAML content files (No database required)

---

## Getting Started

### 1. Installation

If Node.js is already installed on your system, run:
```bash
npm install
```

*Note: If Node.js is not installed, you can use the portable Node environment downloaded in the `node/` folder:*
```powershell
# Prepend portable node to PATH (Windows PowerShell)
$env:PATH = "$(pwd)\node;" + $env:PATH
npm install
```

### 2. Local Development

To run the development server locally:
```bash
npm run dev
```

The site will be available at [http://localhost:4321](http://localhost:4321).

### 3. Build for Production

To build the static site (output will be in the `dist/` directory):
```bash
npm run build
```

---

## Customizing Content

All main content is modular and driven by YAML files located under `src/content/`. You can edit these files to customize the website text without touching the components:

1. **Profile Data (`src/content/profile.yaml`):**
   * Change your name, contact email, social profile links, and the 4 core research focus areas.
   * Replace the placeholder CV file in the `public/YangJunJoo_CV.pdf` path with your real PDF curriculum vitae.

2. **Projects Data (`src/content/projects.yaml`):**
   * Customize details, category tags, status, problem statements, and industry value fields for all projects.
   * Toggle `featured: true` or `false` to select which projects are highlighted on the Home page.

3. **Publications Data (`src/content/publications.yaml`):**
   * Keep your publications organized under the three primary industry-facing groups.
   * Customize author lists, summaries, and industry value tags.

4. **Skills Data (`src/content/skills.yaml`):**
   * Group skills into Data & Programming, Machine Learning & AI, Transportation Safety, and Research Translation.
   * Provide bulleted or paragraph-based explanations for each.

5. **Experience Data (`src/content/experience.yaml`):**
   * Edit roles, institutions, dates, advisors, and bullet points.
   * Edit education degrees and academic sources.

---

## Deployment

Since the site builds to pure static HTML/CSS/JS (in the `dist/` folder), it can be deployed for free on any static host.

### GitHub Pages
1. Push your code to a GitHub repository.
2. Go to **Settings > Pages**.
3. Choose **GitHub Actions** under Source.
4. Add an Astro deployment workflow (Astro has an official template). It will automatically build and publish the `dist/` directory.

### Vercel / Netlify
1. Connect your repository to Vercel or Netlify.
2. Configure the build command as `npm run build`.
3. Set the output directory to `dist`.
4. Deploy!
