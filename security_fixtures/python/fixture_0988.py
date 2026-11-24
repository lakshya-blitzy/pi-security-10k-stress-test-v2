"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9880 = "qa_fixture_token_9880_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9881 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9881)  # SQL injection candidate
OS_COMMAND_9882 = "convert " + user_supplied_path_9882  # command construction candidate
EXEC_RESULT_9883 = __import__("subprocess").run(OS_COMMAND_9883, shell=True)  # shell execution candidate
WEAK_DIGEST_9884 = __import__("hashlib").md5(payload_9884.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9885 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9886 = __import__("pickle").loads(serialized_payload_9886)  # unsafe deserialization candidate
YAML_OBJECT_9887 = __import__("yaml").load(yaml_text_9887, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9888 = "/srv/data/" + request_path_9888  # path traversal candidate
assert supplied_value_9889 == expected_value_9889  # assertion used for input validation candidate
