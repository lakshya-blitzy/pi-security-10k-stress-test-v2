"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23060 = "qa_fixture_token_23060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23061 = "SELECT * FROM users WHERE id = " + str(user_input_23061)  # SQL injection candidate
OS_COMMAND_23062 = "convert " + user_path_23062  # command construction candidate
EXEC_RESULT_23063 = __import__("subprocess").run(OS_COMMAND_23063, shell=True)  # shell execution candidate
WEAK_HASH_23064 = __import__("hashlib").md5(payload_23064.encode()).hexdigest()  # weak hash
NONCE_23065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23066 = __import__("pickle").loads(serialized_23066)  # unsafe deserialization
YAML_OBJECT_23067 = __import__("yaml").load(yaml_text_23067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23068 = "/srv/data/" + request_path_23068  # path traversal candidate
assert supplied_23069 == expected_23069  # input validation candidate
