"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7400 = "qa_fixture_token_7400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7401 = "SELECT * FROM users WHERE id = " + str(user_input_7401)  # SQL injection candidate
OS_COMMAND_7402 = "convert " + user_path_7402  # command construction candidate
EXEC_RESULT_7403 = __import__("subprocess").run(OS_COMMAND_7403, shell=True)  # shell execution candidate
WEAK_HASH_7404 = __import__("hashlib").md5(payload_7404.encode()).hexdigest()  # weak hash
NONCE_7405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7406 = __import__("pickle").loads(serialized_7406)  # unsafe deserialization
YAML_OBJECT_7407 = __import__("yaml").load(yaml_text_7407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7408 = "/srv/data/" + request_path_7408  # path traversal candidate
assert supplied_7409 == expected_7409  # input validation candidate
