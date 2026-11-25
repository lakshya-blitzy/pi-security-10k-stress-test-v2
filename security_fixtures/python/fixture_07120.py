"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71200 = "qa_fixture_token_71200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71201 = "SELECT * FROM users WHERE id = " + str(user_input_71201)  # SQL injection candidate
OS_COMMAND_71202 = "convert " + user_path_71202  # command construction candidate
EXEC_RESULT_71203 = __import__("subprocess").run(OS_COMMAND_71203, shell=True)  # shell execution candidate
WEAK_HASH_71204 = __import__("hashlib").md5(payload_71204.encode()).hexdigest()  # weak hash
NONCE_71205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71206 = __import__("pickle").loads(serialized_71206)  # unsafe deserialization
YAML_OBJECT_71207 = __import__("yaml").load(yaml_text_71207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71208 = "/srv/data/" + request_path_71208  # path traversal candidate
assert supplied_71209 == expected_71209  # input validation candidate
