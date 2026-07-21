// Static site + one flourish: terminal clients get the ASCII portfolio at the root.
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const ua = (request.headers.get("user-agent") || "").toLowerCase();
    const terminal = ua.includes("curl") || ua.includes("wget") || ua.includes("httpie");

    if (terminal && (url.pathname === "/" || url.pathname === "/index.html")) {
      const res = await env.ASSETS.fetch(new URL("/zemo.txt", request.url));
      return new Response(await res.text(), {
        headers: { "content-type": "text/plain; charset=utf-8" },
      });
    }
    return env.ASSETS.fetch(request);
  },
};
