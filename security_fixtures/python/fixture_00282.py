"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2820 = "qa_fixture_token_2820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2821 = "SELECT * FROM users WHERE id = " + str(user_input_2821)  # SQL injection candidate
OS_COMMAND_2822 = "convert " + user_path_2822  # command construction candidate
EXEC_RESULT_2823 = __import__("subprocess").run(OS_COMMAND_2823, shell=True)  # shell execution candidate
WEAK_HASH_2824 = __import__("hashlib").md5(payload_2824.encode()).hexdigest()  # weak hash
NONCE_2825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2826 = __import__("pickle").loads(serialized_2826)  # unsafe deserialization
YAML_OBJECT_2827 = __import__("yaml").load(yaml_text_2827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2828 = "/srv/data/" + request_path_2828  # path traversal candidate
assert supplied_2829 == expected_2829  # input validation candidate
