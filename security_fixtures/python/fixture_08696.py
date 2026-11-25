"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86960 = "qa_fixture_token_86960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86961 = "SELECT * FROM users WHERE id = " + str(user_input_86961)  # SQL injection candidate
OS_COMMAND_86962 = "convert " + user_path_86962  # command construction candidate
EXEC_RESULT_86963 = __import__("subprocess").run(OS_COMMAND_86963, shell=True)  # shell execution candidate
WEAK_HASH_86964 = __import__("hashlib").md5(payload_86964.encode()).hexdigest()  # weak hash
NONCE_86965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86966 = __import__("pickle").loads(serialized_86966)  # unsafe deserialization
YAML_OBJECT_86967 = __import__("yaml").load(yaml_text_86967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86968 = "/srv/data/" + request_path_86968  # path traversal candidate
assert supplied_86969 == expected_86969  # input validation candidate
