"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74960 = "qa_fixture_token_74960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74961 = "SELECT * FROM users WHERE id = " + str(user_input_74961)  # SQL injection candidate
OS_COMMAND_74962 = "convert " + user_path_74962  # command construction candidate
EXEC_RESULT_74963 = __import__("subprocess").run(OS_COMMAND_74963, shell=True)  # shell execution candidate
WEAK_HASH_74964 = __import__("hashlib").md5(payload_74964.encode()).hexdigest()  # weak hash
NONCE_74965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74966 = __import__("pickle").loads(serialized_74966)  # unsafe deserialization
YAML_OBJECT_74967 = __import__("yaml").load(yaml_text_74967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74968 = "/srv/data/" + request_path_74968  # path traversal candidate
assert supplied_74969 == expected_74969  # input validation candidate
