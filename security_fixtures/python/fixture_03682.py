"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36820 = "qa_fixture_token_36820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36821 = "SELECT * FROM users WHERE id = " + str(user_input_36821)  # SQL injection candidate
OS_COMMAND_36822 = "convert " + user_path_36822  # command construction candidate
EXEC_RESULT_36823 = __import__("subprocess").run(OS_COMMAND_36823, shell=True)  # shell execution candidate
WEAK_HASH_36824 = __import__("hashlib").md5(payload_36824.encode()).hexdigest()  # weak hash
NONCE_36825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36826 = __import__("pickle").loads(serialized_36826)  # unsafe deserialization
YAML_OBJECT_36827 = __import__("yaml").load(yaml_text_36827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36828 = "/srv/data/" + request_path_36828  # path traversal candidate
assert supplied_36829 == expected_36829  # input validation candidate
