# Valtori Security Website

Static GitHub Pages website for Valtori Security.

## Files

- `index.html` - Home page
- `shop.html` - Pricing and services
- `reviews.html` - Testimonials
- `contact.html` - Contact form and contact information
- `after-purchase.html` - Remote support software instructions
- `assets/logo.png` - Site logo, navbar logo, footer logo, hero logo, and favicon
- `assets/css/styles.css` - Main styling
- `assets/js/main.js` - Mobile navigation and placeholder payment behavior
- `backend/app.py` - Optional secure Stripe Checkout Session backend example

## GitHub Pages Deployment

1. Create a GitHub repository.
2. Upload all files in this folder to the repository root.
3. In GitHub, open `Settings` -> `Pages`.
4. Under `Build and deployment`, choose `Deploy from a branch`.
5. Choose your default branch and `/root`.
6. Save.

The public website is static and requires no backend.

## Checkout Flow

This site is static, so payments must be handled by a hosted checkout provider such as Stripe Payment Links, PayPal, Square, or another payment platform.

For each plan in `shop.html`:

1. Create a checkout/payment link in your payment provider.
2. Configure checkout to collect:
   - Customer name
   - Email
   - Phone number
3. Set the successful payment redirect, success URL, or return URL to:

```text
https://your-domain.example/after-purchase.html
```

4. Replace the matching `#PAYMENT_LINK_...` placeholder in `shop.html` with the real checkout URL.

Customers should enter their information, pay through the hosted checkout, and then be redirected to `after-purchase.html` to install remote support software.

## Optional Stripe Backend

An optional secure Python backend example is included in `backend/app.py`.

Use it only on a backend host. GitHub Pages cannot run this Python file.

The backend reads the Stripe secret key from:

```bash
STRIPE_SECRET_KEY
```

The secret key is never exposed in frontend code. The backend creates a Stripe Checkout Session and returns the session URL so your frontend can redirect the customer.

See:

```text
backend/README.md
```

## Customization

- Payment links: replace each `#PAYMENT_LINK_...` placeholder in `shop.html`.
- Stripe backend: deploy `backend/` separately and connect frontend buttons to that backend if you do not want hosted payment links.
- Contact form: replace `https://formspree.io/f/YOUR_FORMSPREE_ENDPOINT` in `contact.html`.
- Branding: replace `assets/logo.png` with a new logo using the same filename.
- Custom domain: edit `CNAME` and replace the placeholder domain.
