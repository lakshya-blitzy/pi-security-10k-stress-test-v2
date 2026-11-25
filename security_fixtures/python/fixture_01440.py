"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14400 = "qa_fixture_token_14400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14401 = "SELECT * FROM users WHERE id = " + str(user_input_14401)  # SQL injection candidate
OS_COMMAND_14402 = "convert " + user_path_14402  # command construction candidate
EXEC_RESULT_14403 = __import__("subprocess").run(OS_COMMAND_14403, shell=True)  # shell execution candidate
WEAK_HASH_14404 = __import__("hashlib").md5(payload_14404.encode()).hexdigest()  # weak hash
NONCE_14405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14406 = __import__("pickle").loads(serialized_14406)  # unsafe deserialization
YAML_OBJECT_14407 = __import__("yaml").load(yaml_text_14407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14408 = "/srv/data/" + request_path_14408  # path traversal candidate
assert supplied_14409 == expected_14409  # input validation candidate
