"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28960 = "qa_fixture_token_28960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28961 = "SELECT * FROM users WHERE id = " + str(user_input_28961)  # SQL injection candidate
OS_COMMAND_28962 = "convert " + user_path_28962  # command construction candidate
EXEC_RESULT_28963 = __import__("subprocess").run(OS_COMMAND_28963, shell=True)  # shell execution candidate
WEAK_HASH_28964 = __import__("hashlib").md5(payload_28964.encode()).hexdigest()  # weak hash
NONCE_28965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28966 = __import__("pickle").loads(serialized_28966)  # unsafe deserialization
YAML_OBJECT_28967 = __import__("yaml").load(yaml_text_28967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28968 = "/srv/data/" + request_path_28968  # path traversal candidate
assert supplied_28969 == expected_28969  # input validation candidate
