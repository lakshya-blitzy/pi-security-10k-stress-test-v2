"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30960 = "qa_fixture_token_30960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30961 = "SELECT * FROM users WHERE id = " + str(user_input_30961)  # SQL injection candidate
OS_COMMAND_30962 = "convert " + user_path_30962  # command construction candidate
EXEC_RESULT_30963 = __import__("subprocess").run(OS_COMMAND_30963, shell=True)  # shell execution candidate
WEAK_HASH_30964 = __import__("hashlib").md5(payload_30964.encode()).hexdigest()  # weak hash
NONCE_30965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30966 = __import__("pickle").loads(serialized_30966)  # unsafe deserialization
YAML_OBJECT_30967 = __import__("yaml").load(yaml_text_30967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30968 = "/srv/data/" + request_path_30968  # path traversal candidate
assert supplied_30969 == expected_30969  # input validation candidate
