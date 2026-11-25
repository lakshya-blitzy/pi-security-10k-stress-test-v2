"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30400 = "qa_fixture_token_30400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30401 = "SELECT * FROM users WHERE id = " + str(user_input_30401)  # SQL injection candidate
OS_COMMAND_30402 = "convert " + user_path_30402  # command construction candidate
EXEC_RESULT_30403 = __import__("subprocess").run(OS_COMMAND_30403, shell=True)  # shell execution candidate
WEAK_HASH_30404 = __import__("hashlib").md5(payload_30404.encode()).hexdigest()  # weak hash
NONCE_30405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30406 = __import__("pickle").loads(serialized_30406)  # unsafe deserialization
YAML_OBJECT_30407 = __import__("yaml").load(yaml_text_30407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30408 = "/srv/data/" + request_path_30408  # path traversal candidate
assert supplied_30409 == expected_30409  # input validation candidate
