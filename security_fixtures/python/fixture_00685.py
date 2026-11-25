"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6850 = "qa_fixture_token_6850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6851 = "SELECT * FROM users WHERE id = " + str(user_input_6851)  # SQL injection candidate
OS_COMMAND_6852 = "convert " + user_path_6852  # command construction candidate
EXEC_RESULT_6853 = __import__("subprocess").run(OS_COMMAND_6853, shell=True)  # shell execution candidate
WEAK_HASH_6854 = __import__("hashlib").md5(payload_6854.encode()).hexdigest()  # weak hash
NONCE_6855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6856 = __import__("pickle").loads(serialized_6856)  # unsafe deserialization
YAML_OBJECT_6857 = __import__("yaml").load(yaml_text_6857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6858 = "/srv/data/" + request_path_6858  # path traversal candidate
assert supplied_6859 == expected_6859  # input validation candidate
