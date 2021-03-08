import React, { useState } from 'react'
import styled from 'styled-components'
import "./style.css"
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


function EventRow({event}) {
  const [logsVisible, setLogsVisible] = useState(false)
  const BG = getBackgroundColor(event.severity)

  return (
      <>
        <tr
            onClick={() => setLogsVisible(!logsVisible)}
            style={{ cursor: "pointer", background: BG}}
        >
        <td data-label="Alertname">{event.alertname}</td>
        <td data-label="Namespace">{event.namespace}</td>
        <td data-label="Source">{event.source}</td>
        <td data-label="Message">{event.message}</td>
        <td data-label="Triggered">{event.triggered}</td>
        </tr>
        {logsVisible ? <tr style={{background: BG, borderTop: 'none'}}>
          {logsVisible &&
          <td colSpan={5}>
            <div className="logRow">
              {event.logs.map(line => (
                  <div>{line}</div>
              ))}
            </div>
          </td>
          }
        </tr> : <div></div>}

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
        <table>
          <thead>
            <tr id="eventContainer">
              <th>Alertname</th>
              <th>Namespace/Host</th>
              <th>Source</th>
              <th className="message">Message</th>
              <th >Triggered</th>
            </tr>
          </thead>
          <tbody>
          {events.map(event => (
              <EventRow event={event}/>
          ))}
          </tbody>
        </table>
      </div>


  )
}

export default EventContainer
