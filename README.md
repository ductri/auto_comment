# Train seq2seq for fun, and playaround with Tensor2Tensor
## Dataset: 
Data: Row [Row]*
Row: (Post|Share Comment) | (Comment Reply-Comment)

### Some samples:

Post: `__share__ Các mom có ai cho bé uống sữa này cho mình xin rewei nha. Con mình đang uống friso mình định cho bé đổi qua similac mà không biết của nó có ngọt lắm ko, có béo nhiều ko. Cảm ơn các mom nhé __post__`

-> Comment: `bé mình chịu uống.bé nào hợp lên kí nhiề`

Comment: `__comment__ Trời ơi bú 7 ngày 1 lần mỗi lần 120ml là ok rui mà mom còn kêu có 120ml. Cân nặng như kia cũng quá ok rui mà`

-> Reply-Comment: `May Coco nhà minh 5m20d bdau ăn nhưng minh cho ăn xíu thui, duoi 1t chủ yếu là sữa m`

Model will try to generate a comment/reply comment corresponding posts

### Some infering samples:

Comment: `__comment__ Em đây, cũng từng đau đầu vì vấn đề cân nặng của con, nhưng may quá tìm hiểu xong đổi qua Pediasure, thấy con có sự thay đổi về cân nặng rõ luôn. Không bị chê còi nữa 🙂`

-> Infering: `Similac neosure là dòng này thì mom ơi, bé nhà mình uống similac similac thì uống similac thì uống similac thì uống similac thì uống similac thì uống similac thì uống similac thì uống similac thì k bị táo bón, bé uống similac thì uống similac thì tăng cân đều, bé uống similac thì tăng cân đều, bé uống similac thì tăng cân đều, bé uống similac thì tăng cân đều, bé uống similac thì tăng cân đều, bé uống similac thì tăng cân đều, tăng cân đều`

Post: `__share__ Các mom có ai cho bé uống sữa này cho mình xin rewei nha. Con mình đang uống friso mình định cho bé đổi qua similac mà không biết của nó có ngọt lắm ko, có béo nhiều ko. Cảm ơn các mom nhé __post__`

-> Infering: `Bé nhà mình uống friso từ lúc sinh non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non non`


## Conclude
Training data includes ~300k, mostly about milk domain. There are so much variance in post/share-response, which makes model's prediction not good. However, it still learned to response with correct brand name :v
