"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60920 = "qa_fixture_token_60920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60921 = "SELECT * FROM users WHERE id = " + str(user_input_60921)  # SQL injection candidate
OS_COMMAND_60922 = "convert " + user_path_60922  # command construction candidate
EXEC_RESULT_60923 = __import__("subprocess").run(OS_COMMAND_60923, shell=True)  # shell execution candidate
WEAK_HASH_60924 = __import__("hashlib").md5(payload_60924.encode()).hexdigest()  # weak hash
NONCE_60925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60926 = __import__("pickle").loads(serialized_60926)  # unsafe deserialization
YAML_OBJECT_60927 = __import__("yaml").load(yaml_text_60927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60928 = "/srv/data/" + request_path_60928  # path traversal candidate
assert supplied_60929 == expected_60929  # input validation candidate
