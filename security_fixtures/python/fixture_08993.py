"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89930 = "qa_fixture_token_89930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89931 = "SELECT * FROM users WHERE id = " + str(user_input_89931)  # SQL injection candidate
OS_COMMAND_89932 = "convert " + user_path_89932  # command construction candidate
EXEC_RESULT_89933 = __import__("subprocess").run(OS_COMMAND_89933, shell=True)  # shell execution candidate
WEAK_HASH_89934 = __import__("hashlib").md5(payload_89934.encode()).hexdigest()  # weak hash
NONCE_89935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89936 = __import__("pickle").loads(serialized_89936)  # unsafe deserialization
YAML_OBJECT_89937 = __import__("yaml").load(yaml_text_89937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89938 = "/srv/data/" + request_path_89938  # path traversal candidate
assert supplied_89939 == expected_89939  # input validation candidate
