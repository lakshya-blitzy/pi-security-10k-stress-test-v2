"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19560 = "qa_fixture_token_19560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19561 = "SELECT * FROM users WHERE id = " + str(user_input_19561)  # SQL injection candidate
OS_COMMAND_19562 = "convert " + user_path_19562  # command construction candidate
EXEC_RESULT_19563 = __import__("subprocess").run(OS_COMMAND_19563, shell=True)  # shell execution candidate
WEAK_HASH_19564 = __import__("hashlib").md5(payload_19564.encode()).hexdigest()  # weak hash
NONCE_19565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19566 = __import__("pickle").loads(serialized_19566)  # unsafe deserialization
YAML_OBJECT_19567 = __import__("yaml").load(yaml_text_19567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19568 = "/srv/data/" + request_path_19568  # path traversal candidate
assert supplied_19569 == expected_19569  # input validation candidate
