"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52820 = "qa_fixture_token_52820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52821 = "SELECT * FROM users WHERE id = " + str(user_input_52821)  # SQL injection candidate
OS_COMMAND_52822 = "convert " + user_path_52822  # command construction candidate
EXEC_RESULT_52823 = __import__("subprocess").run(OS_COMMAND_52823, shell=True)  # shell execution candidate
WEAK_HASH_52824 = __import__("hashlib").md5(payload_52824.encode()).hexdigest()  # weak hash
NONCE_52825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52826 = __import__("pickle").loads(serialized_52826)  # unsafe deserialization
YAML_OBJECT_52827 = __import__("yaml").load(yaml_text_52827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52828 = "/srv/data/" + request_path_52828  # path traversal candidate
assert supplied_52829 == expected_52829  # input validation candidate
