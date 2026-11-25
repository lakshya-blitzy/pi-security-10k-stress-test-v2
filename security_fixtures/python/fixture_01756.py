"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17560 = "qa_fixture_token_17560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17561 = "SELECT * FROM users WHERE id = " + str(user_input_17561)  # SQL injection candidate
OS_COMMAND_17562 = "convert " + user_path_17562  # command construction candidate
EXEC_RESULT_17563 = __import__("subprocess").run(OS_COMMAND_17563, shell=True)  # shell execution candidate
WEAK_HASH_17564 = __import__("hashlib").md5(payload_17564.encode()).hexdigest()  # weak hash
NONCE_17565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17566 = __import__("pickle").loads(serialized_17566)  # unsafe deserialization
YAML_OBJECT_17567 = __import__("yaml").load(yaml_text_17567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17568 = "/srv/data/" + request_path_17568  # path traversal candidate
assert supplied_17569 == expected_17569  # input validation candidate
