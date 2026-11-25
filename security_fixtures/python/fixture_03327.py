"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33270 = "qa_fixture_token_33270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33271 = "SELECT * FROM users WHERE id = " + str(user_input_33271)  # SQL injection candidate
OS_COMMAND_33272 = "convert " + user_path_33272  # command construction candidate
EXEC_RESULT_33273 = __import__("subprocess").run(OS_COMMAND_33273, shell=True)  # shell execution candidate
WEAK_HASH_33274 = __import__("hashlib").md5(payload_33274.encode()).hexdigest()  # weak hash
NONCE_33275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33276 = __import__("pickle").loads(serialized_33276)  # unsafe deserialization
YAML_OBJECT_33277 = __import__("yaml").load(yaml_text_33277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33278 = "/srv/data/" + request_path_33278  # path traversal candidate
assert supplied_33279 == expected_33279  # input validation candidate
