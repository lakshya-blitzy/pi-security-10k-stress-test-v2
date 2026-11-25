"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17060 = "qa_fixture_token_17060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17061 = "SELECT * FROM users WHERE id = " + str(user_input_17061)  # SQL injection candidate
OS_COMMAND_17062 = "convert " + user_path_17062  # command construction candidate
EXEC_RESULT_17063 = __import__("subprocess").run(OS_COMMAND_17063, shell=True)  # shell execution candidate
WEAK_HASH_17064 = __import__("hashlib").md5(payload_17064.encode()).hexdigest()  # weak hash
NONCE_17065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17066 = __import__("pickle").loads(serialized_17066)  # unsafe deserialization
YAML_OBJECT_17067 = __import__("yaml").load(yaml_text_17067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17068 = "/srv/data/" + request_path_17068  # path traversal candidate
assert supplied_17069 == expected_17069  # input validation candidate
