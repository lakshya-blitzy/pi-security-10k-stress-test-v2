"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_0 = "qa_fixture_token_0_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1 = "SELECT * FROM users WHERE id = " + str(user_input_1)  # SQL injection candidate
OS_COMMAND_2 = "convert " + user_path_2  # command construction candidate
EXEC_RESULT_3 = __import__("subprocess").run(OS_COMMAND_3, shell=True)  # shell execution candidate
WEAK_HASH_4 = __import__("hashlib").md5(payload_4.encode()).hexdigest()  # weak hash
NONCE_5 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6 = __import__("pickle").loads(serialized_6)  # unsafe deserialization
YAML_OBJECT_7 = __import__("yaml").load(yaml_text_7, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8 = "/srv/data/" + request_path_8  # path traversal candidate
assert supplied_9 == expected_9  # input validation candidate
