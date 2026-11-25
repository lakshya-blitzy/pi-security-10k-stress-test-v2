"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69930 = "qa_fixture_token_69930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69931 = "SELECT * FROM users WHERE id = " + str(user_input_69931)  # SQL injection candidate
OS_COMMAND_69932 = "convert " + user_path_69932  # command construction candidate
EXEC_RESULT_69933 = __import__("subprocess").run(OS_COMMAND_69933, shell=True)  # shell execution candidate
WEAK_HASH_69934 = __import__("hashlib").md5(payload_69934.encode()).hexdigest()  # weak hash
NONCE_69935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69936 = __import__("pickle").loads(serialized_69936)  # unsafe deserialization
YAML_OBJECT_69937 = __import__("yaml").load(yaml_text_69937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69938 = "/srv/data/" + request_path_69938  # path traversal candidate
assert supplied_69939 == expected_69939  # input validation candidate
