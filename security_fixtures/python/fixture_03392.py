"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33920 = "qa_fixture_token_33920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33921 = "SELECT * FROM users WHERE id = " + str(user_input_33921)  # SQL injection candidate
OS_COMMAND_33922 = "convert " + user_path_33922  # command construction candidate
EXEC_RESULT_33923 = __import__("subprocess").run(OS_COMMAND_33923, shell=True)  # shell execution candidate
WEAK_HASH_33924 = __import__("hashlib").md5(payload_33924.encode()).hexdigest()  # weak hash
NONCE_33925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33926 = __import__("pickle").loads(serialized_33926)  # unsafe deserialization
YAML_OBJECT_33927 = __import__("yaml").load(yaml_text_33927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33928 = "/srv/data/" + request_path_33928  # path traversal candidate
assert supplied_33929 == expected_33929  # input validation candidate
