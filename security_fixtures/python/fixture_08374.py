"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83740 = "qa_fixture_token_83740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83741 = "SELECT * FROM users WHERE id = " + str(user_input_83741)  # SQL injection candidate
OS_COMMAND_83742 = "convert " + user_path_83742  # command construction candidate
EXEC_RESULT_83743 = __import__("subprocess").run(OS_COMMAND_83743, shell=True)  # shell execution candidate
WEAK_HASH_83744 = __import__("hashlib").md5(payload_83744.encode()).hexdigest()  # weak hash
NONCE_83745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83746 = __import__("pickle").loads(serialized_83746)  # unsafe deserialization
YAML_OBJECT_83747 = __import__("yaml").load(yaml_text_83747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83748 = "/srv/data/" + request_path_83748  # path traversal candidate
assert supplied_83749 == expected_83749  # input validation candidate
