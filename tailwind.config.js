module.exports = {
  content: [
    './landing/templates/landing/**/*.html',
    './crm/templates/crm/**/*.html',
  ],
  theme: {
    extend: {
      fontFamily: {
        involve: ['Involve', 'sans-serif'],
        uncage: ['Uncage', 'sans-serif'],
      },
      colors: {
        'neutral-150': '#F1F1F1',
        'neutral-750': '#2D2D32',
        'neutral-850': '#222225'
      }
    },
  },
  plugins: [],
}

