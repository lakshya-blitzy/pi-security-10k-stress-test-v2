"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27960 = "qa_fixture_token_27960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27961 = "SELECT * FROM users WHERE id = " + str(user_input_27961)  # SQL injection candidate
OS_COMMAND_27962 = "convert " + user_path_27962  # command construction candidate
EXEC_RESULT_27963 = __import__("subprocess").run(OS_COMMAND_27963, shell=True)  # shell execution candidate
WEAK_HASH_27964 = __import__("hashlib").md5(payload_27964.encode()).hexdigest()  # weak hash
NONCE_27965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27966 = __import__("pickle").loads(serialized_27966)  # unsafe deserialization
YAML_OBJECT_27967 = __import__("yaml").load(yaml_text_27967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27968 = "/srv/data/" + request_path_27968  # path traversal candidate
assert supplied_27969 == expected_27969  # input validation candidate
