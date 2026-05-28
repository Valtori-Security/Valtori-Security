# Valtori Security Stripe Backend

This is an optional backend for creating Stripe Checkout Sessions securely.

GitHub Pages cannot run Python backend code. Deploy this `backend/` folder to a backend host such as Render, Railway, Fly.io, a VPS, or another Python hosting provider.

## Security Rules

- Store `STRIPE_SECRET_KEY` only in backend environment variables.
- Never put `STRIPE_SECRET_KEY` in `index.html`, `shop.html`, `assets/js/main.js`, or any frontend file.
- The frontend should call this backend endpoint and redirect to the returned `url`.

## Local Setup

```bash
cd backend
python3.14 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export STRIPE_SECRET_KEY="sk_test_replace_this"
export YOUR_DOMAIN="http://127.0.0.1:4173"
python app.py
```

The backend endpoint will be:

```text
POST http://127.0.0.1:4242/create-checkout-session
```

The response is JSON:

```json
{
  "url": "https://checkout.stripe.com/..."
}
```

## Frontend Redirect Example

```js
const response = await fetch("https://your-backend.example/create-checkout-session", {
  method: "POST"
});

const data = await response.json();
window.location.href = data.url;
```

## Checkout Flow

1. Frontend calls the backend endpoint.
2. Backend creates the Stripe Checkout Session using `STRIPE_SECRET_KEY`.
3. Backend returns `session.url`.
4. Frontend redirects customer to `session.url`.
5. Stripe collects customer/payment info.
6. On successful payment, Stripe redirects to:

```text
YOUR_DOMAIN/after-purchase.html?session_id={CHECKOUT_SESSION_ID}
```
