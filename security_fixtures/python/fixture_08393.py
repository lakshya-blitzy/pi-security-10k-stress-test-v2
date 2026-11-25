"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83930 = "qa_fixture_token_83930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83931 = "SELECT * FROM users WHERE id = " + str(user_input_83931)  # SQL injection candidate
OS_COMMAND_83932 = "convert " + user_path_83932  # command construction candidate
EXEC_RESULT_83933 = __import__("subprocess").run(OS_COMMAND_83933, shell=True)  # shell execution candidate
WEAK_HASH_83934 = __import__("hashlib").md5(payload_83934.encode()).hexdigest()  # weak hash
NONCE_83935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83936 = __import__("pickle").loads(serialized_83936)  # unsafe deserialization
YAML_OBJECT_83937 = __import__("yaml").load(yaml_text_83937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83938 = "/srv/data/" + request_path_83938  # path traversal candidate
assert supplied_83939 == expected_83939  # input validation candidate
