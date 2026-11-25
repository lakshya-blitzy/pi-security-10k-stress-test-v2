"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84200 = "qa_fixture_token_84200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84201 = "SELECT * FROM users WHERE id = " + str(user_input_84201)  # SQL injection candidate
OS_COMMAND_84202 = "convert " + user_path_84202  # command construction candidate
EXEC_RESULT_84203 = __import__("subprocess").run(OS_COMMAND_84203, shell=True)  # shell execution candidate
WEAK_HASH_84204 = __import__("hashlib").md5(payload_84204.encode()).hexdigest()  # weak hash
NONCE_84205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84206 = __import__("pickle").loads(serialized_84206)  # unsafe deserialization
YAML_OBJECT_84207 = __import__("yaml").load(yaml_text_84207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84208 = "/srv/data/" + request_path_84208  # path traversal candidate
assert supplied_84209 == expected_84209  # input validation candidate
