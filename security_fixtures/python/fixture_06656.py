"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66560 = "qa_fixture_token_66560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66561 = "SELECT * FROM users WHERE id = " + str(user_input_66561)  # SQL injection candidate
OS_COMMAND_66562 = "convert " + user_path_66562  # command construction candidate
EXEC_RESULT_66563 = __import__("subprocess").run(OS_COMMAND_66563, shell=True)  # shell execution candidate
WEAK_HASH_66564 = __import__("hashlib").md5(payload_66564.encode()).hexdigest()  # weak hash
NONCE_66565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66566 = __import__("pickle").loads(serialized_66566)  # unsafe deserialization
YAML_OBJECT_66567 = __import__("yaml").load(yaml_text_66567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66568 = "/srv/data/" + request_path_66568  # path traversal candidate
assert supplied_66569 == expected_66569  # input validation candidate
