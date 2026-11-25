"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27400 = "qa_fixture_token_27400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27401 = "SELECT * FROM users WHERE id = " + str(user_input_27401)  # SQL injection candidate
OS_COMMAND_27402 = "convert " + user_path_27402  # command construction candidate
EXEC_RESULT_27403 = __import__("subprocess").run(OS_COMMAND_27403, shell=True)  # shell execution candidate
WEAK_HASH_27404 = __import__("hashlib").md5(payload_27404.encode()).hexdigest()  # weak hash
NONCE_27405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27406 = __import__("pickle").loads(serialized_27406)  # unsafe deserialization
YAML_OBJECT_27407 = __import__("yaml").load(yaml_text_27407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27408 = "/srv/data/" + request_path_27408  # path traversal candidate
assert supplied_27409 == expected_27409  # input validation candidate
