import { json } from "@sveltejs/kit"
import { findYears } from '$lib/db';

export async function GET() {
	const years = await findYears() as unknown as number[]

    return json({
        years
    })
}