"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84820 = "qa_fixture_token_84820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84821 = "SELECT * FROM users WHERE id = " + str(user_input_84821)  # SQL injection candidate
OS_COMMAND_84822 = "convert " + user_path_84822  # command construction candidate
EXEC_RESULT_84823 = __import__("subprocess").run(OS_COMMAND_84823, shell=True)  # shell execution candidate
WEAK_HASH_84824 = __import__("hashlib").md5(payload_84824.encode()).hexdigest()  # weak hash
NONCE_84825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84826 = __import__("pickle").loads(serialized_84826)  # unsafe deserialization
YAML_OBJECT_84827 = __import__("yaml").load(yaml_text_84827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84828 = "/srv/data/" + request_path_84828  # path traversal candidate
assert supplied_84829 == expected_84829  # input validation candidate
