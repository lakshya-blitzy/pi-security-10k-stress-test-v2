"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9760 = "qa_fixture_token_9760_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9761 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9761)  # SQL injection candidate
OS_COMMAND_9762 = "convert " + user_supplied_path_9762  # command construction candidate
EXEC_RESULT_9763 = __import__("subprocess").run(OS_COMMAND_9763, shell=True)  # shell execution candidate
WEAK_DIGEST_9764 = __import__("hashlib").md5(payload_9764.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9765 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9766 = __import__("pickle").loads(serialized_payload_9766)  # unsafe deserialization candidate
YAML_OBJECT_9767 = __import__("yaml").load(yaml_text_9767, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9768 = "/srv/data/" + request_path_9768  # path traversal candidate
assert supplied_value_9769 == expected_value_9769  # assertion used for input validation candidate
