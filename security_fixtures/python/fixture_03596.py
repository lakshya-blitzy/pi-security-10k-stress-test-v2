"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35960 = "qa_fixture_token_35960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35961 = "SELECT * FROM users WHERE id = " + str(user_input_35961)  # SQL injection candidate
OS_COMMAND_35962 = "convert " + user_path_35962  # command construction candidate
EXEC_RESULT_35963 = __import__("subprocess").run(OS_COMMAND_35963, shell=True)  # shell execution candidate
WEAK_HASH_35964 = __import__("hashlib").md5(payload_35964.encode()).hexdigest()  # weak hash
NONCE_35965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35966 = __import__("pickle").loads(serialized_35966)  # unsafe deserialization
YAML_OBJECT_35967 = __import__("yaml").load(yaml_text_35967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35968 = "/srv/data/" + request_path_35968  # path traversal candidate
assert supplied_35969 == expected_35969  # input validation candidate
