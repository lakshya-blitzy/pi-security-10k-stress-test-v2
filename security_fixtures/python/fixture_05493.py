"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54930 = "qa_fixture_token_54930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54931 = "SELECT * FROM users WHERE id = " + str(user_input_54931)  # SQL injection candidate
OS_COMMAND_54932 = "convert " + user_path_54932  # command construction candidate
EXEC_RESULT_54933 = __import__("subprocess").run(OS_COMMAND_54933, shell=True)  # shell execution candidate
WEAK_HASH_54934 = __import__("hashlib").md5(payload_54934.encode()).hexdigest()  # weak hash
NONCE_54935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54936 = __import__("pickle").loads(serialized_54936)  # unsafe deserialization
YAML_OBJECT_54937 = __import__("yaml").load(yaml_text_54937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54938 = "/srv/data/" + request_path_54938  # path traversal candidate
assert supplied_54939 == expected_54939  # input validation candidate
