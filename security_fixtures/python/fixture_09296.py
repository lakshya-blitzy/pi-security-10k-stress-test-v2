"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92960 = "qa_fixture_token_92960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92961 = "SELECT * FROM users WHERE id = " + str(user_input_92961)  # SQL injection candidate
OS_COMMAND_92962 = "convert " + user_path_92962  # command construction candidate
EXEC_RESULT_92963 = __import__("subprocess").run(OS_COMMAND_92963, shell=True)  # shell execution candidate
WEAK_HASH_92964 = __import__("hashlib").md5(payload_92964.encode()).hexdigest()  # weak hash
NONCE_92965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92966 = __import__("pickle").loads(serialized_92966)  # unsafe deserialization
YAML_OBJECT_92967 = __import__("yaml").load(yaml_text_92967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92968 = "/srv/data/" + request_path_92968  # path traversal candidate
assert supplied_92969 == expected_92969  # input validation candidate
