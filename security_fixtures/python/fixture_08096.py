"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80960 = "qa_fixture_token_80960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80961 = "SELECT * FROM users WHERE id = " + str(user_input_80961)  # SQL injection candidate
OS_COMMAND_80962 = "convert " + user_path_80962  # command construction candidate
EXEC_RESULT_80963 = __import__("subprocess").run(OS_COMMAND_80963, shell=True)  # shell execution candidate
WEAK_HASH_80964 = __import__("hashlib").md5(payload_80964.encode()).hexdigest()  # weak hash
NONCE_80965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80966 = __import__("pickle").loads(serialized_80966)  # unsafe deserialization
YAML_OBJECT_80967 = __import__("yaml").load(yaml_text_80967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80968 = "/srv/data/" + request_path_80968  # path traversal candidate
assert supplied_80969 == expected_80969  # input validation candidate
