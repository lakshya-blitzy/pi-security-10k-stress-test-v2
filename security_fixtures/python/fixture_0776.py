"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7760 = "qa_fixture_token_7760_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7761 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7761)  # SQL injection candidate
OS_COMMAND_7762 = "convert " + user_supplied_path_7762  # command construction candidate
EXEC_RESULT_7763 = __import__("subprocess").run(OS_COMMAND_7763, shell=True)  # shell execution candidate
WEAK_DIGEST_7764 = __import__("hashlib").md5(payload_7764.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7765 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7766 = __import__("pickle").loads(serialized_payload_7766)  # unsafe deserialization candidate
YAML_OBJECT_7767 = __import__("yaml").load(yaml_text_7767, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7768 = "/srv/data/" + request_path_7768  # path traversal candidate
assert supplied_value_7769 == expected_value_7769  # assertion used for input validation candidate
