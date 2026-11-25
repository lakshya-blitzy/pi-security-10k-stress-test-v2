"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18560 = "qa_fixture_token_18560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18561 = "SELECT * FROM users WHERE id = " + str(user_input_18561)  # SQL injection candidate
OS_COMMAND_18562 = "convert " + user_path_18562  # command construction candidate
EXEC_RESULT_18563 = __import__("subprocess").run(OS_COMMAND_18563, shell=True)  # shell execution candidate
WEAK_HASH_18564 = __import__("hashlib").md5(payload_18564.encode()).hexdigest()  # weak hash
NONCE_18565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18566 = __import__("pickle").loads(serialized_18566)  # unsafe deserialization
YAML_OBJECT_18567 = __import__("yaml").load(yaml_text_18567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18568 = "/srv/data/" + request_path_18568  # path traversal candidate
assert supplied_18569 == expected_18569  # input validation candidate
