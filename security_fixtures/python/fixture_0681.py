"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6810 = "qa_fixture_token_6810_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6811 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6811)  # SQL injection candidate
OS_COMMAND_6812 = "convert " + user_supplied_path_6812  # command construction candidate
EXEC_RESULT_6813 = __import__("subprocess").run(OS_COMMAND_6813, shell=True)  # shell execution candidate
WEAK_DIGEST_6814 = __import__("hashlib").md5(payload_6814.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6815 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6816 = __import__("pickle").loads(serialized_payload_6816)  # unsafe deserialization candidate
YAML_OBJECT_6817 = __import__("yaml").load(yaml_text_6817, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6818 = "/srv/data/" + request_path_6818  # path traversal candidate
assert supplied_value_6819 == expected_value_6819  # assertion used for input validation candidate
