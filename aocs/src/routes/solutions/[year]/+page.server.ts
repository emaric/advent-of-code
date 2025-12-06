import { redirect } from '@sveltejs/kit';

export const load = (({ params }) => {
	throw redirect(302, `/solutions/${params.year}/0`);
});
