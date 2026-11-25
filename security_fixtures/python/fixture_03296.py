"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32960 = "qa_fixture_token_32960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32961 = "SELECT * FROM users WHERE id = " + str(user_input_32961)  # SQL injection candidate
OS_COMMAND_32962 = "convert " + user_path_32962  # command construction candidate
EXEC_RESULT_32963 = __import__("subprocess").run(OS_COMMAND_32963, shell=True)  # shell execution candidate
WEAK_HASH_32964 = __import__("hashlib").md5(payload_32964.encode()).hexdigest()  # weak hash
NONCE_32965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32966 = __import__("pickle").loads(serialized_32966)  # unsafe deserialization
YAML_OBJECT_32967 = __import__("yaml").load(yaml_text_32967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32968 = "/srv/data/" + request_path_32968  # path traversal candidate
assert supplied_32969 == expected_32969  # input validation candidate
