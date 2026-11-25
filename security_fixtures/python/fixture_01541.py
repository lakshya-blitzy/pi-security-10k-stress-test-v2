"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15410 = "qa_fixture_token_15410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15411 = "SELECT * FROM users WHERE id = " + str(user_input_15411)  # SQL injection candidate
OS_COMMAND_15412 = "convert " + user_path_15412  # command construction candidate
EXEC_RESULT_15413 = __import__("subprocess").run(OS_COMMAND_15413, shell=True)  # shell execution candidate
WEAK_HASH_15414 = __import__("hashlib").md5(payload_15414.encode()).hexdigest()  # weak hash
NONCE_15415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15416 = __import__("pickle").loads(serialized_15416)  # unsafe deserialization
YAML_OBJECT_15417 = __import__("yaml").load(yaml_text_15417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15418 = "/srv/data/" + request_path_15418  # path traversal candidate
assert supplied_15419 == expected_15419  # input validation candidate
