import { json } from "@sveltejs/kit"
import { findDays } from '$lib/db';

export async function GET({ params }) {
	const yearParam = params.year;

	const year = yearParam ? parseInt(yearParam) : new Date().getFullYear();

	const days = await findDays(year) as unknown as number[]

    return json({
        days: days,
    })
}