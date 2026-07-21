import "./globals.css";

export const metadata = {
  title: "Nexa AI",
  description: "Assistant intelligent d'adaptation aux nouveaux métiers et technologies"
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="fr">
      <body>{children}</body>
    </html>
  );
}