<!DOCTYPE html>
<html>
<head>
    <title>Azure Table Storage Example</title>
</head>
<body bgcolor="#00abec" >
    <div>
        <table width="450" frame="below">
            <tr>  
            <th align="left">Azure Storage Tables:</th>  
            </tr>
            <%@ page import="java.util.*" %>
            <%@ page import="com.microsoft.azure.storage.*" %>
            <%@ page import="com.microsoft.azure.storage.table.*" %>
            <%@ page import="com.microsoft.azure.storage.table.TableQuery.*" %>
            <%
                String connectionString = "DefaultEndpointsProtocol=http;" +
                "AccountName=ACCOUNT-NAME;" +
                "AccountKey=ACCOUNT-KEY;";
                
                CloudStorageAccount stAc = CloudStorageAccount.parse(connectionString);
                CloudTableClient tableClient = stAc.createCloudTableClient();

                for(String table : tableClient.listTables())
                {
                    out.print("<tr><td>" + table + "</td></tr>");
                }
                
            %>
        </table>
    </div>
</body>

</html>