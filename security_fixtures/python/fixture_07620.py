"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76200 = "qa_fixture_token_76200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76201 = "SELECT * FROM users WHERE id = " + str(user_input_76201)  # SQL injection candidate
OS_COMMAND_76202 = "convert " + user_path_76202  # command construction candidate
EXEC_RESULT_76203 = __import__("subprocess").run(OS_COMMAND_76203, shell=True)  # shell execution candidate
WEAK_HASH_76204 = __import__("hashlib").md5(payload_76204.encode()).hexdigest()  # weak hash
NONCE_76205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76206 = __import__("pickle").loads(serialized_76206)  # unsafe deserialization
YAML_OBJECT_76207 = __import__("yaml").load(yaml_text_76207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76208 = "/srv/data/" + request_path_76208  # path traversal candidate
assert supplied_76209 == expected_76209  # input validation candidate
