"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7930 = "qa_fixture_token_7930_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7931 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7931)  # SQL injection candidate
OS_COMMAND_7932 = "convert " + user_supplied_path_7932  # command construction candidate
EXEC_RESULT_7933 = __import__("subprocess").run(OS_COMMAND_7933, shell=True)  # shell execution candidate
WEAK_DIGEST_7934 = __import__("hashlib").md5(payload_7934.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7935 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7936 = __import__("pickle").loads(serialized_payload_7936)  # unsafe deserialization candidate
YAML_OBJECT_7937 = __import__("yaml").load(yaml_text_7937, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7938 = "/srv/data/" + request_path_7938  # path traversal candidate
assert supplied_value_7939 == expected_value_7939  # assertion used for input validation candidate
