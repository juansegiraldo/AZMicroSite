#!/usr/bin/env python3
"""
MicroSite Generator
Generates a custom microsite HTML file from a JSON configuration file.

Usage:
    python create_microsite.py <config_file.json> [output_file.html]

Example:
    python create_microsite.py example_config.json AcmeMicroSite.html
"""

import json
import sys
import os
from pathlib import Path


class MicroSiteGenerator:
    def __init__(self, template_path='MicroSite_Template.html'):
        self.template_path = template_path
        self.template_content = None
        self.config = None

    def load_template(self):
        """Load the HTML template file."""
        try:
            with open(self.template_path, 'r', encoding='utf-8') as f:
                self.template_content = f.read()
            print(f"✓ Template loaded: {self.template_path}")
            return True
        except FileNotFoundError:
            print(f"✗ Error: Template file not found: {self.template_path}")
            return False
        except Exception as e:
            print(f"✗ Error loading template: {e}")
            return False

    def load_config(self, config_path):
        """Load and validate the configuration file."""
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
            print(f"✓ Config loaded: {config_path}")
            return True
        except FileNotFoundError:
            print(f"✗ Error: Config file not found: {config_path}")
            return False
        except json.JSONDecodeError as e:
            print(f"✗ Error: Invalid JSON in config file: {e}")
            return False
        except Exception as e:
            print(f"✗ Error loading config: {e}")
            return False

    def replace_placeholder(self, placeholder, value):
        """Replace a placeholder with its value."""
        if value is None:
            value = ""
        placeholder_text = f"[PLACEHOLDER: {placeholder}]"
        if placeholder_text in self.template_content:
            self.template_content = self.template_content.replace(placeholder_text, str(value))
            return True
        return False

    def generate(self):
        """Generate the microsite by replacing all placeholders."""
        if not self.config or not self.template_content:
            print("✗ Error: Config or template not loaded")
            return False

        replacements = 0

        # Site metadata
        replacements += self.replace_placeholder("Site Title", self.config['site']['title'])
        replacements += self.replace_placeholder("Site Description", self.config['site']['description'])
        replacements += self.replace_placeholder("Site URL", self.config['site']['url'])
        replacements += self.replace_placeholder("Hero Image URL", self.config.get('hero', {}).get('image_path', ''))

        # Branding
        replacements += self.replace_placeholder("Company Name", self.config['branding']['company_name'])
        replacements += self.replace_placeholder("Company Logo Path", self.config['branding']['logo_path'])
        replacements += self.replace_placeholder("Footer Logo Path", self.config['branding']['footer_logo_path'])
        replacements += self.replace_placeholder("Footer Text", self.config['branding']['footer_text'])

        # Hero section
        hero = self.config.get('hero', {})
        replacements += self.replace_placeholder("Main Hero Title", hero.get('title', ''))
        replacements += self.replace_placeholder("Hero Subtitle", hero.get('subtitle', ''))
        replacements += self.replace_placeholder("Hero Image Path", hero.get('image_path', ''))
        replacements += self.replace_placeholder("Hero Image Alt Text", hero.get('image_alt', ''))

        # Hero CTAs
        primary_cta = hero.get('primary_cta', {})
        replacements += self.replace_placeholder("Primary CTA Text", primary_cta.get('text', 'Learn More'))
        replacements += self.replace_placeholder("Primary CTA Link", primary_cta.get('link', '#'))

        secondary_cta = hero.get('secondary_cta', {})
        replacements += self.replace_placeholder("Secondary CTA Text", secondary_cta.get('text', 'View Resources'))
        replacements += self.replace_placeholder("Secondary CTA Link", secondary_cta.get('link', '#resources'))

        # About section
        about = self.config.get('sections', {}).get('about', {})
        replacements += self.replace_placeholder("About Us Description", about.get('description', ''))
        replacements += self.replace_placeholder("About Us Image Path", about.get('image_path', ''))
        replacements += self.replace_placeholder("About Us Image Alt Text", about.get('image_alt', ''))

        # Partners section
        partners = self.config.get('sections', {}).get('partners', {})
        replacements += self.replace_placeholder("Partners Description", partners.get('description', ''))
        replacements += self.replace_placeholder("Partners Image Path", partners.get('image_path', ''))
        replacements += self.replace_placeholder("Partners Image Alt Text", partners.get('image_alt', ''))

        # Services section
        services = self.config.get('sections', {}).get('services', {})
        replacements += self.replace_placeholder("Services Section Title", services.get('title', ''))
        replacements += self.replace_placeholder("Services Section Description", services.get('description', ''))

        # Service cards (up to 3)
        service_items = services.get('items', [])
        for i in range(3):
            if i < len(service_items):
                item = service_items[i]
                replacements += self.replace_placeholder(f"Service {i+1} Name", item.get('name', ''))
                replacements += self.replace_placeholder(f"Service {i+1} Description", item.get('description', ''))
                replacements += self.replace_placeholder(f"Service {i+1} Icon Path", item.get('icon_path', ''))
            else:
                # Fill empty slots with placeholders
                replacements += self.replace_placeholder(f"Service {i+1} Name", f"Service {i+1}")
                replacements += self.replace_placeholder(f"Service {i+1} Description", "Description")
                replacements += self.replace_placeholder(f"Service {i+1} Icon Path", "images/icon.png")

        # Detailed service section
        detailed = self.config.get('sections', {}).get('detailed_service', {})
        replacements += self.replace_placeholder("Detailed Service Title", detailed.get('title', ''))
        replacements += self.replace_placeholder("Detailed Service Description", detailed.get('description', ''))
        replacements += self.replace_placeholder("Feature Title", detailed.get('feature_title', ''))
        replacements += self.replace_placeholder("Feature Description", detailed.get('feature_description', ''))

        # Feature list
        feature_list = detailed.get('feature_list', [])
        for i in range(3):
            if i < len(feature_list):
                replacements += self.replace_placeholder(f"Feature {i+1}", feature_list[i])
            else:
                replacements += self.replace_placeholder(f"Feature {i+1}", "")

        # Feature image
        replacements += self.replace_placeholder("Feature Image Path", detailed.get('feature_image_path', ''))
        replacements += self.replace_placeholder("Feature Image Alt Text", detailed.get('feature_image_alt', ''))

        # Videos
        videos = detailed.get('videos', [])
        for i in range(2):
            if i < len(videos):
                video = videos[i]
                replacements += self.replace_placeholder(f"Video {i+1} YouTube URL", video.get('url', ''))
                replacements += self.replace_placeholder(f"Video {i+1} Title", video.get('title', ''))
            else:
                replacements += self.replace_placeholder(f"Video {i+1} YouTube URL", "")
                replacements += self.replace_placeholder(f"Video {i+1} Title", "")

        # Resources section
        resources = self.config.get('sections', {}).get('resources', {})
        replacements += self.replace_placeholder("Resources Description", resources.get('description', ''))

        # Resource items (up to 2)
        resource_items = resources.get('items', [])
        for i in range(2):
            if i < len(resource_items):
                item = resource_items[i]
                replacements += self.replace_placeholder(f"Resource {i+1} Title", item.get('title', ''))
                replacements += self.replace_placeholder(f"Resource {i+1} Name", item.get('name', ''))
                replacements += self.replace_placeholder(f"Resource {i+1} Description", item.get('description', ''))
                replacements += self.replace_placeholder(f"Resource {i+1} URL", item.get('url', ''))
                replacements += self.replace_placeholder(f"Resource {i+1} Button Text", item.get('button_text', 'Download'))
                replacements += self.replace_placeholder(f"Resource {i+1} Status", item.get('status', ''))
            else:
                replacements += self.replace_placeholder(f"Resource {i+1} Title", "")
                replacements += self.replace_placeholder(f"Resource {i+1} Name", "")
                replacements += self.replace_placeholder(f"Resource {i+1} Description", "")
                replacements += self.replace_placeholder(f"Resource {i+1} URL", "")
                replacements += self.replace_placeholder(f"Resource {i+1} Button Text", "")
                replacements += self.replace_placeholder(f"Resource {i+1} Status", "")

        print(f"✓ Replaced {replacements} placeholders")

        # Check for remaining placeholders
        remaining_placeholders = self.template_content.count('[PLACEHOLDER:')
        if remaining_placeholders > 0:
            print(f"⚠ Warning: {remaining_placeholders} placeholders still remain in the output")
            print("  You may need to manually replace these or add them to your config file")

        return True

    def save(self, output_path):
        """Save the generated microsite to a file."""
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(self.template_content)
            print(f"✓ Microsite generated successfully: {output_path}")
            return True
        except Exception as e:
            print(f"✗ Error saving file: {e}")
            return False


def main():
    """Main entry point for the script."""
    if len(sys.argv) < 2:
        print("Usage: python create_microsite.py <config_file.json> [output_file.html]")
        print("\nExample:")
        print("  python create_microsite.py example_config.json AcmeMicroSite.html")
        sys.exit(1)

    config_file = sys.argv[1]

    # Generate output filename from config filename if not provided
    if len(sys.argv) >= 3:
        output_file = sys.argv[2]
    else:
        config_name = Path(config_file).stem
        output_file = f"{config_name}_MicroSite.html"

    print("=" * 60)
    print("MicroSite Generator")
    print("=" * 60)

    # Create generator instance
    generator = MicroSiteGenerator()

    # Load template
    if not generator.load_template():
        sys.exit(1)

    # Load config
    if not generator.load_config(config_file):
        sys.exit(1)

    # Generate microsite
    print("\nGenerating microsite...")
    if not generator.generate():
        sys.exit(1)

    # Save output
    if not generator.save(output_file):
        sys.exit(1)

    print("=" * 60)
    print("✓ Done!")
    print(f"\nYour new microsite is ready: {output_file}")
    print("\nNext steps:")
    print("  1. Open the file in a browser to preview")
    print("  2. Check for any remaining placeholders")
    print("  3. Customize as needed")
    print("=" * 60)


if __name__ == '__main__':
    main()
