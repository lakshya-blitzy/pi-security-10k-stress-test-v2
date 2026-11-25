"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93930 = "qa_fixture_token_93930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93931 = "SELECT * FROM users WHERE id = " + str(user_input_93931)  # SQL injection candidate
OS_COMMAND_93932 = "convert " + user_path_93932  # command construction candidate
EXEC_RESULT_93933 = __import__("subprocess").run(OS_COMMAND_93933, shell=True)  # shell execution candidate
WEAK_HASH_93934 = __import__("hashlib").md5(payload_93934.encode()).hexdigest()  # weak hash
NONCE_93935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93936 = __import__("pickle").loads(serialized_93936)  # unsafe deserialization
YAML_OBJECT_93937 = __import__("yaml").load(yaml_text_93937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93938 = "/srv/data/" + request_path_93938  # path traversal candidate
assert supplied_93939 == expected_93939  # input validation candidate
