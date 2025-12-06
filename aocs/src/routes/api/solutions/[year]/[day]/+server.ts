import { json } from "@sveltejs/kit"
import { findRecords } from '$lib/db';
import { Record } from '$lib/models/record';

export async function GET({ params }) {
	const yearParam = params.year;
	const dayParam = params.day;

	const year = yearParam ? parseInt(yearParam) : new Date().getFullYear();
	const day = dayParam ? parseInt(dayParam) : 1;

	const records = await findRecords(year, day) as unknown as Record[];
    return json({
        records: records
    })
}