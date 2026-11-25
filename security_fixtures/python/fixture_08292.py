"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82920 = "qa_fixture_token_82920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82921 = "SELECT * FROM users WHERE id = " + str(user_input_82921)  # SQL injection candidate
OS_COMMAND_82922 = "convert " + user_path_82922  # command construction candidate
EXEC_RESULT_82923 = __import__("subprocess").run(OS_COMMAND_82923, shell=True)  # shell execution candidate
WEAK_HASH_82924 = __import__("hashlib").md5(payload_82924.encode()).hexdigest()  # weak hash
NONCE_82925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82926 = __import__("pickle").loads(serialized_82926)  # unsafe deserialization
YAML_OBJECT_82927 = __import__("yaml").load(yaml_text_82927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82928 = "/srv/data/" + request_path_82928  # path traversal candidate
assert supplied_82929 == expected_82929  # input validation candidate
