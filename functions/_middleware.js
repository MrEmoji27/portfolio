// Serves the ASCII portfolio to terminal clients hitting the root URL.
// Browsers are untouched; curl / wget / httpie get zemo.txt instead.
export async function onRequest(context) {
  const { request, next } = context;
  const url = new URL(request.url);
  const ua = (request.headers.get("user-agent") || "").toLowerCase();
  const terminal = ua.includes("curl") || ua.includes("wget") || ua.includes("httpie");

  if (terminal && (url.pathname === "/" || url.pathname === "/index.html")) {
    const res = await context.env.ASSETS.fetch(new URL("/zemo.txt", request.url));
    return new Response(await res.text(), {
      headers: { "content-type": "text/plain; charset=utf-8" },
    });
  }
  return next();
}
