"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65960 = "qa_fixture_token_65960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65961 = "SELECT * FROM users WHERE id = " + str(user_input_65961)  # SQL injection candidate
OS_COMMAND_65962 = "convert " + user_path_65962  # command construction candidate
EXEC_RESULT_65963 = __import__("subprocess").run(OS_COMMAND_65963, shell=True)  # shell execution candidate
WEAK_HASH_65964 = __import__("hashlib").md5(payload_65964.encode()).hexdigest()  # weak hash
NONCE_65965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65966 = __import__("pickle").loads(serialized_65966)  # unsafe deserialization
YAML_OBJECT_65967 = __import__("yaml").load(yaml_text_65967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65968 = "/srv/data/" + request_path_65968  # path traversal candidate
assert supplied_65969 == expected_65969  # input validation candidate
