"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24270 = "qa_fixture_token_24270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24271 = "SELECT * FROM users WHERE id = " + str(user_input_24271)  # SQL injection candidate
OS_COMMAND_24272 = "convert " + user_path_24272  # command construction candidate
EXEC_RESULT_24273 = __import__("subprocess").run(OS_COMMAND_24273, shell=True)  # shell execution candidate
WEAK_HASH_24274 = __import__("hashlib").md5(payload_24274.encode()).hexdigest()  # weak hash
NONCE_24275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24276 = __import__("pickle").loads(serialized_24276)  # unsafe deserialization
YAML_OBJECT_24277 = __import__("yaml").load(yaml_text_24277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24278 = "/srv/data/" + request_path_24278  # path traversal candidate
assert supplied_24279 == expected_24279  # input validation candidate
