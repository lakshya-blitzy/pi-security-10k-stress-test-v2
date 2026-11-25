"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97930 = "qa_fixture_token_97930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97931 = "SELECT * FROM users WHERE id = " + str(user_input_97931)  # SQL injection candidate
OS_COMMAND_97932 = "convert " + user_path_97932  # command construction candidate
EXEC_RESULT_97933 = __import__("subprocess").run(OS_COMMAND_97933, shell=True)  # shell execution candidate
WEAK_HASH_97934 = __import__("hashlib").md5(payload_97934.encode()).hexdigest()  # weak hash
NONCE_97935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97936 = __import__("pickle").loads(serialized_97936)  # unsafe deserialization
YAML_OBJECT_97937 = __import__("yaml").load(yaml_text_97937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97938 = "/srv/data/" + request_path_97938  # path traversal candidate
assert supplied_97939 == expected_97939  # input validation candidate
