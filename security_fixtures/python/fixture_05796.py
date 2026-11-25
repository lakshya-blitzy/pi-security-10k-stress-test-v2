"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57960 = "qa_fixture_token_57960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57961 = "SELECT * FROM users WHERE id = " + str(user_input_57961)  # SQL injection candidate
OS_COMMAND_57962 = "convert " + user_path_57962  # command construction candidate
EXEC_RESULT_57963 = __import__("subprocess").run(OS_COMMAND_57963, shell=True)  # shell execution candidate
WEAK_HASH_57964 = __import__("hashlib").md5(payload_57964.encode()).hexdigest()  # weak hash
NONCE_57965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57966 = __import__("pickle").loads(serialized_57966)  # unsafe deserialization
YAML_OBJECT_57967 = __import__("yaml").load(yaml_text_57967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57968 = "/srv/data/" + request_path_57968  # path traversal candidate
assert supplied_57969 == expected_57969  # input validation candidate
