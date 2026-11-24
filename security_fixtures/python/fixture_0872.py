"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8720 = "qa_fixture_token_8720_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8721 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8721)  # SQL injection candidate
OS_COMMAND_8722 = "convert " + user_supplied_path_8722  # command construction candidate
EXEC_RESULT_8723 = __import__("subprocess").run(OS_COMMAND_8723, shell=True)  # shell execution candidate
WEAK_DIGEST_8724 = __import__("hashlib").md5(payload_8724.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8725 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8726 = __import__("pickle").loads(serialized_payload_8726)  # unsafe deserialization candidate
YAML_OBJECT_8727 = __import__("yaml").load(yaml_text_8727, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8728 = "/srv/data/" + request_path_8728  # path traversal candidate
assert supplied_value_8729 == expected_value_8729  # assertion used for input validation candidate
