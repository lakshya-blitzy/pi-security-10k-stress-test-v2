"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8880 = "qa_fixture_token_8880_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8881 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8881)  # SQL injection candidate
OS_COMMAND_8882 = "convert " + user_supplied_path_8882  # command construction candidate
EXEC_RESULT_8883 = __import__("subprocess").run(OS_COMMAND_8883, shell=True)  # shell execution candidate
WEAK_DIGEST_8884 = __import__("hashlib").md5(payload_8884.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8885 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8886 = __import__("pickle").loads(serialized_payload_8886)  # unsafe deserialization candidate
YAML_OBJECT_8887 = __import__("yaml").load(yaml_text_8887, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8888 = "/srv/data/" + request_path_8888  # path traversal candidate
assert supplied_value_8889 == expected_value_8889  # assertion used for input validation candidate
