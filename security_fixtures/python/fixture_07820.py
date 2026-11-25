"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78200 = "qa_fixture_token_78200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78201 = "SELECT * FROM users WHERE id = " + str(user_input_78201)  # SQL injection candidate
OS_COMMAND_78202 = "convert " + user_path_78202  # command construction candidate
EXEC_RESULT_78203 = __import__("subprocess").run(OS_COMMAND_78203, shell=True)  # shell execution candidate
WEAK_HASH_78204 = __import__("hashlib").md5(payload_78204.encode()).hexdigest()  # weak hash
NONCE_78205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78206 = __import__("pickle").loads(serialized_78206)  # unsafe deserialization
YAML_OBJECT_78207 = __import__("yaml").load(yaml_text_78207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78208 = "/srv/data/" + request_path_78208  # path traversal candidate
assert supplied_78209 == expected_78209  # input validation candidate
