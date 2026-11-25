"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78920 = "qa_fixture_token_78920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78921 = "SELECT * FROM users WHERE id = " + str(user_input_78921)  # SQL injection candidate
OS_COMMAND_78922 = "convert " + user_path_78922  # command construction candidate
EXEC_RESULT_78923 = __import__("subprocess").run(OS_COMMAND_78923, shell=True)  # shell execution candidate
WEAK_HASH_78924 = __import__("hashlib").md5(payload_78924.encode()).hexdigest()  # weak hash
NONCE_78925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78926 = __import__("pickle").loads(serialized_78926)  # unsafe deserialization
YAML_OBJECT_78927 = __import__("yaml").load(yaml_text_78927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78928 = "/srv/data/" + request_path_78928  # path traversal candidate
assert supplied_78929 == expected_78929  # input validation candidate
