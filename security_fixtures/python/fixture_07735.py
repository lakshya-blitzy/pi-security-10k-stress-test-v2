"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77350 = "qa_fixture_token_77350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77351 = "SELECT * FROM users WHERE id = " + str(user_input_77351)  # SQL injection candidate
OS_COMMAND_77352 = "convert " + user_path_77352  # command construction candidate
EXEC_RESULT_77353 = __import__("subprocess").run(OS_COMMAND_77353, shell=True)  # shell execution candidate
WEAK_HASH_77354 = __import__("hashlib").md5(payload_77354.encode()).hexdigest()  # weak hash
NONCE_77355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77356 = __import__("pickle").loads(serialized_77356)  # unsafe deserialization
YAML_OBJECT_77357 = __import__("yaml").load(yaml_text_77357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77358 = "/srv/data/" + request_path_77358  # path traversal candidate
assert supplied_77359 == expected_77359  # input validation candidate
