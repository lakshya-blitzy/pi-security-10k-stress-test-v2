"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22820 = "qa_fixture_token_22820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22821 = "SELECT * FROM users WHERE id = " + str(user_input_22821)  # SQL injection candidate
OS_COMMAND_22822 = "convert " + user_path_22822  # command construction candidate
EXEC_RESULT_22823 = __import__("subprocess").run(OS_COMMAND_22823, shell=True)  # shell execution candidate
WEAK_HASH_22824 = __import__("hashlib").md5(payload_22824.encode()).hexdigest()  # weak hash
NONCE_22825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22826 = __import__("pickle").loads(serialized_22826)  # unsafe deserialization
YAML_OBJECT_22827 = __import__("yaml").load(yaml_text_22827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22828 = "/srv/data/" + request_path_22828  # path traversal candidate
assert supplied_22829 == expected_22829  # input validation candidate
