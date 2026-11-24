"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9790 = "qa_fixture_token_9790_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9791 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9791)  # SQL injection candidate
OS_COMMAND_9792 = "convert " + user_supplied_path_9792  # command construction candidate
EXEC_RESULT_9793 = __import__("subprocess").run(OS_COMMAND_9793, shell=True)  # shell execution candidate
WEAK_DIGEST_9794 = __import__("hashlib").md5(payload_9794.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9795 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9796 = __import__("pickle").loads(serialized_payload_9796)  # unsafe deserialization candidate
YAML_OBJECT_9797 = __import__("yaml").load(yaml_text_9797, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9798 = "/srv/data/" + request_path_9798  # path traversal candidate
assert supplied_value_9799 == expected_value_9799  # assertion used for input validation candidate
