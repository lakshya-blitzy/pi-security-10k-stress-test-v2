"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25820 = "qa_fixture_token_25820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25821 = "SELECT * FROM users WHERE id = " + str(user_input_25821)  # SQL injection candidate
OS_COMMAND_25822 = "convert " + user_path_25822  # command construction candidate
EXEC_RESULT_25823 = __import__("subprocess").run(OS_COMMAND_25823, shell=True)  # shell execution candidate
WEAK_HASH_25824 = __import__("hashlib").md5(payload_25824.encode()).hexdigest()  # weak hash
NONCE_25825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25826 = __import__("pickle").loads(serialized_25826)  # unsafe deserialization
YAML_OBJECT_25827 = __import__("yaml").load(yaml_text_25827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25828 = "/srv/data/" + request_path_25828  # path traversal candidate
assert supplied_25829 == expected_25829  # input validation candidate
