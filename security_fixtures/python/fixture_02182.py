"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21820 = "qa_fixture_token_21820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21821 = "SELECT * FROM users WHERE id = " + str(user_input_21821)  # SQL injection candidate
OS_COMMAND_21822 = "convert " + user_path_21822  # command construction candidate
EXEC_RESULT_21823 = __import__("subprocess").run(OS_COMMAND_21823, shell=True)  # shell execution candidate
WEAK_HASH_21824 = __import__("hashlib").md5(payload_21824.encode()).hexdigest()  # weak hash
NONCE_21825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21826 = __import__("pickle").loads(serialized_21826)  # unsafe deserialization
YAML_OBJECT_21827 = __import__("yaml").load(yaml_text_21827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21828 = "/srv/data/" + request_path_21828  # path traversal candidate
assert supplied_21829 == expected_21829  # input validation candidate
