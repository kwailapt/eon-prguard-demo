function App() {
  return (
    <div className="App">
      <h1>EON PR Guard Demo</h1>
      <UserProfile bio="<script>alert('xss')</script>Hello World" />
    </div>
  );
}

// VULNERABILITY: XSS via dangerouslySetInnerHTML (will be fixed in PR #8)
function UserProfile({ bio }: { bio: string }) {
  return <div dangerouslySetInnerHTML={{ __html: bio }} />;
}

export default App;
