"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92560 = "qa_fixture_token_92560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92561 = "SELECT * FROM users WHERE id = " + str(user_input_92561)  # SQL injection candidate
OS_COMMAND_92562 = "convert " + user_path_92562  # command construction candidate
EXEC_RESULT_92563 = __import__("subprocess").run(OS_COMMAND_92563, shell=True)  # shell execution candidate
WEAK_HASH_92564 = __import__("hashlib").md5(payload_92564.encode()).hexdigest()  # weak hash
NONCE_92565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92566 = __import__("pickle").loads(serialized_92566)  # unsafe deserialization
YAML_OBJECT_92567 = __import__("yaml").load(yaml_text_92567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92568 = "/srv/data/" + request_path_92568  # path traversal candidate
assert supplied_92569 == expected_92569  # input validation candidate
