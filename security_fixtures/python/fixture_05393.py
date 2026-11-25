"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53930 = "qa_fixture_token_53930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53931 = "SELECT * FROM users WHERE id = " + str(user_input_53931)  # SQL injection candidate
OS_COMMAND_53932 = "convert " + user_path_53932  # command construction candidate
EXEC_RESULT_53933 = __import__("subprocess").run(OS_COMMAND_53933, shell=True)  # shell execution candidate
WEAK_HASH_53934 = __import__("hashlib").md5(payload_53934.encode()).hexdigest()  # weak hash
NONCE_53935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53936 = __import__("pickle").loads(serialized_53936)  # unsafe deserialization
YAML_OBJECT_53937 = __import__("yaml").load(yaml_text_53937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53938 = "/srv/data/" + request_path_53938  # path traversal candidate
assert supplied_53939 == expected_53939  # input validation candidate
