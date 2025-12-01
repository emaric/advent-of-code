export class Record {
	constructor(
		public year: number,
		public day: number,
		public part: number,
		public result_time: number,
		public timestamp: Date,
		public person: string,
		public code: string,
		public _id?: string
	) {}
}
