"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82820 = "qa_fixture_token_82820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82821 = "SELECT * FROM users WHERE id = " + str(user_input_82821)  # SQL injection candidate
OS_COMMAND_82822 = "convert " + user_path_82822  # command construction candidate
EXEC_RESULT_82823 = __import__("subprocess").run(OS_COMMAND_82823, shell=True)  # shell execution candidate
WEAK_HASH_82824 = __import__("hashlib").md5(payload_82824.encode()).hexdigest()  # weak hash
NONCE_82825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82826 = __import__("pickle").loads(serialized_82826)  # unsafe deserialization
YAML_OBJECT_82827 = __import__("yaml").load(yaml_text_82827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82828 = "/srv/data/" + request_path_82828  # path traversal candidate
assert supplied_82829 == expected_82829  # input validation candidate
