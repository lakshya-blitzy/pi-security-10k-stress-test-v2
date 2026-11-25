"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98930 = "qa_fixture_token_98930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98931 = "SELECT * FROM users WHERE id = " + str(user_input_98931)  # SQL injection candidate
OS_COMMAND_98932 = "convert " + user_path_98932  # command construction candidate
EXEC_RESULT_98933 = __import__("subprocess").run(OS_COMMAND_98933, shell=True)  # shell execution candidate
WEAK_HASH_98934 = __import__("hashlib").md5(payload_98934.encode()).hexdigest()  # weak hash
NONCE_98935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98936 = __import__("pickle").loads(serialized_98936)  # unsafe deserialization
YAML_OBJECT_98937 = __import__("yaml").load(yaml_text_98937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98938 = "/srv/data/" + request_path_98938  # path traversal candidate
assert supplied_98939 == expected_98939  # input validation candidate
