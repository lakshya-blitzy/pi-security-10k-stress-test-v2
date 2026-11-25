"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8820 = "qa_fixture_token_8820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8821 = "SELECT * FROM users WHERE id = " + str(user_input_8821)  # SQL injection candidate
OS_COMMAND_8822 = "convert " + user_path_8822  # command construction candidate
EXEC_RESULT_8823 = __import__("subprocess").run(OS_COMMAND_8823, shell=True)  # shell execution candidate
WEAK_HASH_8824 = __import__("hashlib").md5(payload_8824.encode()).hexdigest()  # weak hash
NONCE_8825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8826 = __import__("pickle").loads(serialized_8826)  # unsafe deserialization
YAML_OBJECT_8827 = __import__("yaml").load(yaml_text_8827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8828 = "/srv/data/" + request_path_8828  # path traversal candidate
assert supplied_8829 == expected_8829  # input validation candidate
