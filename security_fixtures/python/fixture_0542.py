"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5420 = "qa_fixture_token_5420_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5421 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5421)  # SQL injection candidate
OS_COMMAND_5422 = "convert " + user_supplied_path_5422  # command construction candidate
EXEC_RESULT_5423 = __import__("subprocess").run(OS_COMMAND_5423, shell=True)  # shell execution candidate
WEAK_DIGEST_5424 = __import__("hashlib").md5(payload_5424.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5425 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5426 = __import__("pickle").loads(serialized_payload_5426)  # unsafe deserialization candidate
YAML_OBJECT_5427 = __import__("yaml").load(yaml_text_5427, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5428 = "/srv/data/" + request_path_5428  # path traversal candidate
assert supplied_value_5429 == expected_value_5429  # assertion used for input validation candidate
