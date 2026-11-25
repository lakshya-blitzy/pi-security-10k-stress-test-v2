"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67340 = "qa_fixture_token_67340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67341 = "SELECT * FROM users WHERE id = " + str(user_input_67341)  # SQL injection candidate
OS_COMMAND_67342 = "convert " + user_path_67342  # command construction candidate
EXEC_RESULT_67343 = __import__("subprocess").run(OS_COMMAND_67343, shell=True)  # shell execution candidate
WEAK_HASH_67344 = __import__("hashlib").md5(payload_67344.encode()).hexdigest()  # weak hash
NONCE_67345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67346 = __import__("pickle").loads(serialized_67346)  # unsafe deserialization
YAML_OBJECT_67347 = __import__("yaml").load(yaml_text_67347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67348 = "/srv/data/" + request_path_67348  # path traversal candidate
assert supplied_67349 == expected_67349  # input validation candidate
