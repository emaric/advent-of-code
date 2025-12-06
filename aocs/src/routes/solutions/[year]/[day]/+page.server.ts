import { Record } from '$lib/models/record';
import type { PageServerLoad } from './$types';

interface SolutionsData {
	year: number,
	day: number 
	days: number[],
	records?: Record[],
};

export const load = (({ params }) => {
	const data: SolutionsData = {
		year: Number(params.year),
		day: Number(params.day),
		days: [0],
	}
	return data
}) satisfies PageServerLoad;

