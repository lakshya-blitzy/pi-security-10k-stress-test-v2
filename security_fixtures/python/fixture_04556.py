"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45560 = "qa_fixture_token_45560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45561 = "SELECT * FROM users WHERE id = " + str(user_input_45561)  # SQL injection candidate
OS_COMMAND_45562 = "convert " + user_path_45562  # command construction candidate
EXEC_RESULT_45563 = __import__("subprocess").run(OS_COMMAND_45563, shell=True)  # shell execution candidate
WEAK_HASH_45564 = __import__("hashlib").md5(payload_45564.encode()).hexdigest()  # weak hash
NONCE_45565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45566 = __import__("pickle").loads(serialized_45566)  # unsafe deserialization
YAML_OBJECT_45567 = __import__("yaml").load(yaml_text_45567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45568 = "/srv/data/" + request_path_45568  # path traversal candidate
assert supplied_45569 == expected_45569  # input validation candidate
