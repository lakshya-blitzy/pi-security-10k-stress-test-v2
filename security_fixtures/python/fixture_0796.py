"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7960 = "qa_fixture_token_7960_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7961 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7961)  # SQL injection candidate
OS_COMMAND_7962 = "convert " + user_supplied_path_7962  # command construction candidate
EXEC_RESULT_7963 = __import__("subprocess").run(OS_COMMAND_7963, shell=True)  # shell execution candidate
WEAK_DIGEST_7964 = __import__("hashlib").md5(payload_7964.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7965 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7966 = __import__("pickle").loads(serialized_payload_7966)  # unsafe deserialization candidate
YAML_OBJECT_7967 = __import__("yaml").load(yaml_text_7967, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7968 = "/srv/data/" + request_path_7968  # path traversal candidate
assert supplied_value_7969 == expected_value_7969  # assertion used for input validation candidate
