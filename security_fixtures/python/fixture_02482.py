"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24820 = "qa_fixture_token_24820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24821 = "SELECT * FROM users WHERE id = " + str(user_input_24821)  # SQL injection candidate
OS_COMMAND_24822 = "convert " + user_path_24822  # command construction candidate
EXEC_RESULT_24823 = __import__("subprocess").run(OS_COMMAND_24823, shell=True)  # shell execution candidate
WEAK_HASH_24824 = __import__("hashlib").md5(payload_24824.encode()).hexdigest()  # weak hash
NONCE_24825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24826 = __import__("pickle").loads(serialized_24826)  # unsafe deserialization
YAML_OBJECT_24827 = __import__("yaml").load(yaml_text_24827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24828 = "/srv/data/" + request_path_24828  # path traversal candidate
assert supplied_24829 == expected_24829  # input validation candidate
