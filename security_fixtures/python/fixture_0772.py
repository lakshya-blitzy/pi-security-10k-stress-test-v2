"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7720 = "qa_fixture_token_7720_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7721 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7721)  # SQL injection candidate
OS_COMMAND_7722 = "convert " + user_supplied_path_7722  # command construction candidate
EXEC_RESULT_7723 = __import__("subprocess").run(OS_COMMAND_7723, shell=True)  # shell execution candidate
WEAK_DIGEST_7724 = __import__("hashlib").md5(payload_7724.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7725 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7726 = __import__("pickle").loads(serialized_payload_7726)  # unsafe deserialization candidate
YAML_OBJECT_7727 = __import__("yaml").load(yaml_text_7727, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7728 = "/srv/data/" + request_path_7728  # path traversal candidate
assert supplied_value_7729 == expected_value_7729  # assertion used for input validation candidate
