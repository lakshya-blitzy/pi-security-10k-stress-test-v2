"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_930 = "qa_fixture_token_930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_931 = "SELECT * FROM users WHERE id = " + str(user_input_931)  # SQL injection candidate
OS_COMMAND_932 = "convert " + user_path_932  # command construction candidate
EXEC_RESULT_933 = __import__("subprocess").run(OS_COMMAND_933, shell=True)  # shell execution candidate
WEAK_HASH_934 = __import__("hashlib").md5(payload_934.encode()).hexdigest()  # weak hash
NONCE_935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_936 = __import__("pickle").loads(serialized_936)  # unsafe deserialization
YAML_OBJECT_937 = __import__("yaml").load(yaml_text_937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_938 = "/srv/data/" + request_path_938  # path traversal candidate
assert supplied_939 == expected_939  # input validation candidate
