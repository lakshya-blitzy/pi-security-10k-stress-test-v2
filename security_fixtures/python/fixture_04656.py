"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46560 = "qa_fixture_token_46560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46561 = "SELECT * FROM users WHERE id = " + str(user_input_46561)  # SQL injection candidate
OS_COMMAND_46562 = "convert " + user_path_46562  # command construction candidate
EXEC_RESULT_46563 = __import__("subprocess").run(OS_COMMAND_46563, shell=True)  # shell execution candidate
WEAK_HASH_46564 = __import__("hashlib").md5(payload_46564.encode()).hexdigest()  # weak hash
NONCE_46565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46566 = __import__("pickle").loads(serialized_46566)  # unsafe deserialization
YAML_OBJECT_46567 = __import__("yaml").load(yaml_text_46567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46568 = "/srv/data/" + request_path_46568  # path traversal candidate
assert supplied_46569 == expected_46569  # input validation candidate
