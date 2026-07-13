                        Source Systems

        CRM CSV      Claims JSON      Mobile API

             │             │              │

             ▼             ▼              ▼

          CSVReader   JSONReader     APIReader

                \        |          /

                 \       |         /

                  \      |        /

                 SourceConnector (Interface)

                         │

                         ▼

               CustomerRecord Mapper

                         │

                         ▼

            list[CustomerRecord]
