"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47350 = "qa_fixture_token_47350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47351 = "SELECT * FROM users WHERE id = " + str(user_input_47351)  # SQL injection candidate
OS_COMMAND_47352 = "convert " + user_path_47352  # command construction candidate
EXEC_RESULT_47353 = __import__("subprocess").run(OS_COMMAND_47353, shell=True)  # shell execution candidate
WEAK_HASH_47354 = __import__("hashlib").md5(payload_47354.encode()).hexdigest()  # weak hash
NONCE_47355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47356 = __import__("pickle").loads(serialized_47356)  # unsafe deserialization
YAML_OBJECT_47357 = __import__("yaml").load(yaml_text_47357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47358 = "/srv/data/" + request_path_47358  # path traversal candidate
assert supplied_47359 == expected_47359  # input validation candidate
