import * as mongoDB from 'mongodb';

export const collections: { records?: mongoDB.Collection } = {};

export async function connectToDatabase() {
	const client: mongoDB.MongoClient = new mongoDB.MongoClient(import.meta.env.VITE_MONGODB_URI);

	await client.connect();

	const db: mongoDB.Db = client.db(import.meta.env.VITE_DB_NAME);

	const recordsCollection: mongoDB.Collection = db.collection(
		import.meta.env.VITE_RECORDS_COLLECTION_NAME
	);

	collections.records = recordsCollection;

	console.log(
		`Successfully connected to database: ${db.databaseName} and collection: ${recordsCollection.collectionName}`
	);
}
