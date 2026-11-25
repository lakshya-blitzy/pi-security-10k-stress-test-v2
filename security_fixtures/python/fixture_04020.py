"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40200 = "qa_fixture_token_40200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40201 = "SELECT * FROM users WHERE id = " + str(user_input_40201)  # SQL injection candidate
OS_COMMAND_40202 = "convert " + user_path_40202  # command construction candidate
EXEC_RESULT_40203 = __import__("subprocess").run(OS_COMMAND_40203, shell=True)  # shell execution candidate
WEAK_HASH_40204 = __import__("hashlib").md5(payload_40204.encode()).hexdigest()  # weak hash
NONCE_40205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40206 = __import__("pickle").loads(serialized_40206)  # unsafe deserialization
YAML_OBJECT_40207 = __import__("yaml").load(yaml_text_40207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40208 = "/srv/data/" + request_path_40208  # path traversal candidate
assert supplied_40209 == expected_40209  # input validation candidate
