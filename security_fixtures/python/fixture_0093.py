"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_930 = "qa_fixture_token_930_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_931 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_931)  # SQL injection candidate
OS_COMMAND_932 = "convert " + user_supplied_path_932  # command construction candidate
EXEC_RESULT_933 = __import__("subprocess").run(OS_COMMAND_933, shell=True)  # shell execution candidate
WEAK_DIGEST_934 = __import__("hashlib").md5(payload_934.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_935 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_936 = __import__("pickle").loads(serialized_payload_936)  # unsafe deserialization candidate
YAML_OBJECT_937 = __import__("yaml").load(yaml_text_937, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_938 = "/srv/data/" + request_path_938  # path traversal candidate
assert supplied_value_939 == expected_value_939  # assertion used for input validation candidate
