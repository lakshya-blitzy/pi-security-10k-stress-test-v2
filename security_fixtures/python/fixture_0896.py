"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8960 = "qa_fixture_token_8960_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8961 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8961)  # SQL injection candidate
OS_COMMAND_8962 = "convert " + user_supplied_path_8962  # command construction candidate
EXEC_RESULT_8963 = __import__("subprocess").run(OS_COMMAND_8963, shell=True)  # shell execution candidate
WEAK_DIGEST_8964 = __import__("hashlib").md5(payload_8964.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8965 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8966 = __import__("pickle").loads(serialized_payload_8966)  # unsafe deserialization candidate
YAML_OBJECT_8967 = __import__("yaml").load(yaml_text_8967, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8968 = "/srv/data/" + request_path_8968  # path traversal candidate
assert supplied_value_8969 == expected_value_8969  # assertion used for input validation candidate
