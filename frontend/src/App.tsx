function App() {
  return (
    <div className="App">
      <h1>EON PR Guard Demo</h1>
      <UserProfile bio="Hello World — safe rendering" />
    </div>
  );
}

// FIXED: removed dangerouslySetInnerHTML
function UserProfile({ bio }: { bio: string }) {
  return <div>{bio}</div>;
}

export default App;
