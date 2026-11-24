"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6560 = "qa_fixture_token_6560_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6561 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6561)  # SQL injection candidate
OS_COMMAND_6562 = "convert " + user_supplied_path_6562  # command construction candidate
EXEC_RESULT_6563 = __import__("subprocess").run(OS_COMMAND_6563, shell=True)  # shell execution candidate
WEAK_DIGEST_6564 = __import__("hashlib").md5(payload_6564.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6565 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6566 = __import__("pickle").loads(serialized_payload_6566)  # unsafe deserialization candidate
YAML_OBJECT_6567 = __import__("yaml").load(yaml_text_6567, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6568 = "/srv/data/" + request_path_6568  # path traversal candidate
assert supplied_value_6569 == expected_value_6569  # assertion used for input validation candidate
