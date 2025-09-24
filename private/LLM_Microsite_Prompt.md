# 🚀 LLM Coding Agent Prompt: AstraZeneca Microsite Development

## 📋 Project Overview
You are tasked with building a professional microsite for Stratesys to present their capabilities to AstraZeneca. This is a B2B presentation focused on Data Governance and Advisory services.

## ⚠️ CRITICAL INSTRUCTIONS - READ FIRST

### 🚫 DO NOT INVENT CONTENT
- **NEVER create fake company information, team photos, or case studies**
- **NEVER generate placeholder text that sounds like real content**
- **NEVER create fake testimonials or client logos**
- **NEVER invent specific project details or metrics**

### 📸 PLACEHOLDER REQUIREMENTS
- **ALL images, videos, and logos MUST use clear placeholder elements**
- **Use descriptive placeholder text that indicates what content is needed**
- **Make placeholders visually distinct and professional**
- **Include alt text for accessibility**

## 🎯 Technical Requirements

### Framework & Structure
- **Technology Stack**: HTML5, CSS3, JavaScript (vanilla or modern framework)
- **Responsive Design**: Mobile-first approach, works on all devices
- **Browser Support**: Modern browsers (Chrome, Firefox, Safari, Edge)
- **Performance**: Fast loading, optimized assets
- **Accessibility**: WCAG 2.1 AA compliance

### File Structure
```
/
├── index.html
├── css/
│   ├── main.css
│   └── responsive.css
├── js/
│   └── main.js
├── images/
│   └── placeholders/
└── videos/
    └── placeholders/
```

## 🎨 Design Specifications

### Color Palette
- **Primary**: Professional blue ( #00456E)
- **Secondary**: Neutral grays ( #6b7280, #9ca3af)
- **Background**: White ( #ffffff) and light gray ( #f9fafb)
- **Accent**: AZ's yellow or purple s ( #FCAF16 or  #8C0954)
- **Text**: Dark gray ( #374151) for body, darker ( #111827) for headings

### Typography
- **Primary Font**: Inter, Roboto, or Open Sans (Google Fonts)
- **Hierarchy**: Clear distinction between H1-H6 and body text
- **Sizes**: Responsive typography scale
- **Line Height**: 1.5-1.6 for readability

### Layout Principles
- **Grid System**: CSS Grid or Flexbox
- **White Space**: Generous padding and margins
- **Modular Design**: Reusable components
- **Clean Navigation**: Sticky header with smooth scrolling

## 📄 Page Structure & Content

### 1. Home Page (index.html)
**Hero Section:**
- [PLACEHOLDER: Hero image with Stratesys branding - healthcare/innovation theme]
- Main headline: "Our proposal for AstraZeneca: Data Governance, Security and Advisory with measurable impact"
- [PLACEHOLDER: Call-to-action buttons to main sections]

**Navigation:**
- About Us
- Data Governance
- Advisory
- Actionables
- Compliance
- Contact

### 2. About Us Section
**Content:**
- [PLACEHOLDER: Company background story - DO NOT INVENT]
- Core capabilities: Data Driven Business and Data Governance
- [PLACEHOLDER: Institutional/team image - professional corporate photo]

### 3. Data Governance Section

#### 3.1 Overview
- Clear explanation of Data Governance concepts
- Benefits for AstraZeneca (regulatory compliance, operational efficiency, data security)
- Focus areas: Lineage & Catalogue, Security, Data Quality

#### 3.1.1 Datasphere Catalog & Lineage
- [PLACEHOLDER: 1 image showing catalog interface]
- [PLACEHOLDER: 2 videos demonstrating lineage functionality]

#### 3.1.1.1 SAP & Collibra Integration
- Explanation of integration benefits
- [PLACEHOLDER: Infographic showing SAP-Collibra integration flow]

#### 3.1.2 Data Quality
- [PLACEHOLDER: Image 1 - Data quality process diagram]
- [PLACEHOLDER: Image 2 - Process explained in Datasphere interface]
- [PLACEHOLDER: Image 3 - Data Quality dashboard in Datasphere]
- [PLACEHOLDER: Video - Data Quality demonstration in Datasphere]

#### 3.1.3 Security
- [PLACEHOLDER: Image - Security administration monitor in SAP Analytics Cloud]
- [PLACEHOLDER: Image - Access Automation App process in SAC]

### 4. Advisory Section

#### 4.1 SAP Datasphere Advisory
- Quality, compliance, risks and best practices focus

#### 4.1.1 Documentation Review
- Why: Guarantees quality and alignment
- What: Functional & technical designs, test documents, KPIs, reconciliation guides

#### 4.1.2 Developments Review
- Why: Ensures correct use of spaces and structures
- What: Queries, models, dataflows, consistency checks

#### 4.1.3 Best Practices & Compliance
- Why: Meets standards and security requirements
- What: Roles & authorizations, technical names validation, versioning

#### 4.1.4 Architecture Review
- Why: Clear architecture definition and responsibilities
- What: Guidelines on "where to do what", compliance with best practices

#### 4.2 Advisory Process
- [PLACEHOLDER: Visual diagram - 3-step process]
  - Step 1: Review
  - Step 2: Recommendations
  - Step 3: Implementation

### 5. Actionables Section
- [PLACEHOLDER: 7 service boxes - DO NOT INVENT specific services]
- Use generic service descriptions with placeholders

### 6. Compliance Section
- [PLACEHOLDER: Compliance documents and certifications]
- [PLACEHOLDER: Download area for PDFs and resources]
- Supplier onboarding information

## 🖼️ Placeholder Specifications

### Image Placeholders
```html
<!-- Example format for all image placeholders -->
<div class="placeholder-image">
  <div class="placeholder-content">
    <i class="icon-camera"></i>
    <p>[PLACEHOLDER: Hero image with Stratesys branding - healthcare/innovation theme]</p>
    <span class="placeholder-dimensions">1920x1080px</span>
  </div>
</div>
```

### Video Placeholders
```html
<!-- Example format for all video placeholders -->
<div class="placeholder-video">
  <div class="placeholder-content">
    <i class="icon-play"></i>
    <p>[PLACEHOLDER: Data Quality demonstration video]</p>
    <span class="placeholder-duration">2-3 minutes</span>
  </div>
</div>
```

### Logo Placeholders
```html
<!-- Example format for logo placeholders -->
<div class="placeholder-logo">
  <div class="placeholder-content">
    <i class="icon-logo"></i>
    <p>[PLACEHOLDER: Stratesys logo]</p>
  </div>
</div>
```

## 🎨 CSS Styling for Placeholders

```css
.placeholder-image,
.placeholder-video,
.placeholder-logo {
  background: #f3f4f6;
  border: 2px dashed #d1d5db;
  border-radius: 8px;
  padding: 2rem;
  text-align: center;
  color: #6b7280;
  min-height: 200px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.placeholder-content i {
  font-size: 2rem;
  margin-bottom: 1rem;
  display: block;
}

.placeholder-dimensions,
.placeholder-duration {
  font-size: 0.875rem;
  color: #9ca3af;
  font-style: italic;
}
```

## 📱 Responsive Design Requirements

### Breakpoints
- Mobile: 320px - 768px
- Tablet: 768px - 1024px
- Desktop: 1024px+

### Mobile Considerations
- Touch-friendly navigation
- Readable text without zooming
- Fast loading on mobile networks
- Swipe gestures for image galleries

## 🚀 Performance Requirements

### Optimization
- Compressed images (when real images are added)
- Minified CSS and JavaScript
- Lazy loading for images and videos
- Fast loading times (< 3 seconds)

### SEO Considerations
- Semantic HTML structure
- Meta tags and descriptions
- Alt text for all images
- Proper heading hierarchy

## 📋 Deliverables Checklist

- [ ] Complete HTML structure with all sections
- [ ] Responsive CSS with professional styling
- [ ] Interactive JavaScript for navigation and interactions
- [ ] All image placeholders with descriptive text
- [ ] All video placeholders with duration estimates
- [ ] All logo placeholders clearly marked
- [ ] Mobile-responsive design
- [ ] Accessibility features implemented
- [ ] Clean, commented code
- [ ] README with setup instructions

## 🔧 Development Guidelines

### Code Quality
- Clean, semantic HTML
- Well-organized CSS with comments
- Modular JavaScript functions
- Consistent naming conventions
- Cross-browser compatibility

### Content Guidelines
- Professional, executive tone
- Clear value propositions
- Benefit-focused messaging
- Industry-specific language for pharma/healthcare

## 📞 Contact Information Placeholder
- [PLACEHOLDER: Contact form with validation]
- [PLACEHOLDER: Company contact details]
- [PLACEHOLDER: Office locations and addresses]

---

**Remember**: This is a presentation microsite for a real business proposal. Maintain professionalism, avoid inventing content, and ensure all placeholders are clearly marked and descriptive.
