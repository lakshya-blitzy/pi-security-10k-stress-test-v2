"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6760 = "qa_fixture_token_6760_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6761 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6761)  # SQL injection candidate
OS_COMMAND_6762 = "convert " + user_supplied_path_6762  # command construction candidate
EXEC_RESULT_6763 = __import__("subprocess").run(OS_COMMAND_6763, shell=True)  # shell execution candidate
WEAK_DIGEST_6764 = __import__("hashlib").md5(payload_6764.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6765 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6766 = __import__("pickle").loads(serialized_payload_6766)  # unsafe deserialization candidate
YAML_OBJECT_6767 = __import__("yaml").load(yaml_text_6767, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6768 = "/srv/data/" + request_path_6768  # path traversal candidate
assert supplied_value_6769 == expected_value_6769  # assertion used for input validation candidate
