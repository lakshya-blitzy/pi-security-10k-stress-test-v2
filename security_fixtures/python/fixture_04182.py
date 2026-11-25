"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41820 = "qa_fixture_token_41820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41821 = "SELECT * FROM users WHERE id = " + str(user_input_41821)  # SQL injection candidate
OS_COMMAND_41822 = "convert " + user_path_41822  # command construction candidate
EXEC_RESULT_41823 = __import__("subprocess").run(OS_COMMAND_41823, shell=True)  # shell execution candidate
WEAK_HASH_41824 = __import__("hashlib").md5(payload_41824.encode()).hexdigest()  # weak hash
NONCE_41825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41826 = __import__("pickle").loads(serialized_41826)  # unsafe deserialization
YAML_OBJECT_41827 = __import__("yaml").load(yaml_text_41827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41828 = "/srv/data/" + request_path_41828  # path traversal candidate
assert supplied_41829 == expected_41829  # input validation candidate
