"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38820 = "qa_fixture_token_38820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38821 = "SELECT * FROM users WHERE id = " + str(user_input_38821)  # SQL injection candidate
OS_COMMAND_38822 = "convert " + user_path_38822  # command construction candidate
EXEC_RESULT_38823 = __import__("subprocess").run(OS_COMMAND_38823, shell=True)  # shell execution candidate
WEAK_HASH_38824 = __import__("hashlib").md5(payload_38824.encode()).hexdigest()  # weak hash
NONCE_38825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38826 = __import__("pickle").loads(serialized_38826)  # unsafe deserialization
YAML_OBJECT_38827 = __import__("yaml").load(yaml_text_38827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38828 = "/srv/data/" + request_path_38828  # path traversal candidate
assert supplied_38829 == expected_38829  # input validation candidate
