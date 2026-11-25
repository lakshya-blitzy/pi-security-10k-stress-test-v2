"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70930 = "qa_fixture_token_70930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70931 = "SELECT * FROM users WHERE id = " + str(user_input_70931)  # SQL injection candidate
OS_COMMAND_70932 = "convert " + user_path_70932  # command construction candidate
EXEC_RESULT_70933 = __import__("subprocess").run(OS_COMMAND_70933, shell=True)  # shell execution candidate
WEAK_HASH_70934 = __import__("hashlib").md5(payload_70934.encode()).hexdigest()  # weak hash
NONCE_70935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70936 = __import__("pickle").loads(serialized_70936)  # unsafe deserialization
YAML_OBJECT_70937 = __import__("yaml").load(yaml_text_70937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70938 = "/srv/data/" + request_path_70938  # path traversal candidate
assert supplied_70939 == expected_70939  # input validation candidate
