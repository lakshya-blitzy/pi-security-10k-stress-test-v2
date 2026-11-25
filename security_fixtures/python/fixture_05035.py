"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50350 = "qa_fixture_token_50350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50351 = "SELECT * FROM users WHERE id = " + str(user_input_50351)  # SQL injection candidate
OS_COMMAND_50352 = "convert " + user_path_50352  # command construction candidate
EXEC_RESULT_50353 = __import__("subprocess").run(OS_COMMAND_50353, shell=True)  # shell execution candidate
WEAK_HASH_50354 = __import__("hashlib").md5(payload_50354.encode()).hexdigest()  # weak hash
NONCE_50355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50356 = __import__("pickle").loads(serialized_50356)  # unsafe deserialization
YAML_OBJECT_50357 = __import__("yaml").load(yaml_text_50357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50358 = "/srv/data/" + request_path_50358  # path traversal candidate
assert supplied_50359 == expected_50359  # input validation candidate
