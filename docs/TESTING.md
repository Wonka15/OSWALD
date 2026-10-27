# OSWALD Mini — M1 iPad test checklist

This is an experimental Safari PWA, not a verified offline AI product.

## Publish
In repository Settings > Pages, choose Deploy from branch, main, /docs. Wait for the deployment. Check https://wonka15.github.io/OSWALD/.

## Safari / M1
1. Open the site in Safari, not the GitHub file viewer.
2. Confirm the Network status reads online.
3. Confirm whether WebGPU is available.
4. Select the smallest model first. Approve the download on Wi-Fi with ample storage.
5. Ask a simple question. Record whether the response is generated and how long it takes.
6. Enable Wikipedia research and confirm that source links open in Safari.
7. Use Share > Add to Home Screen.
8. Restart the Home Screen app, disable Wi-Fi and cellular connectivity, and test local chat again.
9. Record whether offline startup works. Shell caching alone does NOT guarantee cached WebLLM runtime and weights.

## Known limitations
- Wikipedia only, not a full embedded web browser.
- WebGPU and browser memory vary by Safari/iPadOS version.
- WebLLM runtime comes from a third-party CDN; first startup requires internet.
- Web model files may be evicted by Safari.
- No Siri/Apple Intelligence integration.
- No guarantee that 2 GB models fit or perform acceptably.
- No automatic AI model downloads; always confirm.
- Never put sensitive information into search queries.
