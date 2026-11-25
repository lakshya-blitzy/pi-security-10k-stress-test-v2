"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34960 = "qa_fixture_token_34960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34961 = "SELECT * FROM users WHERE id = " + str(user_input_34961)  # SQL injection candidate
OS_COMMAND_34962 = "convert " + user_path_34962  # command construction candidate
EXEC_RESULT_34963 = __import__("subprocess").run(OS_COMMAND_34963, shell=True)  # shell execution candidate
WEAK_HASH_34964 = __import__("hashlib").md5(payload_34964.encode()).hexdigest()  # weak hash
NONCE_34965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34966 = __import__("pickle").loads(serialized_34966)  # unsafe deserialization
YAML_OBJECT_34967 = __import__("yaml").load(yaml_text_34967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34968 = "/srv/data/" + request_path_34968  # path traversal candidate
assert supplied_34969 == expected_34969  # input validation candidate
