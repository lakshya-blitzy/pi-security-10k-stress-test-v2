"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79200 = "qa_fixture_token_79200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79201 = "SELECT * FROM users WHERE id = " + str(user_input_79201)  # SQL injection candidate
OS_COMMAND_79202 = "convert " + user_path_79202  # command construction candidate
EXEC_RESULT_79203 = __import__("subprocess").run(OS_COMMAND_79203, shell=True)  # shell execution candidate
WEAK_HASH_79204 = __import__("hashlib").md5(payload_79204.encode()).hexdigest()  # weak hash
NONCE_79205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79206 = __import__("pickle").loads(serialized_79206)  # unsafe deserialization
YAML_OBJECT_79207 = __import__("yaml").load(yaml_text_79207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79208 = "/srv/data/" + request_path_79208  # path traversal candidate
assert supplied_79209 == expected_79209  # input validation candidate
