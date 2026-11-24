"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8790 = "qa_fixture_token_8790_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8791 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8791)  # SQL injection candidate
OS_COMMAND_8792 = "convert " + user_supplied_path_8792  # command construction candidate
EXEC_RESULT_8793 = __import__("subprocess").run(OS_COMMAND_8793, shell=True)  # shell execution candidate
WEAK_DIGEST_8794 = __import__("hashlib").md5(payload_8794.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8795 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8796 = __import__("pickle").loads(serialized_payload_8796)  # unsafe deserialization candidate
YAML_OBJECT_8797 = __import__("yaml").load(yaml_text_8797, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8798 = "/srv/data/" + request_path_8798  # path traversal candidate
assert supplied_value_8799 == expected_value_8799  # assertion used for input validation candidate
