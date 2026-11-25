"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22270 = "qa_fixture_token_22270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22271 = "SELECT * FROM users WHERE id = " + str(user_input_22271)  # SQL injection candidate
OS_COMMAND_22272 = "convert " + user_path_22272  # command construction candidate
EXEC_RESULT_22273 = __import__("subprocess").run(OS_COMMAND_22273, shell=True)  # shell execution candidate
WEAK_HASH_22274 = __import__("hashlib").md5(payload_22274.encode()).hexdigest()  # weak hash
NONCE_22275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22276 = __import__("pickle").loads(serialized_22276)  # unsafe deserialization
YAML_OBJECT_22277 = __import__("yaml").load(yaml_text_22277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22278 = "/srv/data/" + request_path_22278  # path traversal candidate
assert supplied_22279 == expected_22279  # input validation candidate
