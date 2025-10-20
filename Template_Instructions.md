# MicroSite Template Instructions

## Overview
This template (`MicroSite_Template.html`) is based on the AZMicroSite.html structure and provides a clean, reusable foundation for creating professional B2B microsites. It includes preserved sections and placeholders for easy customization.

## ⚡ Quick Start - Automated Workflow (RECOMMENDED)

The fastest way to create a new microsite is using the automated generator:

### Step 1: Create Your Config File
Copy and customize the example configuration:
```bash
cp example_config.json my_client_config.json
```

Edit `my_client_config.json` with your client's information. The config file includes:
- Site metadata (title, description, URL)
- Branding (company name, logos, footer)
- Hero section (title, subtitle, CTAs, image)
- Content sections (about, partners, services, resources)

See `config_schema.json` for the complete structure reference.

### Step 2: Generate Your Microsite
Run the generator script:
```bash
python create_microsite.py my_client_config.json ClientNameMicroSite.html
```

That's it! Your new microsite is ready.

### Step 3: Preview and Refine
1. Open the generated HTML file in your browser
2. Check that all content appears correctly
3. Make any manual customizations if needed

### Benefits of the Automated Workflow
- ✓ **Fast**: Generate a complete microsite in seconds
- ✓ **Consistent**: No missed placeholders or typos
- ✓ **Version Control**: Track changes through JSON config files
- ✓ **Repeatable**: Easily regenerate if you need to make changes
- ✓ **Documentation**: Config files serve as documentation

## Preserved Sections
The following sections are kept intact from the original:
- **Header/Navigation**: Complete navigation structure with logo placeholder
- **Hero Section**: Main banner with title, subtitle, and CTA buttons
- **Footer**: Simple footer with logo and copyright
- **Resources Section**: Document download and resource showcase area

## Template Structure

### 1. Header Section
- Company logo placeholder: `[PLACEHOLDER: Company Logo Path]`
- Navigation menu with standard links (Home, About Us, Partners, Services, Resources)
- Responsive hamburger menu for mobile

### 2. Hero Section
- Main title with client logo integration
- Subtitle for value proposition
- Two CTA buttons (primary and secondary actions)
- Hero image on the right side

### 3. About Us Section
- Company description
- Large image showcase
- Centered layout

### 4. Partners Section
- Partners description
- Partners logo/image showcase
- Centered layout

### 5. Example Sections (Customizable)

#### Services Section
- Grid layout for service cards
- Each service card includes:
  - Icon/image
  - Service name
  - Service description

#### Detailed Service Section
- Feature description with bullet points
- Image showcase
- Video embeds (2 videos side by side)
- Content grid layout

### 6. Resources Section
- Resource boxes for documents
- PDF preview with download links
- Placeholder for additional resources

## Configuration File Reference

The JSON configuration file structure:

```json
{
  "site": {
    "title": "Page title for browser tab",
    "description": "SEO meta description",
    "url": "Full URL where site will be hosted"
  },
  "branding": {
    "company_name": "Your company name",
    "logo_path": "images/logo.png",
    "footer_logo_path": "images/logo-white.png",
    "footer_text": "© 2025 Company Name. Tagline."
  },
  "hero": {
    "title": "Main headline",
    "subtitle": "Supporting text",
    "image_path": "images/hero.jpg",
    "image_alt": "Alt text for hero image",
    "primary_cta": {
      "text": "Button text",
      "link": "#section-id"
    },
    "secondary_cta": {
      "text": "Button text",
      "link": "#another-section"
    }
  },
  "sections": {
    "about": { ... },
    "partners": { ... },
    "services": { ... },
    "detailed_service": { ... },
    "resources": { ... }
  }
}
```

See `example_config.json` for a complete, working example.

---

## Manual Workflow (Legacy)

If you prefer to work directly with HTML, you can still use the manual approach:

### Step 1: Replace Placeholders
Search and replace all `[PLACEHOLDER: ...]` text with your actual content:

#### Essential Placeholders:
- `[PLACEHOLDER: Company Name]` - Your company name
- `[PLACEHOLDER: Site Title]` - Main page title
- `[PLACEHOLDER: Site Description]` - Meta description
- `[PLACEHOLDER: Company Logo Path]` - Path to your logo
- `[PLACEHOLDER: Client Logo Path]` - Path to client logo (if applicable)
- `[PLACEHOLDER: Hero Image Path]` - Path to hero image

#### Content Placeholders:
- `[PLACEHOLDER: Main Hero Title]` - Main headline
- `[PLACEHOLDER: Hero Subtitle]` - Subtitle text
- `[PLACEHOLDER: Primary CTA Text]` - Primary button text
- `[PLACEHOLDER: Secondary CTA Text]` - Secondary button text

### Step 2: Customize Sections
You can:
- **Add new sections**: Copy the structure of existing sections
- **Remove sections**: Delete entire section blocks
- **Modify layouts**: Change grid structures, add/remove columns
- **Update styling**: Modify CSS classes or add custom styles

### Step 3: Add Your Content
- Replace placeholder images with your actual images
- Update all text content
- Add your YouTube video URLs
- Update resource links and documents

## Agent Instructions for Template Usage

When a user wants to create a new microsite:

### Automated Approach (RECOMMENDED)

1. **Create a config file**:
   - Copy `example_config.json` to a new file (e.g., `client_name_config.json`)
   - Ask the user for all required information:
     - Site metadata (title, description, URL)
     - Branding (company name, logos)
     - Hero section content
     - Section content (about, partners, services, resources)
     - Images and media paths

2. **Fill the config file**:
   - Populate the JSON with the user's information
   - Ensure all required fields are filled
   - Use the schema (`config_schema.json`) as reference

3. **Generate the microsite**:
   - Run: `python create_microsite.py client_name_config.json ClientNameMicroSite.html`
   - Review the output for any warnings
   - Check for remaining placeholders

4. **Manual refinements** (if needed):
   - Add custom sections not covered by template
   - Adjust styling or layout
   - Add special features

### Manual Approach (Legacy)

If the user needs extensive customization beyond the template structure:

1. **Copy the template**: Start with `MicroSite_Template.html`
2. **Replace placeholders systematically** following the sections below
3. **Customize sections** as needed
4. **Test responsiveness**

## File Structure Requirements
Make sure you have these files in your project:
- `css/main.css` - Main stylesheet
- `css/responsive.css` - Responsive styles
- `js/main.js` - Main JavaScript functionality
- `js/animated-hero.js` - Hero animations
- `images/` folder with your assets

## Common Customizations

### Adding a New Section
```html
<section id="new-section" class="new-section">
    <div class="container">
        <div class="section-header">
            <h2>Section Title</h2>
            <p>Section Description</p>
        </div>
        <!-- Your content here -->
    </div>
</section>
```

### Adding a Service Card
```html
<div class="service-card">
    <div class="service-icon">
        <img src="path/to/icon.png" alt="Service Name">
    </div>
    <h3>Service Name</h3>
    <p>Service Description</p>
</div>
```

### Adding a Video
```html
<div class="video-embed">
    <iframe width="100%" height="200" 
            src="https://www.youtube.com/embed/VIDEO_ID" 
            title="Video Title"
            frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen>
    </iframe>
</div>
```

## Tips for Success
- Keep placeholder text descriptive to make replacement easier
- Test all links and media embeds
- Ensure images are optimized for web
- Maintain consistent branding throughout
- Use semantic HTML structure
- Test on multiple devices and browsers




