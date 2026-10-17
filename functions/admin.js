/** Gõ vessca.com/admin (không có dấu / cuối) thì chuyển về /admin/ */
export function onRequest() {
  return new Response(null, { status: 302, headers: { Location: '/admin/' } });
}
