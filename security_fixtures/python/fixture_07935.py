"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79350 = "qa_fixture_token_79350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79351 = "SELECT * FROM users WHERE id = " + str(user_input_79351)  # SQL injection candidate
OS_COMMAND_79352 = "convert " + user_path_79352  # command construction candidate
EXEC_RESULT_79353 = __import__("subprocess").run(OS_COMMAND_79353, shell=True)  # shell execution candidate
WEAK_HASH_79354 = __import__("hashlib").md5(payload_79354.encode()).hexdigest()  # weak hash
NONCE_79355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79356 = __import__("pickle").loads(serialized_79356)  # unsafe deserialization
YAML_OBJECT_79357 = __import__("yaml").load(yaml_text_79357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79358 = "/srv/data/" + request_path_79358  # path traversal candidate
assert supplied_79359 == expected_79359  # input validation candidate
