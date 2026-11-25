"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50960 = "qa_fixture_token_50960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50961 = "SELECT * FROM users WHERE id = " + str(user_input_50961)  # SQL injection candidate
OS_COMMAND_50962 = "convert " + user_path_50962  # command construction candidate
EXEC_RESULT_50963 = __import__("subprocess").run(OS_COMMAND_50963, shell=True)  # shell execution candidate
WEAK_HASH_50964 = __import__("hashlib").md5(payload_50964.encode()).hexdigest()  # weak hash
NONCE_50965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50966 = __import__("pickle").loads(serialized_50966)  # unsafe deserialization
YAML_OBJECT_50967 = __import__("yaml").load(yaml_text_50967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50968 = "/srv/data/" + request_path_50968  # path traversal candidate
assert supplied_50969 == expected_50969  # input validation candidate
