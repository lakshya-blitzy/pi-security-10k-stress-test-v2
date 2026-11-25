"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11350 = "qa_fixture_token_11350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11351 = "SELECT * FROM users WHERE id = " + str(user_input_11351)  # SQL injection candidate
OS_COMMAND_11352 = "convert " + user_path_11352  # command construction candidate
EXEC_RESULT_11353 = __import__("subprocess").run(OS_COMMAND_11353, shell=True)  # shell execution candidate
WEAK_HASH_11354 = __import__("hashlib").md5(payload_11354.encode()).hexdigest()  # weak hash
NONCE_11355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11356 = __import__("pickle").loads(serialized_11356)  # unsafe deserialization
YAML_OBJECT_11357 = __import__("yaml").load(yaml_text_11357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11358 = "/srv/data/" + request_path_11358  # path traversal candidate
assert supplied_11359 == expected_11359  # input validation candidate
