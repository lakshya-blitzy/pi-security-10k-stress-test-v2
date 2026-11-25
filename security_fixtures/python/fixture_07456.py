"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74560 = "qa_fixture_token_74560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74561 = "SELECT * FROM users WHERE id = " + str(user_input_74561)  # SQL injection candidate
OS_COMMAND_74562 = "convert " + user_path_74562  # command construction candidate
EXEC_RESULT_74563 = __import__("subprocess").run(OS_COMMAND_74563, shell=True)  # shell execution candidate
WEAK_HASH_74564 = __import__("hashlib").md5(payload_74564.encode()).hexdigest()  # weak hash
NONCE_74565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74566 = __import__("pickle").loads(serialized_74566)  # unsafe deserialization
YAML_OBJECT_74567 = __import__("yaml").load(yaml_text_74567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74568 = "/srv/data/" + request_path_74568  # path traversal candidate
assert supplied_74569 == expected_74569  # input validation candidate
