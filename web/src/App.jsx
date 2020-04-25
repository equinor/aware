import React from 'react';
import styled from 'styled-components';
import EventContainer from './EventContainer';
import axios from 'axios';

function getMostSevereAlert(events) {
  let mostSever = 'ok';
  if (events.some(event => event.severity === 'none')) {
    mostSever = 'none';
  }
  if (events.some(event => event.severity === 'warning')) {
    mostSever = 'warning';
  }
  if (events.some(event => event.severity === 'critical')) {
    mostSever = 'critical';
  }
  return mostSever;
}

function getBackgroundColor(events) {
  let background;
  switch (getMostSevereAlert(events)) {
    case 'none':
      background = '#747474';
      break;
    case 'ok':
      background = '#86C232';
      break;
    case 'warning':
      background = '#FF652F';
      break;
    case 'critical':
      background = '#FC4445';
      break;
    default:
      background = 'white';
  }
  return background;
}

const Header = styled.h1`
  margin: 0px;
  padding: 20px;
`;

const AppContainer = styled.div`
  background: ${props => props.backgroundColor};
  margin: 0px;
  width: 100%;
  height: 100%;
  position: fixed;
  display: flex;
  flex-direction: column;
  align-items: center;
`;

const P = styled.p`
  margin: 0px;
`;

function CouldNotFetch({ lastSuccessfulFetch }) {
  let lastFetch;
  if (lastSuccessfulFetch) {
    const temp_string = lastSuccessfulFetch.toString();
    lastFetch = temp_string
      .split(' ')
      .splice(0, 5)
      .join(' ');
  } else {
    lastFetch = 'none';
  }
  return (
    <>
      <P>Could not fetch data</P>
      <P>Last updated; {lastFetch}</P>
    </>
  );
}

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      events: []
    };
  }

  refetchData() {
    axios
      .get(`/api/events`)
      .then(response => {
        this.setState({
          isLoaded: true,
          events: response.data,
          backgroundColor: getBackgroundColor(response.data),
          lastSuccessfulFetch: new Date(),
          error: null
        });
      })
      .catch(error => {
        this.setState({
          isLoaded: true,
          error
        });
      });
  }

  componentDidMount() {
    document.title = "Aware monitoring"
    this.refetchData();
    this.interval = setInterval(() => this.refetchData(), 30000);
  }

  componentWillUnmount() {
    clearInterval(this.interval);
  }

  render() {
    const {
      error,
      isLoaded,
      events,
      backgroundColor,
      lastSuccessfulFetch
    } = this.state;
    if (!isLoaded) {
      return <div>Loading...</div>;
    } else {
      return (
        <AppContainer backgroundColor={backgroundColor}>
          <Header>{window.location.host}</Header>
          {error && <CouldNotFetch lastSuccessfulFetch={lastSuccessfulFetch} />}
          <EventContainer events={events} />
        </AppContainer>
      );
    }
  }
}

export default App;
