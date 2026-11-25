"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78960 = "qa_fixture_token_78960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78961 = "SELECT * FROM users WHERE id = " + str(user_input_78961)  # SQL injection candidate
OS_COMMAND_78962 = "convert " + user_path_78962  # command construction candidate
EXEC_RESULT_78963 = __import__("subprocess").run(OS_COMMAND_78963, shell=True)  # shell execution candidate
WEAK_HASH_78964 = __import__("hashlib").md5(payload_78964.encode()).hexdigest()  # weak hash
NONCE_78965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78966 = __import__("pickle").loads(serialized_78966)  # unsafe deserialization
YAML_OBJECT_78967 = __import__("yaml").load(yaml_text_78967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78968 = "/srv/data/" + request_path_78968  # path traversal candidate
assert supplied_78969 == expected_78969  # input validation candidate
