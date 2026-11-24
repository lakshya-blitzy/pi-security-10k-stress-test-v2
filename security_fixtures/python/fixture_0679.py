"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6790 = "qa_fixture_token_6790_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6791 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6791)  # SQL injection candidate
OS_COMMAND_6792 = "convert " + user_supplied_path_6792  # command construction candidate
EXEC_RESULT_6793 = __import__("subprocess").run(OS_COMMAND_6793, shell=True)  # shell execution candidate
WEAK_DIGEST_6794 = __import__("hashlib").md5(payload_6794.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6795 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6796 = __import__("pickle").loads(serialized_payload_6796)  # unsafe deserialization candidate
YAML_OBJECT_6797 = __import__("yaml").load(yaml_text_6797, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6798 = "/srv/data/" + request_path_6798  # path traversal candidate
assert supplied_value_6799 == expected_value_6799  # assertion used for input validation candidate
