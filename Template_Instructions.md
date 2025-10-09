# MicroSite Template Instructions

## Overview
This template (`MicroSite_Template.html`) is based on the AZMicroSite.html structure and provides a clean, reusable foundation for creating professional B2B microsites. It includes preserved sections and placeholders for easy customization.

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

## How to Use This Template

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

When a user wants to create a new microsite using this template:

1. **Copy the template**: Start with `MicroSite_Template.html`
2. **Identify requirements**: Ask the user for:
   - Company name and branding
   - Client name (if applicable)
   - Main value proposition
   - Specific sections they want
   - Images and media they have
   - Any custom functionality needed

3. **Replace placeholders systematically**:
   - Start with meta tags and titles
   - Update navigation and branding
   - Customize hero section
   - Fill in content sections
   - Update resources and footer

4. **Customize sections based on needs**:
   - Add/remove service cards
   - Modify video embeds
   - Adjust image layouts
   - Add custom features

5. **Test responsiveness**: Ensure the site works on mobile devices

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



