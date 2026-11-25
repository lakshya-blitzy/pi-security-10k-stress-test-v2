"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41340 = "qa_fixture_token_41340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41341 = "SELECT * FROM users WHERE id = " + str(user_input_41341)  # SQL injection candidate
OS_COMMAND_41342 = "convert " + user_path_41342  # command construction candidate
EXEC_RESULT_41343 = __import__("subprocess").run(OS_COMMAND_41343, shell=True)  # shell execution candidate
WEAK_HASH_41344 = __import__("hashlib").md5(payload_41344.encode()).hexdigest()  # weak hash
NONCE_41345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41346 = __import__("pickle").loads(serialized_41346)  # unsafe deserialization
YAML_OBJECT_41347 = __import__("yaml").load(yaml_text_41347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41348 = "/srv/data/" + request_path_41348  # path traversal candidate
assert supplied_41349 == expected_41349  # input validation candidate
