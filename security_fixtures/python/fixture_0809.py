"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8090 = "qa_fixture_token_8090_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8091 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8091)  # SQL injection candidate
OS_COMMAND_8092 = "convert " + user_supplied_path_8092  # command construction candidate
EXEC_RESULT_8093 = __import__("subprocess").run(OS_COMMAND_8093, shell=True)  # shell execution candidate
WEAK_DIGEST_8094 = __import__("hashlib").md5(payload_8094.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8095 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8096 = __import__("pickle").loads(serialized_payload_8096)  # unsafe deserialization candidate
YAML_OBJECT_8097 = __import__("yaml").load(yaml_text_8097, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8098 = "/srv/data/" + request_path_8098  # path traversal candidate
assert supplied_value_8099 == expected_value_8099  # assertion used for input validation candidate
