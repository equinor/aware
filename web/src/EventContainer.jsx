import React, { useState, useEffect } from 'react'
import styled from 'styled-components'
import EventContainerMobileView from './EventContainerMobileView';
const NoEventsContainer = styled.div`
  display: flex;
  height: 100%;
  align-items: center;
`

export function getBackgroundColor(severity) {
  switch (severity) {
    case 'none':
      return '#00b7bf'
    case 'ok':
      return '#00E30F'
    case 'warning':
      return '#ffb744'
    case 'critical':
      return '#ed1f28'
    default:
      return 'lightslategray'
  }
}

export const TH = styled.th`
  border: 1px solid black;
  padding: 15px;
  color: white;
  background: black;
`

const THMSG = styled.th`
  border: 1px solid black;
  padding: 15px;
  color: white;
  background: black;
  width: 50%;
`

export const THTriggered = styled.th`
  min-width: 85px;
  border: 1px solid black;
  padding: 15px;
  color: white;
  background: black;
`

const TABLE = styled.table`
  border: 0;
  border-collapse: collapse;
  margin: auto  ;
  padding: 0;
  width: 90%;
  align: center;
  table-layout: fixed;
`

const THEAD = styled.thead`
display: table-header-group;
`

const TR = styled.tr`
  display: table-row;
  padding: 1em 1em .5em;
  border: 1px solid black;
  font-size: 1em;
  background: ${props => getBackgroundColor(props.background)};
`

const TD = styled.td`
  display: table-cell;
  text-wrap: normal;
  word-wrap: break-word;
  font-size: 1em;
  padding: 5px;
  border: 1px solid black;
  text-align: left;
`
export const LogLine = styled.div`
  padding-left: 15px;
  font-size: 1em;
  font-family: monospace;
  color: white;
  &:hover {
    background-color: #494444
  }
`

const LogContainer = styled.td`
  background-color: #131212;
  max-width: 200px;
  overflow: auto;
`

function getWindowDimensions() {
  const { innerWidth: width, innerHeight: height } = window;
  return {
    width,
    height
  };
}

function useWindowDimensions() {
  const [windowDimensions, setWindowDimensions] = useState(
    getWindowDimensions()
  );

  useEffect(() => {
    function handleResize() {
      setWindowDimensions(getWindowDimensions());
    }

    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  return windowDimensions;
}

function EventRow({event}) {
  const [logsVisible, setLogsVisible] = useState(false)

  return (
      <>
        <TR
            background={event.severity}
            onClick={() => setLogsVisible(!logsVisible)}
            style={{ cursor: "pointer"}}
        >
          <TD>{event.alertname}</TD>
          <TD>{event.namespace}</TD>
          <TD>{event.source}</TD>
          <TD>{event.message}</TD>
          <TD>{event.triggered}</TD>
        </TR>
        <TR>
          {logsVisible &&
          <LogContainer colSpan={5}>
            <div style={{ maxHeight: "600px" }}>
              {event.logs.map(line => (
                  <LogLine>{line}</LogLine>
              ))}
            </div>
          </LogContainer>
          }
        </TR>
      </>
  )
}

function EventContainer({ events }) {
  const { height, width } = useWindowDimensions();

  return events.length === 0 ? (
      <NoEventsContainer>
        <h2>Everything is probably alright</h2>
      </NoEventsContainer>
  ) : ( 
      width > 1000 ?
      (<div style={{ overflow: 'auto' }}>
        <TABLE>
          <THEAD>
            <TR>
              <TH>Alertname</TH>
              <TH>Namespace/Host</TH>
              <TH>Source</TH>
              <THMSG>Message</THMSG>
              <THTriggered>Triggered</THTriggered>
            </TR>
          </THEAD>
          <tbody>
          {events.map(event => (
              <EventRow event={event}/>
          ))}
          </tbody>
        </TABLE>
      </div>)
      :
      (<div> <EventContainerMobileView events={events} /></div>)
  )
}

export default EventContainer
