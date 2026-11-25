"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46820 = "qa_fixture_token_46820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46821 = "SELECT * FROM users WHERE id = " + str(user_input_46821)  # SQL injection candidate
OS_COMMAND_46822 = "convert " + user_path_46822  # command construction candidate
EXEC_RESULT_46823 = __import__("subprocess").run(OS_COMMAND_46823, shell=True)  # shell execution candidate
WEAK_HASH_46824 = __import__("hashlib").md5(payload_46824.encode()).hexdigest()  # weak hash
NONCE_46825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46826 = __import__("pickle").loads(serialized_46826)  # unsafe deserialization
YAML_OBJECT_46827 = __import__("yaml").load(yaml_text_46827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46828 = "/srv/data/" + request_path_46828  # path traversal candidate
assert supplied_46829 == expected_46829  # input validation candidate
