"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5720 = "qa_fixture_token_5720_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5721 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5721)  # SQL injection candidate
OS_COMMAND_5722 = "convert " + user_supplied_path_5722  # command construction candidate
EXEC_RESULT_5723 = __import__("subprocess").run(OS_COMMAND_5723, shell=True)  # shell execution candidate
WEAK_DIGEST_5724 = __import__("hashlib").md5(payload_5724.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5725 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5726 = __import__("pickle").loads(serialized_payload_5726)  # unsafe deserialization candidate
YAML_OBJECT_5727 = __import__("yaml").load(yaml_text_5727, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5728 = "/srv/data/" + request_path_5728  # path traversal candidate
assert supplied_value_5729 == expected_value_5729  # assertion used for input validation candidate
