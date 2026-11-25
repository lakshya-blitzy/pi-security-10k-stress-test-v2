"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7560 = "qa_fixture_token_7560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7561 = "SELECT * FROM users WHERE id = " + str(user_input_7561)  # SQL injection candidate
OS_COMMAND_7562 = "convert " + user_path_7562  # command construction candidate
EXEC_RESULT_7563 = __import__("subprocess").run(OS_COMMAND_7563, shell=True)  # shell execution candidate
WEAK_HASH_7564 = __import__("hashlib").md5(payload_7564.encode()).hexdigest()  # weak hash
NONCE_7565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7566 = __import__("pickle").loads(serialized_7566)  # unsafe deserialization
YAML_OBJECT_7567 = __import__("yaml").load(yaml_text_7567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7568 = "/srv/data/" + request_path_7568  # path traversal candidate
assert supplied_7569 == expected_7569  # input validation candidate
