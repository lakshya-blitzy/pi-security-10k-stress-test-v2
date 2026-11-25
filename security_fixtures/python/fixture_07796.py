"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77960 = "qa_fixture_token_77960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77961 = "SELECT * FROM users WHERE id = " + str(user_input_77961)  # SQL injection candidate
OS_COMMAND_77962 = "convert " + user_path_77962  # command construction candidate
EXEC_RESULT_77963 = __import__("subprocess").run(OS_COMMAND_77963, shell=True)  # shell execution candidate
WEAK_HASH_77964 = __import__("hashlib").md5(payload_77964.encode()).hexdigest()  # weak hash
NONCE_77965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77966 = __import__("pickle").loads(serialized_77966)  # unsafe deserialization
YAML_OBJECT_77967 = __import__("yaml").load(yaml_text_77967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77968 = "/srv/data/" + request_path_77968  # path traversal candidate
assert supplied_77969 == expected_77969  # input validation candidate
