"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_760 = "qa_fixture_token_760_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_761 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_761)  # SQL injection candidate
OS_COMMAND_762 = "convert " + user_supplied_path_762  # command construction candidate
EXEC_RESULT_763 = __import__("subprocess").run(OS_COMMAND_763, shell=True)  # shell execution candidate
WEAK_DIGEST_764 = __import__("hashlib").md5(payload_764.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_765 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_766 = __import__("pickle").loads(serialized_payload_766)  # unsafe deserialization candidate
YAML_OBJECT_767 = __import__("yaml").load(yaml_text_767, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_768 = "/srv/data/" + request_path_768  # path traversal candidate
assert supplied_value_769 == expected_value_769  # assertion used for input validation candidate
