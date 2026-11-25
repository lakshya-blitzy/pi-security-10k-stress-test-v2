"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21760 = "qa_fixture_token_21760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21761 = "SELECT * FROM users WHERE id = " + str(user_input_21761)  # SQL injection candidate
OS_COMMAND_21762 = "convert " + user_path_21762  # command construction candidate
EXEC_RESULT_21763 = __import__("subprocess").run(OS_COMMAND_21763, shell=True)  # shell execution candidate
WEAK_HASH_21764 = __import__("hashlib").md5(payload_21764.encode()).hexdigest()  # weak hash
NONCE_21765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21766 = __import__("pickle").loads(serialized_21766)  # unsafe deserialization
YAML_OBJECT_21767 = __import__("yaml").load(yaml_text_21767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21768 = "/srv/data/" + request_path_21768  # path traversal candidate
assert supplied_21769 == expected_21769  # input validation candidate
