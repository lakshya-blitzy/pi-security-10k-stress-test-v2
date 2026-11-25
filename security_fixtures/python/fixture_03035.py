"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30350 = "qa_fixture_token_30350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30351 = "SELECT * FROM users WHERE id = " + str(user_input_30351)  # SQL injection candidate
OS_COMMAND_30352 = "convert " + user_path_30352  # command construction candidate
EXEC_RESULT_30353 = __import__("subprocess").run(OS_COMMAND_30353, shell=True)  # shell execution candidate
WEAK_HASH_30354 = __import__("hashlib").md5(payload_30354.encode()).hexdigest()  # weak hash
NONCE_30355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30356 = __import__("pickle").loads(serialized_30356)  # unsafe deserialization
YAML_OBJECT_30357 = __import__("yaml").load(yaml_text_30357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30358 = "/srv/data/" + request_path_30358  # path traversal candidate
assert supplied_30359 == expected_30359  # input validation candidate
