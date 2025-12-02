import type { PageServerLoad } from './$types';
import { findRecords } from '$lib/db';
import { Record } from '$lib/models/record';

export const load = (async ({ url }) => {
	const yearParam = url.searchParams.get('year');
	const year = yearParam ? parseInt(yearParam) : new Date().getFullYear();

	const records = await findRecords(year) as unknown as Record[];

	return {
		year: year,
		records: records
	};
}) satisfies PageServerLoad;
