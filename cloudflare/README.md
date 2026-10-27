# OSWALD Mini — Free online AI setup

OSWALD Mini's default mode is **Online Butler**, which does not download AI model weights onto your iPad. The GitHub Pages site alone cannot run cloud inference.

## Deploy your own Cloudflare Worker

1. Create a Cloudflare account and install Node.js on your PC.
2. In this repository's `cloudflare/` directory, run `npx wrangler login` and then `npx wrangler deploy`.
3. Ensure your account's Workers AI free allocation and chosen model are available. The example uses `@cf/meta/llama-3.1-8b-instruct`, not Gemma 4; check Cloudflare's current supported models and quotas before changing `AI_MODEL`.
4. Copy the deployed HTTPS `workers.dev` URL into OSWALD Mini's **Cloudflare Worker URL** field, then select **Save Worker URL** and **Test connection**.
5. Select **Online Butler**, ask a question, and optionally enable spoken replies.

The Cloudflare AI binding runs on the server; **do not put Cloudflare API tokens in the website**. Cloudflare free limits can change and requests may be rejected when quota is exhausted.

## Security caveats

The Worker checks the Origin header and limits message sizes, but **Origin is not authentication**. A publicly reachable Worker can be called by scripts outside the browser, potentially consuming your free allowance. For production use, add Cloudflare Turnstile, verified user authentication, and rate limiting. Do not use this example as an unrestricted public endpoint.

Prompts and replies are processed by Cloudflare's AI service. Do not send secrets. Local mode remains experimental and may fail on Safari.
