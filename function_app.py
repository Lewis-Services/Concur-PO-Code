import logging
import azure.functions as func
import concur_po_logic  # your existing logic module

# Create the FunctionApp object for the Python v2 programming model
app = func.FunctionApp()

@app.function_name(name="ConcurPOFileBuilder")
@app.route(
    route="ConcurPOFileBuilder", 
    methods=["GET", "POST"],
    auth_level=func.AuthLevel.FUNCTION
)
def ConcurPOFileBuilder(req: func.HttpRequest) -> func.HttpResponse:
    """
    HTTP-triggered function that runs the Concur PO file build.
    """
    logging.info("Concur PO Builder HTTP trigger function started.")

    try:
        # Call your existing main() logic
        concur_po_logic.main()

        return func.HttpResponse(
            "Concur PO file build completed successfully.",
            status_code=200,
        )
    except Exception as e:
        logging.exception("Error running Concur PO Builder.")
        return func.HttpResponse(str(e), status_code=500)
