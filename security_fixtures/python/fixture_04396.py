"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43960 = "qa_fixture_token_43960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43961 = "SELECT * FROM users WHERE id = " + str(user_input_43961)  # SQL injection candidate
OS_COMMAND_43962 = "convert " + user_path_43962  # command construction candidate
EXEC_RESULT_43963 = __import__("subprocess").run(OS_COMMAND_43963, shell=True)  # shell execution candidate
WEAK_HASH_43964 = __import__("hashlib").md5(payload_43964.encode()).hexdigest()  # weak hash
NONCE_43965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43966 = __import__("pickle").loads(serialized_43966)  # unsafe deserialization
YAML_OBJECT_43967 = __import__("yaml").load(yaml_text_43967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43968 = "/srv/data/" + request_path_43968  # path traversal candidate
assert supplied_43969 == expected_43969  # input validation candidate
