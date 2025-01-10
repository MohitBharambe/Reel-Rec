// Transition Animation
function delay(n) {
    n = n || 2000;
    return new Promise((done) => {
        setTimeout(() => {
            done();
        }, n);
    });
}

function pageTransition() {
    var tl = gsap.timeline();
    tl.to(".loading-screen", {
        duration: 0.4,
        width: "100%",
        left: "0%",
        ease: "Expo.easeInOut",
    });

    tl.to(".loading-screen", {
        duration: 0.4,
        width: "100%",
        left: "100%",
        ease: "Expo.easeInOut",
        delay: 0.3,
    });
    tl.set(".loading-screen", { left: "-100%" });
}

// GSAP Animation
function contentAnimation() {
    var tl = gsap.timeline();
    tl.from(".animate-this", { duration: 0.6, y: 40, opacity: 0, stagger: 0.3, delay: 0.3 });
}

// Move the rec button to the bottom of the page when 3 or more checkboxes are checked.
function initCheckboxListener() {
    const checkboxes = document.querySelectorAll('.selection-checkbox');
    const button = document.getElementById('get-recommendations');

    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            const selectedCount = document.querySelectorAll('.selection-checkbox:checked').length;
            if (selectedCount >= 3) {
                button.classList.add('fixed-bottom');
            } else {
                button.classList.remove('fixed-bottom');
            }
        });
    });
}

// Event Listeners for Page Transitions
document.addEventListener('DOMContentLoaded', function() {
    barba.init({
        sync: true,

        transitions: [
            {
                async leave(data) {
                    const done = this.async();

                    pageTransition();
                    await delay(500);
                    done();
                },

                async enter(data) {
                    contentAnimation();
                    initCheckboxListener(); 
                },

                async once(data) {
                    contentAnimation();
                    initCheckboxListener(); 
                },
            },
        ],
    });

    initCheckboxListener();
});