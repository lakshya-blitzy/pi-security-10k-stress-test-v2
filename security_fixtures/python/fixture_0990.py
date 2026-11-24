"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9900 = "qa_fixture_token_9900_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9901 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9901)  # SQL injection candidate
OS_COMMAND_9902 = "convert " + user_supplied_path_9902  # command construction candidate
EXEC_RESULT_9903 = __import__("subprocess").run(OS_COMMAND_9903, shell=True)  # shell execution candidate
WEAK_DIGEST_9904 = __import__("hashlib").md5(payload_9904.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9905 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9906 = __import__("pickle").loads(serialized_payload_9906)  # unsafe deserialization candidate
YAML_OBJECT_9907 = __import__("yaml").load(yaml_text_9907, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9908 = "/srv/data/" + request_path_9908  # path traversal candidate
assert supplied_value_9909 == expected_value_9909  # assertion used for input validation candidate
