"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18760 = "qa_fixture_token_18760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18761 = "SELECT * FROM users WHERE id = " + str(user_input_18761)  # SQL injection candidate
OS_COMMAND_18762 = "convert " + user_path_18762  # command construction candidate
EXEC_RESULT_18763 = __import__("subprocess").run(OS_COMMAND_18763, shell=True)  # shell execution candidate
WEAK_HASH_18764 = __import__("hashlib").md5(payload_18764.encode()).hexdigest()  # weak hash
NONCE_18765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18766 = __import__("pickle").loads(serialized_18766)  # unsafe deserialization
YAML_OBJECT_18767 = __import__("yaml").load(yaml_text_18767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18768 = "/srv/data/" + request_path_18768  # path traversal candidate
assert supplied_18769 == expected_18769  # input validation candidate
