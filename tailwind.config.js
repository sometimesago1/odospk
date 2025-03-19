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
      },
      borderRadius: {
        '3xl': '20px',
        '3.5xl': '24px',
        '4xl': '32px',
        '5xl': '36px',
        '6xl': '48px',
        '7xl': '56px',
        '8xl': '64px',
        '9xl': '72px',
      },
      fontSize: {
        '2.5xl': '28px',
        '4xxl': '42px'
      }
    },
  },
  plugins: [],
}

