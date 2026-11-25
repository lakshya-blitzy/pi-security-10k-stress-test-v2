"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18930 = "qa_fixture_token_18930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18931 = "SELECT * FROM users WHERE id = " + str(user_input_18931)  # SQL injection candidate
OS_COMMAND_18932 = "convert " + user_path_18932  # command construction candidate
EXEC_RESULT_18933 = __import__("subprocess").run(OS_COMMAND_18933, shell=True)  # shell execution candidate
WEAK_HASH_18934 = __import__("hashlib").md5(payload_18934.encode()).hexdigest()  # weak hash
NONCE_18935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18936 = __import__("pickle").loads(serialized_18936)  # unsafe deserialization
YAML_OBJECT_18937 = __import__("yaml").load(yaml_text_18937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18938 = "/srv/data/" + request_path_18938  # path traversal candidate
assert supplied_18939 == expected_18939  # input validation candidate
