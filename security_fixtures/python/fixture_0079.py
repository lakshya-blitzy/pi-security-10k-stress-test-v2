"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_790 = "qa_fixture_token_790_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_791 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_791)  # SQL injection candidate
OS_COMMAND_792 = "convert " + user_supplied_path_792  # command construction candidate
EXEC_RESULT_793 = __import__("subprocess").run(OS_COMMAND_793, shell=True)  # shell execution candidate
WEAK_DIGEST_794 = __import__("hashlib").md5(payload_794.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_795 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_796 = __import__("pickle").loads(serialized_payload_796)  # unsafe deserialization candidate
YAML_OBJECT_797 = __import__("yaml").load(yaml_text_797, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_798 = "/srv/data/" + request_path_798  # path traversal candidate
assert supplied_value_799 == expected_value_799  # assertion used for input validation candidate
