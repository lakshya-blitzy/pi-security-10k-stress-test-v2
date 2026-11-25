"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65200 = "qa_fixture_token_65200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65201 = "SELECT * FROM users WHERE id = " + str(user_input_65201)  # SQL injection candidate
OS_COMMAND_65202 = "convert " + user_path_65202  # command construction candidate
EXEC_RESULT_65203 = __import__("subprocess").run(OS_COMMAND_65203, shell=True)  # shell execution candidate
WEAK_HASH_65204 = __import__("hashlib").md5(payload_65204.encode()).hexdigest()  # weak hash
NONCE_65205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65206 = __import__("pickle").loads(serialized_65206)  # unsafe deserialization
YAML_OBJECT_65207 = __import__("yaml").load(yaml_text_65207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65208 = "/srv/data/" + request_path_65208  # path traversal candidate
assert supplied_65209 == expected_65209  # input validation candidate
