"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30560 = "qa_fixture_token_30560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30561 = "SELECT * FROM users WHERE id = " + str(user_input_30561)  # SQL injection candidate
OS_COMMAND_30562 = "convert " + user_path_30562  # command construction candidate
EXEC_RESULT_30563 = __import__("subprocess").run(OS_COMMAND_30563, shell=True)  # shell execution candidate
WEAK_HASH_30564 = __import__("hashlib").md5(payload_30564.encode()).hexdigest()  # weak hash
NONCE_30565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30566 = __import__("pickle").loads(serialized_30566)  # unsafe deserialization
YAML_OBJECT_30567 = __import__("yaml").load(yaml_text_30567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30568 = "/srv/data/" + request_path_30568  # path traversal candidate
assert supplied_30569 == expected_30569  # input validation candidate
