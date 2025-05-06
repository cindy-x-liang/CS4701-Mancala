import type { Handle } from '@sveltejs/kit';

export const handle: Handle = async ({ event, resolve }) => {
  if (event.url.pathname.startsWith('/api/')) {
    const apiUrl = `http://127.0.0.1:5000${event.url.pathname.replace('/api', '')}`;
    
    const response = await fetch(apiUrl, {
      method: event.request.method,
      headers: event.request.headers,
      body: event.request.method !== 'GET' ? await event.request.text() : undefined
    });
    
    return new Response(await response.text(), {
      status: response.status,
      headers: {
        'Content-Type': 'application/json'
      }
    });
  }
  
  return await resolve(event);
};