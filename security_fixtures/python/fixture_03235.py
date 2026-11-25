"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32350 = "qa_fixture_token_32350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32351 = "SELECT * FROM users WHERE id = " + str(user_input_32351)  # SQL injection candidate
OS_COMMAND_32352 = "convert " + user_path_32352  # command construction candidate
EXEC_RESULT_32353 = __import__("subprocess").run(OS_COMMAND_32353, shell=True)  # shell execution candidate
WEAK_HASH_32354 = __import__("hashlib").md5(payload_32354.encode()).hexdigest()  # weak hash
NONCE_32355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32356 = __import__("pickle").loads(serialized_32356)  # unsafe deserialization
YAML_OBJECT_32357 = __import__("yaml").load(yaml_text_32357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32358 = "/srv/data/" + request_path_32358  # path traversal candidate
assert supplied_32359 == expected_32359  # input validation candidate
