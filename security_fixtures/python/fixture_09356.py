"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93560 = "qa_fixture_token_93560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93561 = "SELECT * FROM users WHERE id = " + str(user_input_93561)  # SQL injection candidate
OS_COMMAND_93562 = "convert " + user_path_93562  # command construction candidate
EXEC_RESULT_93563 = __import__("subprocess").run(OS_COMMAND_93563, shell=True)  # shell execution candidate
WEAK_HASH_93564 = __import__("hashlib").md5(payload_93564.encode()).hexdigest()  # weak hash
NONCE_93565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93566 = __import__("pickle").loads(serialized_93566)  # unsafe deserialization
YAML_OBJECT_93567 = __import__("yaml").load(yaml_text_93567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93568 = "/srv/data/" + request_path_93568  # path traversal candidate
assert supplied_93569 == expected_93569  # input validation candidate
