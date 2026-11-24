"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5930 = "qa_fixture_token_5930_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5931 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5931)  # SQL injection candidate
OS_COMMAND_5932 = "convert " + user_supplied_path_5932  # command construction candidate
EXEC_RESULT_5933 = __import__("subprocess").run(OS_COMMAND_5933, shell=True)  # shell execution candidate
WEAK_DIGEST_5934 = __import__("hashlib").md5(payload_5934.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5935 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5936 = __import__("pickle").loads(serialized_payload_5936)  # unsafe deserialization candidate
YAML_OBJECT_5937 = __import__("yaml").load(yaml_text_5937, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5938 = "/srv/data/" + request_path_5938  # path traversal candidate
assert supplied_value_5939 == expected_value_5939  # assertion used for input validation candidate
