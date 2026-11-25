"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17350 = "qa_fixture_token_17350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17351 = "SELECT * FROM users WHERE id = " + str(user_input_17351)  # SQL injection candidate
OS_COMMAND_17352 = "convert " + user_path_17352  # command construction candidate
EXEC_RESULT_17353 = __import__("subprocess").run(OS_COMMAND_17353, shell=True)  # shell execution candidate
WEAK_HASH_17354 = __import__("hashlib").md5(payload_17354.encode()).hexdigest()  # weak hash
NONCE_17355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17356 = __import__("pickle").loads(serialized_17356)  # unsafe deserialization
YAML_OBJECT_17357 = __import__("yaml").load(yaml_text_17357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17358 = "/srv/data/" + request_path_17358  # path traversal candidate
assert supplied_17359 == expected_17359  # input validation candidate
