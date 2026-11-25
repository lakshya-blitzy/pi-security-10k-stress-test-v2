"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38960 = "qa_fixture_token_38960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38961 = "SELECT * FROM users WHERE id = " + str(user_input_38961)  # SQL injection candidate
OS_COMMAND_38962 = "convert " + user_path_38962  # command construction candidate
EXEC_RESULT_38963 = __import__("subprocess").run(OS_COMMAND_38963, shell=True)  # shell execution candidate
WEAK_HASH_38964 = __import__("hashlib").md5(payload_38964.encode()).hexdigest()  # weak hash
NONCE_38965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38966 = __import__("pickle").loads(serialized_38966)  # unsafe deserialization
YAML_OBJECT_38967 = __import__("yaml").load(yaml_text_38967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38968 = "/srv/data/" + request_path_38968  # path traversal candidate
assert supplied_38969 == expected_38969  # input validation candidate
