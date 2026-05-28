const toggle = document.querySelector("[data-menu-toggle]");
const navLinks = document.querySelector("[data-nav-links]");

if (toggle && navLinks) {
  toggle.addEventListener("click", () => {
    const isOpen = navLinks.classList.toggle("open");
    toggle.setAttribute("aria-expanded", String(isOpen));
  });
}

document.querySelectorAll("[data-year]").forEach((node) => {
  node.textContent = new Date().getFullYear();
});

document.querySelectorAll("[data-payment-placeholder]").forEach((link) => {
  link.addEventListener("click", (event) => {
    const href = link.getAttribute("href") || "";
    if (href.startsWith("#PAYMENT_LINK_")) {
      event.preventDefault();
      alert("Payment checkout link is not connected yet. Replace this placeholder with your real checkout URL. Set the checkout success/return URL to after-purchase.html.");
    }
  });
});
