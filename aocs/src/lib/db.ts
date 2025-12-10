import { env } from '$env/dynamic/private'
import { MongoClient, ObjectId, type Collection, type Db, type DeleteResult, type SortDirection } from 'mongodb';
import { Record } from './models/record';
import * as dotenv from 'dotenv';

if (import.meta.env.DEV) {
	dotenv.config();
}

export const collections: {records?: Collection} = {}

export async function connectToDatabase() {
	const client = new MongoClient(env.MONGODB_URI ?? '')
	await client.connect();

	const db: Db = client.db(env.VITE_DB_NAME ?? 'aoc');

	const recordsCollection: Collection = db.collection(
		env.VITE_RECORDS_COLLECTION_NAME ?? 'records'
	);

	collections.records = recordsCollection

	console.log(
		`Successfully connected to database: ${db.databaseName} and collection: ${recordsCollection.collectionName}`
	);
}

export async function findRecords(year: number, day?: number) {
	collections.records ?? await connectToDatabase()
	const sort: {
		year: SortDirection;
		day: SortDirection;
		part: SortDirection;
		result_time: SortDirection;
	} = {
		year: 'desc',
		day: 'desc',
		part: 'desc',
		result_time: 'asc'
	};
	const query: any = { year: { $eq: year } };

	if (day !== undefined) {
		query.day = { $eq: day };
	}

	const records = (await collections.records?.find(query).sort(sort).limit(100).toArray()) as unknown as Record[]
	const serializable_records = records?.map((record) => ({
		...record,
		_id: record._id?.toString()
	}));

	return serializable_records;
}


export async function findDays(year: number) {
	collections.records ?? await connectToDatabase()
	const days = (await collections.records?.distinct('day', {year: {$eq: year}})) as unknown as number[]
	return days
}


export async function deleteRecord(id: string) {
	collections.records ?? await connectToDatabase()
	const deleteResult: DeleteResult | undefined = await collections.records?.deleteOne({_id: new ObjectId(id)})
	const deletedCount = deleteResult?.deletedCount || 0
	return deletedCount > 0
}


export async function findYears() {
	collections.records ?? await connectToDatabase();
	const sort: {
		year: SortDirection;
	} = {
		year: 'desc',
	};
	const years = (await collections.records?.distinct('year')) as unknown as number[]
	return years.reverse()
}