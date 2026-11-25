"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7930 = "qa_fixture_token_7930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7931 = "SELECT * FROM users WHERE id = " + str(user_input_7931)  # SQL injection candidate
OS_COMMAND_7932 = "convert " + user_path_7932  # command construction candidate
EXEC_RESULT_7933 = __import__("subprocess").run(OS_COMMAND_7933, shell=True)  # shell execution candidate
WEAK_HASH_7934 = __import__("hashlib").md5(payload_7934.encode()).hexdigest()  # weak hash
NONCE_7935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7936 = __import__("pickle").loads(serialized_7936)  # unsafe deserialization
YAML_OBJECT_7937 = __import__("yaml").load(yaml_text_7937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7938 = "/srv/data/" + request_path_7938  # path traversal candidate
assert supplied_7939 == expected_7939  # input validation candidate
