import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import EventContainer from './EventContainer';
import axios from 'axios';

function getMostSevereAlert(events) {
  if (events.some((event) => event.severity === 'critical')) {
    return 'critical';
  }
  if (events.some((event) => event.severity === 'warning')) {
    return 'warning';
  }
  if (events.some((event) => event.severity === 'none')) {
    return 'none';
  }
  return 'ok';
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
  background: ${(props) => props.backgroundColor};
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
    lastFetch = temp_string.split(' ').splice(0, 5).join(' ');
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

export default () => {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [events, setEvents] = useState([]);
  const [backgroundColor, setBackgroundColor] = useState('white');
  const [lastSuccessfulFetch, setLastSuccessfulFetch] = useState(null);
  const [interval, setInterval] = useState(null);

  function refetchData() {
    axios
      .get(`/api/events`)
      .then((response) => {
        setLoading(false);
        setEvents(response.data);
        setBackgroundColor(getBackgroundColor(response.data));
        setLastSuccessfulFetch(new Date());
      })
      .catch((error) => {
        setLoading(false);
        setError(error);
      });
  }

  useEffect(() => {
    document.title = 'Aware monitoring';
    refetchData();
    setInterval(setInterval(() => refetchData(), 30000));
    return () => clearInterval(interval);
  },[])

  if (loading) {
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
};
