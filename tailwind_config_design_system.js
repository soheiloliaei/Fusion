// tailwind.config.js - 100% Design System Match
module.exports = {
    content: [
        './pages/**/*.{js,ts,jsx,tsx}',
        './components/**/*.{js,ts,jsx,tsx}',
        './app/**/*.{js,ts,jsx,tsx}',
    ],
    theme: {
        extend: {
            // --- Colors (Monochromatic Design System) ---
            colors: {
                // Backgrounds
                'background': '#FAFAFA',        // Main page background (neutral-50)
                'background-card': '#FFFFFF',    // Card backgrounds, buttons
                'background-light': '#FAFAFA',   // Alternative background

                // Text Colors
                'foreground': '#0A0A0A',        // Main text, headings (neutral-950)
                'muted-foreground': '#737373',  // Secondary text, descriptions (neutral-500)
                'description-text': 'rgba(0,0,0,0.7)', // Specific description text
                'placeholder': 'rgba(0,0,0,0.3)', // Input placeholder text

                // Borders & Dividers
                'border': '#E5E5E5',            // Subtle borders, dividers
                'border-light': '#E5E5E5',      // Alternative border

                // Interactive States
                'primary': '#0A0A0A',           // Primary buttons, active states
                'primary-foreground': '#FFFFFF', // Text on primary buttons
                'secondary': '#F5F5F5',         // Secondary buttons
                'secondary-foreground': '#0A0A0A', // Text on secondary buttons

                // Status & Priority Colors (Monochromatic)
                'success': '#0A0A0A',           // Success states (black)
                'warning': '#737373',           // Warning states (gray)
                'destructive': '#0A0A0A',       // Error states (black)
                'info': '#737373',              // Info states (gray)
            },

            // --- Typography ---
            fontFamily: {
                'sans': ['Inter', 'ui-sans-serif', 'system-ui', 'sans-serif'],
                'body': ['Inter', 'ui-sans-serif', 'system-ui', 'sans-serif'],
                'heading': ['Inter', 'ui-sans-serif', 'system-ui', 'sans-serif'],
            },

            fontSize: {
                'xs': '11px',      // Status text, small labels
                'sm': '12px',      // Small text, descriptions
                'base': '14px',    // Regular text, customer info
                'md': '16px',      // Input placeholder, medium text
                'lg': '18px',      // Card titles, section headers
                'xl': '30px',      // Large metrics, case numbers
                '2xl': '30px',     // Main headings (same as xl)
            },

            lineHeight: {
                'tight': '12px',    // xs
                'snug': '14px',     // sm
                'normal': '20px',   // base
                'relaxed': '36px',  // xl
                'loose': '37.5px',  // 2xl
            },

            letterSpacing: {
                'tight': '-0.75px', // For main headings
            },

            // --- Border Radii ---
            borderRadius: {
                'default': '14px',    // General components, cards, buttons, inputs
                'badge': '200px',     // Status badges, navigation buttons
                'chat-input': '32px', // Chat input field
                'status': '200px',    // Status indicators
                'priority': '160px',  // Priority indicators
            },

            // --- Box Shadows ---
            boxShadow: {
                // Subtle shadow for cards and buttons
                'card': '0px 1px 3px 0px rgba(0,0,0,0.1), 0px 1px 2px -1px rgba(0,0,0,0.1)',

                // More pronounced shadow for navigation elements
                'nav': '0px 12px 32px 0px rgba(0,0,0,0.04), 0px 8px 16px 0px rgba(0,0,0,0.02), 0px 2px 4px 0px rgba(0,0,0,0.04), 0px 0px 1px 0px rgba(0,0,0,0.2)',

                // Hover state for cards (slightly lifted)
                'card-hover': '0 10px 25px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)',

                // Tile shadow for case tiles
                'tile': '0px 1px 3px 0px rgba(0,0,0,0.1), 0px 1px 2px -1px rgba(0,0,0,0.1)',

                // Chat shadow for conversation elements
                'chat': '0px 12px 32px 0px rgba(0,0,0,0.04), 0px 8px 16px 0px rgba(0,0,0,0.02), 0px 2px 4px 0px rgba(0,0,0,0.04), 0px 0px 1px 0px rgba(0,0,0,0.2)',
            },

            // --- Spacing (Based on Design System) ---
            spacing: {
                'px-4': '16px',      // Standard padding
                'py-2': '8px',       // Standard padding
                'gap-1.5': '6px',    // Small gaps
                'gap-3': '12px',     // Medium gaps
                'gap-4': '16px',     // Larger gaps
                'p-card': '25px',    // Card inner padding
                'mt-header': '128px', // Top margin for main content
                'mb-footer': '19px', // Bottom margin for footer
                'h-card': '288px',   // Fixed height for cards
                'w-card': '33.33%',  // Approx width for 3-column grid
                '25': '25px',        // Custom spacing
                '76': '76px',        // Custom spacing
                '11.2': '11.2px',    // Custom spacing
                '6.4': '6.4px',      // Custom spacing
                '128': '128px',      // Custom spacing
                '19': '19px',        // Custom spacing
            },

            // --- Animations ---
            animation: {
                'fade-in': 'fadeIn 0.3s ease-out',
                'slide-up': 'slideUp 0.3s ease-out',
                'scale-in': 'scaleIn 0.2s ease-out',
                'pulse-slow': 'pulse 3s infinite',
                'typing': 'typing 2s steps(40) infinite',
            },

            keyframes: {
                fadeIn: {
                    '0%': { opacity: '0' },
                    '100%': { opacity: '1' },
                },
                slideUp: {
                    '0%': { opacity: '0', transform: 'translateY(10px)' },
                    '100%': { opacity: '1', transform: 'translateY(0)' },
                },
                scaleIn: {
                    '0%': { opacity: '0', transform: 'scale(0.95)' },
                    '100%': { opacity: '1', transform: 'scale(1)' },
                },
                typing: {
                    '0%': { width: '0' },
                    '100%': { width: '100%' },
                },
            },
        },
    },
    plugins: [],
}; 