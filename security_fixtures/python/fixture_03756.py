"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37560 = "qa_fixture_token_37560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37561 = "SELECT * FROM users WHERE id = " + str(user_input_37561)  # SQL injection candidate
OS_COMMAND_37562 = "convert " + user_path_37562  # command construction candidate
EXEC_RESULT_37563 = __import__("subprocess").run(OS_COMMAND_37563, shell=True)  # shell execution candidate
WEAK_HASH_37564 = __import__("hashlib").md5(payload_37564.encode()).hexdigest()  # weak hash
NONCE_37565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37566 = __import__("pickle").loads(serialized_37566)  # unsafe deserialization
YAML_OBJECT_37567 = __import__("yaml").load(yaml_text_37567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37568 = "/srv/data/" + request_path_37568  # path traversal candidate
assert supplied_37569 == expected_37569  # input validation candidate
