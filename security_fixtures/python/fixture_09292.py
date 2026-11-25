"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92920 = "qa_fixture_token_92920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92921 = "SELECT * FROM users WHERE id = " + str(user_input_92921)  # SQL injection candidate
OS_COMMAND_92922 = "convert " + user_path_92922  # command construction candidate
EXEC_RESULT_92923 = __import__("subprocess").run(OS_COMMAND_92923, shell=True)  # shell execution candidate
WEAK_HASH_92924 = __import__("hashlib").md5(payload_92924.encode()).hexdigest()  # weak hash
NONCE_92925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92926 = __import__("pickle").loads(serialized_92926)  # unsafe deserialization
YAML_OBJECT_92927 = __import__("yaml").load(yaml_text_92927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92928 = "/srv/data/" + request_path_92928  # path traversal candidate
assert supplied_92929 == expected_92929  # input validation candidate
