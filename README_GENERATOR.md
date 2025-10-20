# MicroSite Generator

Automated tool for creating professional B2B microsites from JSON configuration files.

## Quick Start

### 1. Create a configuration file

Copy the example and customize it:
```bash
cp example_config.json my_client_config.json
```

Edit `my_client_config.json` with your client's information.

### 2. Generate the microsite

```bash
python create_microsite.py my_client_config.json ClientNameMicroSite.html
```

### 3. Done!

Your microsite is ready. Open it in a browser to preview.

## Files

- `MicroSite_Template.html` - The base HTML template
- `create_microsite.py` - The generator script
- `config_schema.json` - JSON schema reference
- `example_config.json` - Example configuration
- `Template_Instructions.md` - Detailed documentation

## Configuration Structure

Your config file needs these sections:

```json
{
  "site": {
    "title": "Page title",
    "description": "SEO description",
    "url": "https://your-domain.com/page.html"
  },
  "branding": {
    "company_name": "Your Company",
    "logo_path": "images/logo.png",
    "footer_logo_path": "images/logo-white.png",
    "footer_text": "© 2025 Your Company. Tagline."
  },
  "hero": {
    "title": "Hero headline",
    "subtitle": "Hero subtitle",
    "image_path": "images/hero.jpg",
    "image_alt": "Hero image description",
    "primary_cta": {
      "text": "Main Button",
      "link": "#section"
    },
    "secondary_cta": {
      "text": "Secondary Button",
      "link": "#resources"
    }
  },
  "sections": {
    "about": {
      "description": "About us text...",
      "image_path": "images/about.jpg",
      "image_alt": "About image"
    },
    "partners": {
      "description": "Partners text...",
      "image_path": "images/partners.png",
      "image_alt": "Partners"
    },
    "services": {
      "title": "Our Services",
      "description": "Services overview...",
      "items": [
        {
          "name": "Service 1",
          "description": "Service description...",
          "icon_path": "images/icon1.png"
        }
      ]
    },
    "detailed_service": {
      "title": "Feature Title",
      "description": "Feature description...",
      "feature_title": "Key Capabilities",
      "feature_description": "Feature details...",
      "feature_list": [
        "Feature point 1",
        "Feature point 2",
        "Feature point 3"
      ],
      "feature_image_path": "images/feature.jpg",
      "feature_image_alt": "Feature image",
      "videos": [
        {
          "url": "https://www.youtube.com/embed/VIDEO_ID",
          "title": "Video Title"
        }
      ]
    },
    "resources": {
      "description": "Resources intro...",
      "items": [
        {
          "title": "Resource Title",
          "name": "Document Name",
          "description": "Description...",
          "url": "documents/file.pdf",
          "button_text": "Download PDF"
        }
      ]
    }
  }
}
```

## Tips

- **Paths**: Use relative paths for images (e.g., `images/logo.png`)
- **URLs**: For videos, use YouTube embed URLs
- **Testing**: Generate and preview frequently while building your config
- **Validation**: The script will warn you if placeholders remain
- **Customization**: After generation, you can still edit the HTML manually

## Workflow Comparison

### Before (Manual)
1. Copy template
2. Find and replace 40+ placeholders manually
3. Risk of missing placeholders
4. Hard to regenerate if you make mistakes

### After (Automated)
1. Edit JSON config
2. Run script
3. Done in seconds
4. Easy to regenerate anytime

## Troubleshooting

**Script won't run:**
```bash
python create_microsite.py example_config.json test.html
```

**Check for Python:**
```bash
python --version
```
or
```bash
python3 create_microsite.py example_config.json test.html
```

**JSON syntax errors:**
- Validate your JSON at https://jsonlint.com
- Common issues: missing commas, trailing commas, unescaped quotes

**Remaining placeholders:**
- Check the warning message from the script
- Compare your config to `example_config.json`
- Some placeholders may need manual replacement

## Support

For detailed instructions, see `Template_Instructions.md`.

For issues or questions, refer to the original template documentation.
