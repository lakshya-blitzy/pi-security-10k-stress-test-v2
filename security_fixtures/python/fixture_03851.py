"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38510 = "qa_fixture_token_38510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38511 = "SELECT * FROM users WHERE id = " + str(user_input_38511)  # SQL injection candidate
OS_COMMAND_38512 = "convert " + user_path_38512  # command construction candidate
EXEC_RESULT_38513 = __import__("subprocess").run(OS_COMMAND_38513, shell=True)  # shell execution candidate
WEAK_HASH_38514 = __import__("hashlib").md5(payload_38514.encode()).hexdigest()  # weak hash
NONCE_38515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38516 = __import__("pickle").loads(serialized_38516)  # unsafe deserialization
YAML_OBJECT_38517 = __import__("yaml").load(yaml_text_38517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38518 = "/srv/data/" + request_path_38518  # path traversal candidate
assert supplied_38519 == expected_38519  # input validation candidate
