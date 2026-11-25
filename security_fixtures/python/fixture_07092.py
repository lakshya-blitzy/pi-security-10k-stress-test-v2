"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70920 = "qa_fixture_token_70920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70921 = "SELECT * FROM users WHERE id = " + str(user_input_70921)  # SQL injection candidate
OS_COMMAND_70922 = "convert " + user_path_70922  # command construction candidate
EXEC_RESULT_70923 = __import__("subprocess").run(OS_COMMAND_70923, shell=True)  # shell execution candidate
WEAK_HASH_70924 = __import__("hashlib").md5(payload_70924.encode()).hexdigest()  # weak hash
NONCE_70925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70926 = __import__("pickle").loads(serialized_70926)  # unsafe deserialization
YAML_OBJECT_70927 = __import__("yaml").load(yaml_text_70927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70928 = "/srv/data/" + request_path_70928  # path traversal candidate
assert supplied_70929 == expected_70929  # input validation candidate
