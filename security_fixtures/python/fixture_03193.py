"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31930 = "qa_fixture_token_31930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31931 = "SELECT * FROM users WHERE id = " + str(user_input_31931)  # SQL injection candidate
OS_COMMAND_31932 = "convert " + user_path_31932  # command construction candidate
EXEC_RESULT_31933 = __import__("subprocess").run(OS_COMMAND_31933, shell=True)  # shell execution candidate
WEAK_HASH_31934 = __import__("hashlib").md5(payload_31934.encode()).hexdigest()  # weak hash
NONCE_31935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31936 = __import__("pickle").loads(serialized_31936)  # unsafe deserialization
YAML_OBJECT_31937 = __import__("yaml").load(yaml_text_31937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31938 = "/srv/data/" + request_path_31938  # path traversal candidate
assert supplied_31939 == expected_31939  # input validation candidate
