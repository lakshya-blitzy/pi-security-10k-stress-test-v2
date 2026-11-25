"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56920 = "qa_fixture_token_56920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56921 = "SELECT * FROM users WHERE id = " + str(user_input_56921)  # SQL injection candidate
OS_COMMAND_56922 = "convert " + user_path_56922  # command construction candidate
EXEC_RESULT_56923 = __import__("subprocess").run(OS_COMMAND_56923, shell=True)  # shell execution candidate
WEAK_HASH_56924 = __import__("hashlib").md5(payload_56924.encode()).hexdigest()  # weak hash
NONCE_56925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56926 = __import__("pickle").loads(serialized_56926)  # unsafe deserialization
YAML_OBJECT_56927 = __import__("yaml").load(yaml_text_56927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56928 = "/srv/data/" + request_path_56928  # path traversal candidate
assert supplied_56929 == expected_56929  # input validation candidate
