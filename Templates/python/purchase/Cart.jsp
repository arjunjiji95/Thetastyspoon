<%-- 
    Document   : Cart
    Created on : 6 Feb, 2018, 10:06:39 AM
    Author     : AkHiLeSh
--%>

<%@page import="java.sql.ResultSet"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<jsp:useBean id="obj" class="db.ConnectionClass"></jsp:useBean>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JustClick</title>
        
        <script>
            function find_tot(val,price,cnt)
            {
                var tot=parseInt(val)*parseInt(price);
           
                document.getElementById("tot_"+cnt).innerHTML=tot;
            }
            
            </script>
            
 
    
            <script src="jquery.js" type="text/javascript"></script>
            <script>
            function update(cnt,price,ids)
            {
            
        
           var  qunty=document.getElementById("txt_"+cnt).value;
           
         if(parseInt(qunty)<1)
         {
            alert("Please select atleast 1 quantity of the item"); 
         }else
         {
             $.ajax({

                           url: "ajax_update.jsp",
                            data:{id:ids,pr:price,q:qunty},
                            
                             success: function(result)
                            {
                                $("#res").html(result);
                                
                            }   
                          
                        });
                        
                 window.location="../purchase/PaymentMethod.jsp";      
            }
        }
                   
        </script>
        
        
    </head>
    <body>
        <form >
       <%
          
           
        if(request.getParameter("rmv")!=null)
        {
            String del="delete from tbl_cart where Cart_id='"+request.getParameter("rmv")+"'";
            obj.executeCommand(del);
        }
        
            

        %>    
        
        <table width="90%" align="center" cellpadding="8" bgcolor="#FAFAFA" style="box-shadow: 0 8px 16px 0 rgba(0,0,0,0.15), 0 6px 20px 0 rgba(0,0,0,0.19);border-radius: 12px;">
            <tr bgcolor="#FFB74D" style="box-shadow: 0 8px 16px 0 rgba(0,0,0,0.15), 0 6px 20px 0 rgba(0,0,0,0.19);border-radius: 12px;">
                <td width="40%" align="center" colspan="2">
                    <b>  <h3>Item</h3></b>
                </td >
                <td width="20%" align="center">
                     <b>  <h3>Price</h3></b>
                </td>
                <td width="20%" align="center" >
                     <b>  <h3>Quantity</h3></b>
                </td>
                <td width="20%" align="center" colspan="3">
                     <b>  <h3>Total</h3></b>
                </td>
            </tr>
            <%
             
            String sel="select * from tbl_cart c inner join tbl_item i on c.Item_id=i.Item_id inner join tbl_user u on c.User_id=u.user_id where u.user_id='"+session.getAttribute("userid")+"' and c.Cart_status=0";
            int cnt=0;
            ResultSet rs=obj.selectCommand(sel);
            while(rs.next())
            {
                 cnt++;
                %>
                <tr>
                    <td>
                        <img src="../Company/ProductImage/<%=rs.getString("Item_image")%>" width="80" height="80" style="box-shadow: 0 8px 16px 0 rgba(0,0,0,0.15), 0 6px 20px 0 rgba(0,0,0,0.19)">
                        
                    </td>
                    <td>
                         <%=rs.getString("Item_name")%>
                    </td>
                    <td align="center">
                        
                      <h4 color="#FFE0B2"> &#8377; <%=rs.getString("Item_price")%></h4>  
                    </td>
                    <td align="center">
                            
                        <input id="txt_<%=cnt%>" name="txtqnty" onkeyup="find_tot(this.value,<%=rs.getString("Item_price")%>,<%=cnt%>)" value="0" max="2" min="1" size="1">
                   </td>
                   <td align="center" id="tot_<%=cnt%>" name="utotal">
                       
                        
                   </td>
                   <td>
                       <a href="Cart.jsp?rmv=<%=rs.getString("Cart_id")%>" style="text-decoration:none"><img src="../purchase/img/remove.jpg" width="30" height="30"></a>
                   </td>
                   <td>
                       <a onclick="update(<%=cnt%>,<%=rs.getString("Item_price")%>,<%=rs.getString("cart_id")%>)"><img src="../purchase/img/buy.png" width="50" height="50" ></a> 
                   </td>
                </tr>  
                
                
           <%
               
            }
             
            %>
           
        </table>
            <div id="res"></div>
            </form>
    </body>
</html>
