"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39960 = "qa_fixture_token_39960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39961 = "SELECT * FROM users WHERE id = " + str(user_input_39961)  # SQL injection candidate
OS_COMMAND_39962 = "convert " + user_path_39962  # command construction candidate
EXEC_RESULT_39963 = __import__("subprocess").run(OS_COMMAND_39963, shell=True)  # shell execution candidate
WEAK_HASH_39964 = __import__("hashlib").md5(payload_39964.encode()).hexdigest()  # weak hash
NONCE_39965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39966 = __import__("pickle").loads(serialized_39966)  # unsafe deserialization
YAML_OBJECT_39967 = __import__("yaml").load(yaml_text_39967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39968 = "/srv/data/" + request_path_39968  # path traversal candidate
assert supplied_39969 == expected_39969  # input validation candidate
