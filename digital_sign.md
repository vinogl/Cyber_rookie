* 签名过程

	```mermaid
	graph LR

	subgraph 签名过程
		content_s(合约内容) --Hash运算--> digest_s(信息摘要)
		digest_s(信息摘要) --私钥加密--> sign_s(签名)
	end

		content_s(合约内容) ==> s2v(合约+签名)
		sign_s(签名) ==> s2v(合约+签名)
	```

* 验证过程

	```mermaid
	graph LR

		s2v(合约+签名) ==> content_v(合约内容)
		s2v(合约+签名) ==> sign_v(签名)	

	subgraph 验证过程
		content_v(合约内容) --Hash运算--> digest_v_c(信息摘要) --> judge{是否一致}
		sign_v(签名) --公钥解密--> digest_v_s(信息摘要) --> judge{是否一致}
	end
	```