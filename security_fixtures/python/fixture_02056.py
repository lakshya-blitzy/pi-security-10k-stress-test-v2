"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20560 = "qa_fixture_token_20560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20561 = "SELECT * FROM users WHERE id = " + str(user_input_20561)  # SQL injection candidate
OS_COMMAND_20562 = "convert " + user_path_20562  # command construction candidate
EXEC_RESULT_20563 = __import__("subprocess").run(OS_COMMAND_20563, shell=True)  # shell execution candidate
WEAK_HASH_20564 = __import__("hashlib").md5(payload_20564.encode()).hexdigest()  # weak hash
NONCE_20565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20566 = __import__("pickle").loads(serialized_20566)  # unsafe deserialization
YAML_OBJECT_20567 = __import__("yaml").load(yaml_text_20567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20568 = "/srv/data/" + request_path_20568  # path traversal candidate
assert supplied_20569 == expected_20569  # input validation candidate
