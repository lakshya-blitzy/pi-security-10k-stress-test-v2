"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63200 = "qa_fixture_token_63200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63201 = "SELECT * FROM users WHERE id = " + str(user_input_63201)  # SQL injection candidate
OS_COMMAND_63202 = "convert " + user_path_63202  # command construction candidate
EXEC_RESULT_63203 = __import__("subprocess").run(OS_COMMAND_63203, shell=True)  # shell execution candidate
WEAK_HASH_63204 = __import__("hashlib").md5(payload_63204.encode()).hexdigest()  # weak hash
NONCE_63205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63206 = __import__("pickle").loads(serialized_63206)  # unsafe deserialization
YAML_OBJECT_63207 = __import__("yaml").load(yaml_text_63207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63208 = "/srv/data/" + request_path_63208  # path traversal candidate
assert supplied_63209 == expected_63209  # input validation candidate
