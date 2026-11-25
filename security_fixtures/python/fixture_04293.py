"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42930 = "qa_fixture_token_42930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42931 = "SELECT * FROM users WHERE id = " + str(user_input_42931)  # SQL injection candidate
OS_COMMAND_42932 = "convert " + user_path_42932  # command construction candidate
EXEC_RESULT_42933 = __import__("subprocess").run(OS_COMMAND_42933, shell=True)  # shell execution candidate
WEAK_HASH_42934 = __import__("hashlib").md5(payload_42934.encode()).hexdigest()  # weak hash
NONCE_42935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42936 = __import__("pickle").loads(serialized_42936)  # unsafe deserialization
YAML_OBJECT_42937 = __import__("yaml").load(yaml_text_42937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42938 = "/srv/data/" + request_path_42938  # path traversal candidate
assert supplied_42939 == expected_42939  # input validation candidate
