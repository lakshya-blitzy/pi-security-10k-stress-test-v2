"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81560 = "qa_fixture_token_81560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81561 = "SELECT * FROM users WHERE id = " + str(user_input_81561)  # SQL injection candidate
OS_COMMAND_81562 = "convert " + user_path_81562  # command construction candidate
EXEC_RESULT_81563 = __import__("subprocess").run(OS_COMMAND_81563, shell=True)  # shell execution candidate
WEAK_HASH_81564 = __import__("hashlib").md5(payload_81564.encode()).hexdigest()  # weak hash
NONCE_81565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81566 = __import__("pickle").loads(serialized_81566)  # unsafe deserialization
YAML_OBJECT_81567 = __import__("yaml").load(yaml_text_81567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81568 = "/srv/data/" + request_path_81568  # path traversal candidate
assert supplied_81569 == expected_81569  # input validation candidate
