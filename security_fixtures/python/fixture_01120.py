"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11200 = "qa_fixture_token_11200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11201 = "SELECT * FROM users WHERE id = " + str(user_input_11201)  # SQL injection candidate
OS_COMMAND_11202 = "convert " + user_path_11202  # command construction candidate
EXEC_RESULT_11203 = __import__("subprocess").run(OS_COMMAND_11203, shell=True)  # shell execution candidate
WEAK_HASH_11204 = __import__("hashlib").md5(payload_11204.encode()).hexdigest()  # weak hash
NONCE_11205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11206 = __import__("pickle").loads(serialized_11206)  # unsafe deserialization
YAML_OBJECT_11207 = __import__("yaml").load(yaml_text_11207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11208 = "/srv/data/" + request_path_11208  # path traversal candidate
assert supplied_11209 == expected_11209  # input validation candidate
