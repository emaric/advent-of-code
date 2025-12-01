import type { PageServerLoad } from './$types';
import {connectToDatabase, collections } from '$lib/db';
import type { Record } from './record';

export const load = (async () => {
	if (collections.records == undefined) {
		await connectToDatabase()
	}

	const records = (await collections.records?.find({}).limit(100).toArray()) as unknown as Record[];
	const serializable_records = records?.map((record) => ({
		...record,
		_id: record._id?.toString()
	}));
	return {
		records: serializable_records
	};
}) satisfies PageServerLoad;
