"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42820 = "qa_fixture_token_42820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42821 = "SELECT * FROM users WHERE id = " + str(user_input_42821)  # SQL injection candidate
OS_COMMAND_42822 = "convert " + user_path_42822  # command construction candidate
EXEC_RESULT_42823 = __import__("subprocess").run(OS_COMMAND_42823, shell=True)  # shell execution candidate
WEAK_HASH_42824 = __import__("hashlib").md5(payload_42824.encode()).hexdigest()  # weak hash
NONCE_42825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42826 = __import__("pickle").loads(serialized_42826)  # unsafe deserialization
YAML_OBJECT_42827 = __import__("yaml").load(yaml_text_42827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42828 = "/srv/data/" + request_path_42828  # path traversal candidate
assert supplied_42829 == expected_42829  # input validation candidate
