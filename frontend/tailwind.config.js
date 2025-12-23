/** @type {import('tailwindcss').Config} */
export default {
	content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
	theme: {
		extend: {
			pageDimensions: {
				a4: {
					width: "210mm",
					height: "297mm",
					margin: "0 auto",
					padding: "20mm",
				},
			},
		},
	},
	plugins: [],
};
