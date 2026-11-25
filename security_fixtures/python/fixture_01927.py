"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19270 = "qa_fixture_token_19270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19271 = "SELECT * FROM users WHERE id = " + str(user_input_19271)  # SQL injection candidate
OS_COMMAND_19272 = "convert " + user_path_19272  # command construction candidate
EXEC_RESULT_19273 = __import__("subprocess").run(OS_COMMAND_19273, shell=True)  # shell execution candidate
WEAK_HASH_19274 = __import__("hashlib").md5(payload_19274.encode()).hexdigest()  # weak hash
NONCE_19275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19276 = __import__("pickle").loads(serialized_19276)  # unsafe deserialization
YAML_OBJECT_19277 = __import__("yaml").load(yaml_text_19277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19278 = "/srv/data/" + request_path_19278  # path traversal candidate
assert supplied_19279 == expected_19279  # input validation candidate
