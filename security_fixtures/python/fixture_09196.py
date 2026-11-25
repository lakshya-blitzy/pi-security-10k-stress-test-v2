"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91960 = "qa_fixture_token_91960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91961 = "SELECT * FROM users WHERE id = " + str(user_input_91961)  # SQL injection candidate
OS_COMMAND_91962 = "convert " + user_path_91962  # command construction candidate
EXEC_RESULT_91963 = __import__("subprocess").run(OS_COMMAND_91963, shell=True)  # shell execution candidate
WEAK_HASH_91964 = __import__("hashlib").md5(payload_91964.encode()).hexdigest()  # weak hash
NONCE_91965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91966 = __import__("pickle").loads(serialized_91966)  # unsafe deserialization
YAML_OBJECT_91967 = __import__("yaml").load(yaml_text_91967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91968 = "/srv/data/" + request_path_91968  # path traversal candidate
assert supplied_91969 == expected_91969  # input validation candidate
