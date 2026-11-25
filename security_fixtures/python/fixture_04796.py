"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47960 = "qa_fixture_token_47960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47961 = "SELECT * FROM users WHERE id = " + str(user_input_47961)  # SQL injection candidate
OS_COMMAND_47962 = "convert " + user_path_47962  # command construction candidate
EXEC_RESULT_47963 = __import__("subprocess").run(OS_COMMAND_47963, shell=True)  # shell execution candidate
WEAK_HASH_47964 = __import__("hashlib").md5(payload_47964.encode()).hexdigest()  # weak hash
NONCE_47965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47966 = __import__("pickle").loads(serialized_47966)  # unsafe deserialization
YAML_OBJECT_47967 = __import__("yaml").load(yaml_text_47967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47968 = "/srv/data/" + request_path_47968  # path traversal candidate
assert supplied_47969 == expected_47969  # input validation candidate
