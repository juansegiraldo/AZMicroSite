# Video Setup Instructions

## How to Replace Video Placeholders with YouTube Embeds

### Step 1: Upload Videos to YouTube
1. Go to [YouTube Studio](https://studio.youtube.com)
2. Click "Create" → "Upload videos"
3. Upload your videos:
   - `catalogue.mp4` → Name it "Data Catalog Demo"
   - `Data Quality.mp4` → Name it "Data Quality Demonstration" 
   - `Lineage.mp4` → Name it "Lineage Functionality Demo"
4. Set visibility to **"Unlisted"** (only people with the link can see them)
5. Copy the video IDs from the URLs

### Step 2: Replace Video IDs in HTML
Open `index.html` and replace these placeholders:

1. **Lineage Videos** (around line 129):
   ```html
   src="https://www.youtube.com/embed/YOUR_VIDEO_ID_1"
   src="https://www.youtube.com/embed/YOUR_VIDEO_ID_2"
   ```

2. **Data Quality Video** (around line 193):
   ```html
   src="https://www.youtube.com/embed/YOUR_DATA_QUALITY_VIDEO_ID"
   ```

### Step 3: Get Video IDs
From YouTube URLs like `https://www.youtube.com/watch?v=ABC123XYZ`, the video ID is `ABC123XYZ`

### Step 4: Test Your Site
1. Open `index.html` in your browser
2. Check that videos load properly
3. Test on mobile devices
4. Verify videos are unlisted (not public)

## Alternative Hosting Options

### Option 1: Vimeo (More Professional)
- Upload to Vimeo
- Use embed code: `<iframe src="https://player.vimeo.com/video/VIDEO_ID" ...>`

### Option 2: GitHub Releases
- Create a new release in your GitHub repo
- Upload videos as release assets
- Link directly: `https://github.com/USERNAME/REPO/releases/download/v1.0/video.mp4`

### Option 3: Cloud Storage
- Upload to AWS S3, Google Drive, or Dropbox
- Get public sharing links
- Use as video sources: `<video src="CLOUD_URL" controls>`

## Benefits of YouTube Solution
✅ No file size limits  
✅ Automatic video optimization  
✅ Global CDN for fast loading  
✅ Mobile-friendly responsive player  
✅ Analytics and engagement tracking  
✅ Free hosting  
✅ Easy to update videos  

## Current Video Files in Repository
- `images/catalogue.mp4` - Not currently used in HTML
- `images/Data Quality.mp4` - Should replace Data Quality placeholder
- `images/Lineage.mp4` - Should replace Lineage placeholders

After uploading to YouTube, you can safely delete these video files from your repository to reduce its size.
