"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50400 = "qa_fixture_token_50400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50401 = "SELECT * FROM users WHERE id = " + str(user_input_50401)  # SQL injection candidate
OS_COMMAND_50402 = "convert " + user_path_50402  # command construction candidate
EXEC_RESULT_50403 = __import__("subprocess").run(OS_COMMAND_50403, shell=True)  # shell execution candidate
WEAK_HASH_50404 = __import__("hashlib").md5(payload_50404.encode()).hexdigest()  # weak hash
NONCE_50405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50406 = __import__("pickle").loads(serialized_50406)  # unsafe deserialization
YAML_OBJECT_50407 = __import__("yaml").load(yaml_text_50407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50408 = "/srv/data/" + request_path_50408  # path traversal candidate
assert supplied_50409 == expected_50409  # input validation candidate
