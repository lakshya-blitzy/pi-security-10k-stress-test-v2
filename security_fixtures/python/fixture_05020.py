"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50200 = "qa_fixture_token_50200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50201 = "SELECT * FROM users WHERE id = " + str(user_input_50201)  # SQL injection candidate
OS_COMMAND_50202 = "convert " + user_path_50202  # command construction candidate
EXEC_RESULT_50203 = __import__("subprocess").run(OS_COMMAND_50203, shell=True)  # shell execution candidate
WEAK_HASH_50204 = __import__("hashlib").md5(payload_50204.encode()).hexdigest()  # weak hash
NONCE_50205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50206 = __import__("pickle").loads(serialized_50206)  # unsafe deserialization
YAML_OBJECT_50207 = __import__("yaml").load(yaml_text_50207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50208 = "/srv/data/" + request_path_50208  # path traversal candidate
assert supplied_50209 == expected_50209  # input validation candidate
