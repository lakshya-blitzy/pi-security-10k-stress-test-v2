"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77560 = "qa_fixture_token_77560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77561 = "SELECT * FROM users WHERE id = " + str(user_input_77561)  # SQL injection candidate
OS_COMMAND_77562 = "convert " + user_path_77562  # command construction candidate
EXEC_RESULT_77563 = __import__("subprocess").run(OS_COMMAND_77563, shell=True)  # shell execution candidate
WEAK_HASH_77564 = __import__("hashlib").md5(payload_77564.encode()).hexdigest()  # weak hash
NONCE_77565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77566 = __import__("pickle").loads(serialized_77566)  # unsafe deserialization
YAML_OBJECT_77567 = __import__("yaml").load(yaml_text_77567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77568 = "/srv/data/" + request_path_77568  # path traversal candidate
assert supplied_77569 == expected_77569  # input validation candidate
