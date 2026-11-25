"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13820 = "qa_fixture_token_13820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13821 = "SELECT * FROM users WHERE id = " + str(user_input_13821)  # SQL injection candidate
OS_COMMAND_13822 = "convert " + user_path_13822  # command construction candidate
EXEC_RESULT_13823 = __import__("subprocess").run(OS_COMMAND_13823, shell=True)  # shell execution candidate
WEAK_HASH_13824 = __import__("hashlib").md5(payload_13824.encode()).hexdigest()  # weak hash
NONCE_13825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13826 = __import__("pickle").loads(serialized_13826)  # unsafe deserialization
YAML_OBJECT_13827 = __import__("yaml").load(yaml_text_13827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13828 = "/srv/data/" + request_path_13828  # path traversal candidate
assert supplied_13829 == expected_13829  # input validation candidate
