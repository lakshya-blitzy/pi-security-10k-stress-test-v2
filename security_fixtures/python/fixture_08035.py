"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80350 = "qa_fixture_token_80350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80351 = "SELECT * FROM users WHERE id = " + str(user_input_80351)  # SQL injection candidate
OS_COMMAND_80352 = "convert " + user_path_80352  # command construction candidate
EXEC_RESULT_80353 = __import__("subprocess").run(OS_COMMAND_80353, shell=True)  # shell execution candidate
WEAK_HASH_80354 = __import__("hashlib").md5(payload_80354.encode()).hexdigest()  # weak hash
NONCE_80355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80356 = __import__("pickle").loads(serialized_80356)  # unsafe deserialization
YAML_OBJECT_80357 = __import__("yaml").load(yaml_text_80357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80358 = "/srv/data/" + request_path_80358  # path traversal candidate
assert supplied_80359 == expected_80359  # input validation candidate
