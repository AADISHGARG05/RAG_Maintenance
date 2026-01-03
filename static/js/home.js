// Navigation function to redirect to chat interface
function navigateToChat() {
    window.location.href = '/ui';
}

document.addEventListener('DOMContentLoaded', function() {
    // 1. Navbar Scroll Effect
    const navbar = document.querySelector('.navbar');
    const scrollProgress = document.querySelector('.scroll-progress');

    window.addEventListener('scroll', () => {
        // Navbar styling
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }

        // Scroll progress bar
        const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
        const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = (winScroll / height) * 100;
        scrollProgress.style.width = scrolled + "%";
    });

    // 2. Intersection Observer for Fade-in Animations
    const observerOptions = {
        threshold: 0.15,
        rootMargin: '0px 0px -50px 0px'
    };

    const revealOnScroll = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                // Optional: stop observing once revealed
                // observer.unobserve(entry.target); 
            }
        });
    }, observerOptions);

    // Apply animation classes to elements
    const animateElements = document.querySelectorAll(
        '.feature-card, .tech-card, .section-header, .system-explanation, .me-text'
    );

    animateElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'all 0.8s cubic-bezier(0.4, 0, 0.2, 1)';
        revealOnScroll.observe(el);
    });

    // Intersection Observer callback to handle the opacity/transform
    const observerStyles = document.createElement('style');
    observerStyles.innerHTML = `
        .active {
            opacity: 1 !important;
            transform: translateY(0) !important;
        }
    `;
    document.head.appendChild(observerStyles);

    // 3. Smooth scroll for internal links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                window.scrollTo({
                    top: target.offsetTop - 80,
                    behavior: 'smooth'
                });
            }
        });
    });

    // 4. Hero entrance animation
    const heroContent = document.querySelector('.hero .container');
    if (heroContent) {
        heroContent.style.opacity = '0';
        heroContent.style.transform = 'scale(0.95)';
        setTimeout(() => {
            heroContent.style.transition = 'all 1s ease-out';
            heroContent.style.opacity = '1';
            heroContent.style.transform = 'scale(1)';
        }, 100);
    }
});