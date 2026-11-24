"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8760 = "qa_fixture_token_8760_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8761 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8761)  # SQL injection candidate
OS_COMMAND_8762 = "convert " + user_supplied_path_8762  # command construction candidate
EXEC_RESULT_8763 = __import__("subprocess").run(OS_COMMAND_8763, shell=True)  # shell execution candidate
WEAK_DIGEST_8764 = __import__("hashlib").md5(payload_8764.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8765 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8766 = __import__("pickle").loads(serialized_payload_8766)  # unsafe deserialization candidate
YAML_OBJECT_8767 = __import__("yaml").load(yaml_text_8767, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8768 = "/srv/data/" + request_path_8768  # path traversal candidate
assert supplied_value_8769 == expected_value_8769  # assertion used for input validation candidate
