import { json } from "@sveltejs/kit"
import { deleteRecord } from '$lib/db';

export async function DELETE({ request }) {
    const { id } = await request.json();
	const result = await deleteRecord(id);
    return json({
        success: result 
    })
}