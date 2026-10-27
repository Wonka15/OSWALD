# OSWALD 2.1 Model Manager

A local-only Ollama model manager for OSWALD.

- Lists locally installed models.
- Benchmarks an installed model with bounded output and a 180-second timeout.
- Validates model tags before use.
- Requires exact typed approval `DOWNLOAD <tag>` before downloading any model.
- Never enables automatic model updates.
- Prevents network redirects and use of HTTP proxies for model management.
- Supports selection and rollback when integrated into the desktop dashboard.

**Status:** The standalone backend and tests are in this repository. The full desktop integration is included in the separately packaged OSWALD 2.1 Windows source ZIP, and still needs to be imported into this GitHub repository. Do not treat the repository's current contents as a complete Windows installer.

**Hardware:** AMD Vega 56 inference speed, VRAM fit, and thermal stability remain untested on the target PC.

**Security:** Model weights are not included. Review the source and license of every new model. Never run generated commands automatically.
