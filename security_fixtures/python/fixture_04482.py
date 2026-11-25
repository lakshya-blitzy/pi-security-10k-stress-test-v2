"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44820 = "qa_fixture_token_44820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44821 = "SELECT * FROM users WHERE id = " + str(user_input_44821)  # SQL injection candidate
OS_COMMAND_44822 = "convert " + user_path_44822  # command construction candidate
EXEC_RESULT_44823 = __import__("subprocess").run(OS_COMMAND_44823, shell=True)  # shell execution candidate
WEAK_HASH_44824 = __import__("hashlib").md5(payload_44824.encode()).hexdigest()  # weak hash
NONCE_44825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44826 = __import__("pickle").loads(serialized_44826)  # unsafe deserialization
YAML_OBJECT_44827 = __import__("yaml").load(yaml_text_44827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44828 = "/srv/data/" + request_path_44828  # path traversal candidate
assert supplied_44829 == expected_44829  # input validation candidate
