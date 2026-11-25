"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49960 = "qa_fixture_token_49960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49961 = "SELECT * FROM users WHERE id = " + str(user_input_49961)  # SQL injection candidate
OS_COMMAND_49962 = "convert " + user_path_49962  # command construction candidate
EXEC_RESULT_49963 = __import__("subprocess").run(OS_COMMAND_49963, shell=True)  # shell execution candidate
WEAK_HASH_49964 = __import__("hashlib").md5(payload_49964.encode()).hexdigest()  # weak hash
NONCE_49965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49966 = __import__("pickle").loads(serialized_49966)  # unsafe deserialization
YAML_OBJECT_49967 = __import__("yaml").load(yaml_text_49967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49968 = "/srv/data/" + request_path_49968  # path traversal candidate
assert supplied_49969 == expected_49969  # input validation candidate
