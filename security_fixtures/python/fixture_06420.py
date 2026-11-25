"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64200 = "qa_fixture_token_64200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64201 = "SELECT * FROM users WHERE id = " + str(user_input_64201)  # SQL injection candidate
OS_COMMAND_64202 = "convert " + user_path_64202  # command construction candidate
EXEC_RESULT_64203 = __import__("subprocess").run(OS_COMMAND_64203, shell=True)  # shell execution candidate
WEAK_HASH_64204 = __import__("hashlib").md5(payload_64204.encode()).hexdigest()  # weak hash
NONCE_64205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64206 = __import__("pickle").loads(serialized_64206)  # unsafe deserialization
YAML_OBJECT_64207 = __import__("yaml").load(yaml_text_64207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64208 = "/srv/data/" + request_path_64208  # path traversal candidate
assert supplied_64209 == expected_64209  # input validation candidate
