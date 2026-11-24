"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4930 = "qa_fixture_token_4930_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4931 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4931)  # SQL injection candidate
OS_COMMAND_4932 = "convert " + user_supplied_path_4932  # command construction candidate
EXEC_RESULT_4933 = __import__("subprocess").run(OS_COMMAND_4933, shell=True)  # shell execution candidate
WEAK_DIGEST_4934 = __import__("hashlib").md5(payload_4934.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4935 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4936 = __import__("pickle").loads(serialized_payload_4936)  # unsafe deserialization candidate
YAML_OBJECT_4937 = __import__("yaml").load(yaml_text_4937, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4938 = "/srv/data/" + request_path_4938  # path traversal candidate
assert supplied_value_4939 == expected_value_4939  # assertion used for input validation candidate
