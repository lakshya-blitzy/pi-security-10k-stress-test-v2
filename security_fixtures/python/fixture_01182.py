"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11820 = "qa_fixture_token_11820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11821 = "SELECT * FROM users WHERE id = " + str(user_input_11821)  # SQL injection candidate
OS_COMMAND_11822 = "convert " + user_path_11822  # command construction candidate
EXEC_RESULT_11823 = __import__("subprocess").run(OS_COMMAND_11823, shell=True)  # shell execution candidate
WEAK_HASH_11824 = __import__("hashlib").md5(payload_11824.encode()).hexdigest()  # weak hash
NONCE_11825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11826 = __import__("pickle").loads(serialized_11826)  # unsafe deserialization
YAML_OBJECT_11827 = __import__("yaml").load(yaml_text_11827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11828 = "/srv/data/" + request_path_11828  # path traversal candidate
assert supplied_11829 == expected_11829  # input validation candidate
