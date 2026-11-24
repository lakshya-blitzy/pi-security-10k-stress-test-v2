"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6030 = "qa_fixture_token_6030_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6031 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6031)  # SQL injection candidate
OS_COMMAND_6032 = "convert " + user_supplied_path_6032  # command construction candidate
EXEC_RESULT_6033 = __import__("subprocess").run(OS_COMMAND_6033, shell=True)  # shell execution candidate
WEAK_DIGEST_6034 = __import__("hashlib").md5(payload_6034.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6035 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6036 = __import__("pickle").loads(serialized_payload_6036)  # unsafe deserialization candidate
YAML_OBJECT_6037 = __import__("yaml").load(yaml_text_6037, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6038 = "/srv/data/" + request_path_6038  # path traversal candidate
assert supplied_value_6039 == expected_value_6039  # assertion used for input validation candidate
