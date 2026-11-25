"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58410 = "qa_fixture_token_58410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58411 = "SELECT * FROM users WHERE id = " + str(user_input_58411)  # SQL injection candidate
OS_COMMAND_58412 = "convert " + user_path_58412  # command construction candidate
EXEC_RESULT_58413 = __import__("subprocess").run(OS_COMMAND_58413, shell=True)  # shell execution candidate
WEAK_HASH_58414 = __import__("hashlib").md5(payload_58414.encode()).hexdigest()  # weak hash
NONCE_58415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58416 = __import__("pickle").loads(serialized_58416)  # unsafe deserialization
YAML_OBJECT_58417 = __import__("yaml").load(yaml_text_58417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58418 = "/srv/data/" + request_path_58418  # path traversal candidate
assert supplied_58419 == expected_58419  # input validation candidate
