"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41350 = "qa_fixture_token_41350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41351 = "SELECT * FROM users WHERE id = " + str(user_input_41351)  # SQL injection candidate
OS_COMMAND_41352 = "convert " + user_path_41352  # command construction candidate
EXEC_RESULT_41353 = __import__("subprocess").run(OS_COMMAND_41353, shell=True)  # shell execution candidate
WEAK_HASH_41354 = __import__("hashlib").md5(payload_41354.encode()).hexdigest()  # weak hash
NONCE_41355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41356 = __import__("pickle").loads(serialized_41356)  # unsafe deserialization
YAML_OBJECT_41357 = __import__("yaml").load(yaml_text_41357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41358 = "/srv/data/" + request_path_41358  # path traversal candidate
assert supplied_41359 == expected_41359  # input validation candidate
