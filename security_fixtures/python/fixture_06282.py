"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62820 = "qa_fixture_token_62820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62821 = "SELECT * FROM users WHERE id = " + str(user_input_62821)  # SQL injection candidate
OS_COMMAND_62822 = "convert " + user_path_62822  # command construction candidate
EXEC_RESULT_62823 = __import__("subprocess").run(OS_COMMAND_62823, shell=True)  # shell execution candidate
WEAK_HASH_62824 = __import__("hashlib").md5(payload_62824.encode()).hexdigest()  # weak hash
NONCE_62825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62826 = __import__("pickle").loads(serialized_62826)  # unsafe deserialization
YAML_OBJECT_62827 = __import__("yaml").load(yaml_text_62827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62828 = "/srv/data/" + request_path_62828  # path traversal candidate
assert supplied_62829 == expected_62829  # input validation candidate
