import React, { useState } from 'react'
import styled from 'styled-components'

const NoEventsContainer = styled.div`
  display: flex;
  height: 100%;
  align-items: center;
`

function getBackgroundColor(severity) {
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
      return 'white'
  }
}

const TH = styled.th`
  border: 1px solid black;
  padding: 15px;
  color: white;
  background: black;
`

const THTriggered = styled.th`
  min-width: 85px;
  border: 1px solid black;
  padding: 15px;
  color: white;
  background: black;
`

const TABLE = styled.table`
  width: 90%;
  margin: auto;
  border-collapse: collapse;
  border-spacing: 0;
`

const TR = styled.tr`
  border: 1px solid black;
  font-size: 1em;
  background: ${props => getBackgroundColor(props.background)};
`

const TD = styled.td`
  font-size: 1em;
  padding: 5px;
  border: 1px solid black;
  text-align: left;
`
const LogLine = styled.div`
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
  return events.length === 0 ? (
      <NoEventsContainer>
        <h2>Everything is probably alright</h2>
      </NoEventsContainer>
  ) : (
      <div style={{ overflow: 'auto' }}>
        <TABLE>
          <tbody>
          <TR>
            <TH>Alertname</TH>
            <TH>Namespace/Host</TH>
            <TH>Source</TH>
            <TH>Message</TH>
            <THTriggered>Triggered</THTriggered>
          </TR>
          {events.map(event => (
              <EventRow event={event}/>
          ))}
          </tbody>
        </TABLE>
      </div>
  )
}

export default EventContainer
