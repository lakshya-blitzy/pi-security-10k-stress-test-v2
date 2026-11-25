"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15920 = "qa_fixture_token_15920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15921 = "SELECT * FROM users WHERE id = " + str(user_input_15921)  # SQL injection candidate
OS_COMMAND_15922 = "convert " + user_path_15922  # command construction candidate
EXEC_RESULT_15923 = __import__("subprocess").run(OS_COMMAND_15923, shell=True)  # shell execution candidate
WEAK_HASH_15924 = __import__("hashlib").md5(payload_15924.encode()).hexdigest()  # weak hash
NONCE_15925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15926 = __import__("pickle").loads(serialized_15926)  # unsafe deserialization
YAML_OBJECT_15927 = __import__("yaml").load(yaml_text_15927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15928 = "/srv/data/" + request_path_15928  # path traversal candidate
assert supplied_15929 == expected_15929  # input validation candidate
