import type { PageServerLoad } from './$types';
import type { SortDirection } from 'mongodb';
import { connectToDatabase, collections } from '$lib/db';
import type { Record } from './record';

export const load = (async ({ url }) => {
	const year = url.searchParams.get('year') ?? new Date().getFullYear();

	if (collections.records == undefined) {
		await connectToDatabase();
	}

	const sort: {
		year: SortDirection;
		day: SortDirection;
		part: SortDirection;
		result_time: SortDirection;
	} = {
		year: 'desc',
		day: 'desc',
		part: 'asc',
		result_time: 'asc'
	};
	const records = (await collections.records
		?.find({
			'year': {
				$exists: year
			}
		})
		.sort(sort)
		.limit(100)
		.toArray()) as unknown as Record[];
	const serializable_records = records?.map((record) => ({
		...record,
		_id: record._id?.toString()
	}));

	return {
		year: year,
		records: serializable_records
	};
}) satisfies PageServerLoad;
