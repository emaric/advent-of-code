import { MongoClient, type Collection, type Db, type SortDirection } from 'mongodb';
import { Record } from './models/record';
import * as dotenv from 'dotenv';

if (import.meta.env.DEV) {
	dotenv.config();
}

export async function connectToDatabase() {
	const client: MongoClient = new MongoClient(process.env.MONGODB_URI ?? '');
	try {
		await client.connect();

		const db: Db = client.db(import.meta.env.VITE_DB_NAME);

		const recordsCollection: Collection = db.collection(
			import.meta.env.VITE_RECORDS_COLLECTION_NAME
		);

		console.log(
			`Successfully connected to database: ${db.databaseName} and collection: ${recordsCollection.collectionName}`
		);
	} finally {
		await client.close();
	}
}

export async function findRecords(year: number) {
	const client: MongoClient = new MongoClient(process.env.MONGODB_URI ?? '');
	try {
		await client.connect();

		const db: Db = client.db(import.meta.env.VITE_DB_NAME);
		const recordsCollection: Collection = db.collection(
			import.meta.env.VITE_RECORDS_COLLECTION_NAME
		);

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
		const records = (await recordsCollection
			?.find({
				year: {
					$eq: year
				}
			})
			.sort(sort)
			.limit(100)
			.toArray()) as unknown as Record[];
		const serializable_records = records?.map((record) => ({
			...record,
			_id: record._id?.toString()
		}));

		return serializable_records;
	} finally {
		await client.close();
	}
}
