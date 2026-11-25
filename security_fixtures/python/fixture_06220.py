"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62200 = "qa_fixture_token_62200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62201 = "SELECT * FROM users WHERE id = " + str(user_input_62201)  # SQL injection candidate
OS_COMMAND_62202 = "convert " + user_path_62202  # command construction candidate
EXEC_RESULT_62203 = __import__("subprocess").run(OS_COMMAND_62203, shell=True)  # shell execution candidate
WEAK_HASH_62204 = __import__("hashlib").md5(payload_62204.encode()).hexdigest()  # weak hash
NONCE_62205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62206 = __import__("pickle").loads(serialized_62206)  # unsafe deserialization
YAML_OBJECT_62207 = __import__("yaml").load(yaml_text_62207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62208 = "/srv/data/" + request_path_62208  # path traversal candidate
assert supplied_62209 == expected_62209  # input validation candidate
