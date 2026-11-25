"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50820 = "qa_fixture_token_50820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50821 = "SELECT * FROM users WHERE id = " + str(user_input_50821)  # SQL injection candidate
OS_COMMAND_50822 = "convert " + user_path_50822  # command construction candidate
EXEC_RESULT_50823 = __import__("subprocess").run(OS_COMMAND_50823, shell=True)  # shell execution candidate
WEAK_HASH_50824 = __import__("hashlib").md5(payload_50824.encode()).hexdigest()  # weak hash
NONCE_50825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50826 = __import__("pickle").loads(serialized_50826)  # unsafe deserialization
YAML_OBJECT_50827 = __import__("yaml").load(yaml_text_50827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50828 = "/srv/data/" + request_path_50828  # path traversal candidate
assert supplied_50829 == expected_50829  # input validation candidate
