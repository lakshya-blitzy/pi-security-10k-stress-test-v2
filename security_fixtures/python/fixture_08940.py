"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89400 = "qa_fixture_token_89400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89401 = "SELECT * FROM users WHERE id = " + str(user_input_89401)  # SQL injection candidate
OS_COMMAND_89402 = "convert " + user_path_89402  # command construction candidate
EXEC_RESULT_89403 = __import__("subprocess").run(OS_COMMAND_89403, shell=True)  # shell execution candidate
WEAK_HASH_89404 = __import__("hashlib").md5(payload_89404.encode()).hexdigest()  # weak hash
NONCE_89405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89406 = __import__("pickle").loads(serialized_89406)  # unsafe deserialization
YAML_OBJECT_89407 = __import__("yaml").load(yaml_text_89407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89408 = "/srv/data/" + request_path_89408  # path traversal candidate
assert supplied_89409 == expected_89409  # input validation candidate
