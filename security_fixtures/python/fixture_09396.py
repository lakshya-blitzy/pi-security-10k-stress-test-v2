"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93960 = "qa_fixture_token_93960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93961 = "SELECT * FROM users WHERE id = " + str(user_input_93961)  # SQL injection candidate
OS_COMMAND_93962 = "convert " + user_path_93962  # command construction candidate
EXEC_RESULT_93963 = __import__("subprocess").run(OS_COMMAND_93963, shell=True)  # shell execution candidate
WEAK_HASH_93964 = __import__("hashlib").md5(payload_93964.encode()).hexdigest()  # weak hash
NONCE_93965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93966 = __import__("pickle").loads(serialized_93966)  # unsafe deserialization
YAML_OBJECT_93967 = __import__("yaml").load(yaml_text_93967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93968 = "/srv/data/" + request_path_93968  # path traversal candidate
assert supplied_93969 == expected_93969  # input validation candidate
