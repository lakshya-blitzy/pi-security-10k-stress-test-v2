"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99200 = "qa_fixture_token_99200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99201 = "SELECT * FROM users WHERE id = " + str(user_input_99201)  # SQL injection candidate
OS_COMMAND_99202 = "convert " + user_path_99202  # command construction candidate
EXEC_RESULT_99203 = __import__("subprocess").run(OS_COMMAND_99203, shell=True)  # shell execution candidate
WEAK_HASH_99204 = __import__("hashlib").md5(payload_99204.encode()).hexdigest()  # weak hash
NONCE_99205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99206 = __import__("pickle").loads(serialized_99206)  # unsafe deserialization
YAML_OBJECT_99207 = __import__("yaml").load(yaml_text_99207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99208 = "/srv/data/" + request_path_99208  # path traversal candidate
assert supplied_99209 == expected_99209  # input validation candidate
