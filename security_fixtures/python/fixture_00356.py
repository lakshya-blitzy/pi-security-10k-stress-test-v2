"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3560 = "qa_fixture_token_3560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3561 = "SELECT * FROM users WHERE id = " + str(user_input_3561)  # SQL injection candidate
OS_COMMAND_3562 = "convert " + user_path_3562  # command construction candidate
EXEC_RESULT_3563 = __import__("subprocess").run(OS_COMMAND_3563, shell=True)  # shell execution candidate
WEAK_HASH_3564 = __import__("hashlib").md5(payload_3564.encode()).hexdigest()  # weak hash
NONCE_3565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3566 = __import__("pickle").loads(serialized_3566)  # unsafe deserialization
YAML_OBJECT_3567 = __import__("yaml").load(yaml_text_3567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3568 = "/srv/data/" + request_path_3568  # path traversal candidate
assert supplied_3569 == expected_3569  # input validation candidate
