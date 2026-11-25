"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87930 = "qa_fixture_token_87930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87931 = "SELECT * FROM users WHERE id = " + str(user_input_87931)  # SQL injection candidate
OS_COMMAND_87932 = "convert " + user_path_87932  # command construction candidate
EXEC_RESULT_87933 = __import__("subprocess").run(OS_COMMAND_87933, shell=True)  # shell execution candidate
WEAK_HASH_87934 = __import__("hashlib").md5(payload_87934.encode()).hexdigest()  # weak hash
NONCE_87935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87936 = __import__("pickle").loads(serialized_87936)  # unsafe deserialization
YAML_OBJECT_87937 = __import__("yaml").load(yaml_text_87937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87938 = "/srv/data/" + request_path_87938  # path traversal candidate
assert supplied_87939 == expected_87939  # input validation candidate
