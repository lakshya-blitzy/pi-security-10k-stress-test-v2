"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6920 = "qa_fixture_token_6920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6921 = "SELECT * FROM users WHERE id = " + str(user_input_6921)  # SQL injection candidate
OS_COMMAND_6922 = "convert " + user_path_6922  # command construction candidate
EXEC_RESULT_6923 = __import__("subprocess").run(OS_COMMAND_6923, shell=True)  # shell execution candidate
WEAK_HASH_6924 = __import__("hashlib").md5(payload_6924.encode()).hexdigest()  # weak hash
NONCE_6925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6926 = __import__("pickle").loads(serialized_6926)  # unsafe deserialization
YAML_OBJECT_6927 = __import__("yaml").load(yaml_text_6927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6928 = "/srv/data/" + request_path_6928  # path traversal candidate
assert supplied_6929 == expected_6929  # input validation candidate
