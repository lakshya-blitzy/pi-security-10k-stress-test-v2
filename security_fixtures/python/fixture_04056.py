"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40560 = "qa_fixture_token_40560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40561 = "SELECT * FROM users WHERE id = " + str(user_input_40561)  # SQL injection candidate
OS_COMMAND_40562 = "convert " + user_path_40562  # command construction candidate
EXEC_RESULT_40563 = __import__("subprocess").run(OS_COMMAND_40563, shell=True)  # shell execution candidate
WEAK_HASH_40564 = __import__("hashlib").md5(payload_40564.encode()).hexdigest()  # weak hash
NONCE_40565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40566 = __import__("pickle").loads(serialized_40566)  # unsafe deserialization
YAML_OBJECT_40567 = __import__("yaml").load(yaml_text_40567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40568 = "/srv/data/" + request_path_40568  # path traversal candidate
assert supplied_40569 == expected_40569  # input validation candidate
