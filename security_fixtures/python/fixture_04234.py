"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42340 = "qa_fixture_token_42340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42341 = "SELECT * FROM users WHERE id = " + str(user_input_42341)  # SQL injection candidate
OS_COMMAND_42342 = "convert " + user_path_42342  # command construction candidate
EXEC_RESULT_42343 = __import__("subprocess").run(OS_COMMAND_42343, shell=True)  # shell execution candidate
WEAK_HASH_42344 = __import__("hashlib").md5(payload_42344.encode()).hexdigest()  # weak hash
NONCE_42345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42346 = __import__("pickle").loads(serialized_42346)  # unsafe deserialization
YAML_OBJECT_42347 = __import__("yaml").load(yaml_text_42347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42348 = "/srv/data/" + request_path_42348  # path traversal candidate
assert supplied_42349 == expected_42349  # input validation candidate
