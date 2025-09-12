// Animated Hero with Flapping Butterflies
class AnimatedHero {
    constructor(canvasId) {
        this.canvas = document.getElementById(canvasId);
        this.ctx = this.canvas.getContext('2d');
        this.butterflies = [];
        this.sparkles = [];
        this.animationId = null;
        
        this.init();
    }
    
    init() {
        this.setupCanvas();
        this.createButterflies();
        this.createSparkles();
        this.animate();
    }
    
    setupCanvas() {
        this.canvas.width = 500;
        this.canvas.height = 400;
        
        // Create gradient background
        const gradient = this.ctx.createLinearGradient(0, 0, this.canvas.width, this.canvas.height);
        gradient.addColorStop(0, '#667eea');
        gradient.addColorStop(1, '#764ba2');
        
        this.ctx.fillStyle = gradient;
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
    }
    
    createButterflies() {
        const butterflyCount = 6;
        for (let i = 0; i < butterflyCount; i++) {
            this.butterflies.push({
                x: Math.random() * this.canvas.width,
                y: Math.random() * this.canvas.height,
                vx: (Math.random() - 0.5) * 2,
                vy: (Math.random() - 0.5) * 2,
                wingPhase: Math.random() * Math.PI * 2,
                wingSpeed: 0.1 + Math.random() * 0.1,
                size: 15 + Math.random() * 10,
                color: this.getRandomColor(),
                rotation: Math.random() * Math.PI * 2
            });
        }
    }
    
    createSparkles() {
        const sparkleCount = 8;
        for (let i = 0; i < sparkleCount; i++) {
            this.sparkles.push({
                x: Math.random() * this.canvas.width,
                y: Math.random() * this.canvas.height,
                phase: Math.random() * Math.PI * 2,
                speed: 0.02 + Math.random() * 0.03,
                size: 2 + Math.random() * 3
            });
        }
    }
    
    getRandomColor() {
        const colors = [
            '#ff6b6b', '#ffd93d', '#6bcf7f', '#4d9de0', 
            '#ff9ff3', '#54a0ff', '#5f27cd', '#00d2d3'
        ];
        return colors[Math.floor(Math.random() * colors.length)];
    }
    
    drawButterfly(butterfly) {
        this.ctx.save();
        this.ctx.translate(butterfly.x, butterfly.y);
        this.ctx.rotate(butterfly.rotation);
        
        // Wing flapping animation
        const wingOffset = Math.sin(butterfly.wingPhase) * 0.3;
        
        // Left wing
        this.ctx.fillStyle = butterfly.color;
        this.ctx.beginPath();
        this.ctx.ellipse(-butterfly.size/3, -butterfly.size/4 + wingOffset, 
                        butterfly.size/2, butterfly.size/3, 
                        -0.3 + wingOffset, 0, Math.PI * 2);
        this.ctx.fill();
        
        // Right wing
        this.ctx.beginPath();
        this.ctx.ellipse(butterfly.size/3, -butterfly.size/4 + wingOffset, 
                        butterfly.size/2, butterfly.size/3, 
                        0.3 - wingOffset, 0, Math.PI * 2);
        this.ctx.fill();
        
        // Body
        this.ctx.fillStyle = '#2c3e50';
        this.ctx.fillRect(-2, -butterfly.size/2, 4, butterfly.size);
        
        // Antennae
        this.ctx.strokeStyle = '#2c3e50';
        this.ctx.lineWidth = 1;
        this.ctx.beginPath();
        this.ctx.moveTo(-3, -butterfly.size/2);
        this.ctx.lineTo(-5, -butterfly.size/2 - 5);
        this.ctx.moveTo(3, -butterfly.size/2);
        this.ctx.lineTo(5, -butterfly.size/2 - 5);
        this.ctx.stroke();
        
        this.ctx.restore();
    }
    
    drawSparkle(sparkle) {
        const alpha = Math.sin(sparkle.phase) * 0.5 + 0.5;
        this.ctx.fillStyle = `rgba(255, 255, 255, ${alpha})`;
        this.ctx.beginPath();
        this.ctx.arc(sparkle.x, sparkle.y, sparkle.size, 0, Math.PI * 2);
        this.ctx.fill();
        
        // Add cross sparkle effect
        this.ctx.strokeStyle = `rgba(255, 255, 255, ${alpha * 0.7})`;
        this.ctx.lineWidth = 1;
        this.ctx.beginPath();
        this.ctx.moveTo(sparkle.x - sparkle.size * 2, sparkle.y);
        this.ctx.lineTo(sparkle.x + sparkle.size * 2, sparkle.y);
        this.ctx.moveTo(sparkle.x, sparkle.y - sparkle.size * 2);
        this.ctx.lineTo(sparkle.x, sparkle.y + sparkle.size * 2);
        this.ctx.stroke();
    }
    
    updateButterflies() {
        this.butterflies.forEach(butterfly => {
            // Update position
            butterfly.x += butterfly.vx;
            butterfly.y += butterfly.vy;
            
            // Update wing animation
            butterfly.wingPhase += butterfly.wingSpeed;
            
            // Update rotation based on movement
            butterfly.rotation = Math.atan2(butterfly.vy, butterfly.vx);
            
            // Bounce off edges
            if (butterfly.x < 0 || butterfly.x > this.canvas.width) {
                butterfly.vx *= -1;
            }
            if (butterfly.y < 0 || butterfly.y > this.canvas.height) {
                butterfly.vy *= -1;
            }
            
            // Keep butterflies in bounds
            butterfly.x = Math.max(0, Math.min(this.canvas.width, butterfly.x));
            butterfly.y = Math.max(0, Math.min(this.canvas.height, butterfly.y));
        });
    }
    
    updateSparkles() {
        this.sparkles.forEach(sparkle => {
            sparkle.phase += sparkle.speed;
        });
    }
    
    draw() {
        // Clear canvas with gradient
        const gradient = this.ctx.createLinearGradient(0, 0, this.canvas.width, this.canvas.height);
        gradient.addColorStop(0, '#667eea');
        gradient.addColorStop(1, '#764ba2');
        
        this.ctx.fillStyle = gradient;
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
        
        // Draw sparkles
        this.sparkles.forEach(sparkle => this.drawSparkle(sparkle));
        
        // Draw butterflies
        this.butterflies.forEach(butterfly => this.drawButterfly(butterfly));
        
        // Draw title
        this.ctx.fillStyle = 'rgba(255, 255, 255, 0.9)';
        this.ctx.font = 'bold 32px Arial';
        this.ctx.textAlign = 'center';
        this.ctx.fillText('Data Governance', this.canvas.width/2, 80);
        
        this.ctx.font = '18px Arial';
        this.ctx.fillText('Transforming Data into Strategic Assets', this.canvas.width/2, 110);
    }
    
    animate() {
        this.updateButterflies();
        this.updateSparkles();
        this.draw();
        
        this.animationId = requestAnimationFrame(() => this.animate());
    }
    
    stop() {
        if (this.animationId) {
            cancelAnimationFrame(this.animationId);
        }
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    const animatedHero = new AnimatedHero('animated-hero-canvas');
});
