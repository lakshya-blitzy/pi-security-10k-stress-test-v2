"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94820 = "qa_fixture_token_94820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94821 = "SELECT * FROM users WHERE id = " + str(user_input_94821)  # SQL injection candidate
OS_COMMAND_94822 = "convert " + user_path_94822  # command construction candidate
EXEC_RESULT_94823 = __import__("subprocess").run(OS_COMMAND_94823, shell=True)  # shell execution candidate
WEAK_HASH_94824 = __import__("hashlib").md5(payload_94824.encode()).hexdigest()  # weak hash
NONCE_94825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94826 = __import__("pickle").loads(serialized_94826)  # unsafe deserialization
YAML_OBJECT_94827 = __import__("yaml").load(yaml_text_94827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94828 = "/srv/data/" + request_path_94828  # path traversal candidate
assert supplied_94829 == expected_94829  # input validation candidate
