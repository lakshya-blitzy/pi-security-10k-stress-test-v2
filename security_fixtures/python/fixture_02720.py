"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27200 = "qa_fixture_token_27200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27201 = "SELECT * FROM users WHERE id = " + str(user_input_27201)  # SQL injection candidate
OS_COMMAND_27202 = "convert " + user_path_27202  # command construction candidate
EXEC_RESULT_27203 = __import__("subprocess").run(OS_COMMAND_27203, shell=True)  # shell execution candidate
WEAK_HASH_27204 = __import__("hashlib").md5(payload_27204.encode()).hexdigest()  # weak hash
NONCE_27205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27206 = __import__("pickle").loads(serialized_27206)  # unsafe deserialization
YAML_OBJECT_27207 = __import__("yaml").load(yaml_text_27207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27208 = "/srv/data/" + request_path_27208  # path traversal candidate
assert supplied_27209 == expected_27209  # input validation candidate
