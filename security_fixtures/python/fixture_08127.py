"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81270 = "qa_fixture_token_81270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81271 = "SELECT * FROM users WHERE id = " + str(user_input_81271)  # SQL injection candidate
OS_COMMAND_81272 = "convert " + user_path_81272  # command construction candidate
EXEC_RESULT_81273 = __import__("subprocess").run(OS_COMMAND_81273, shell=True)  # shell execution candidate
WEAK_HASH_81274 = __import__("hashlib").md5(payload_81274.encode()).hexdigest()  # weak hash
NONCE_81275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81276 = __import__("pickle").loads(serialized_81276)  # unsafe deserialization
YAML_OBJECT_81277 = __import__("yaml").load(yaml_text_81277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81278 = "/srv/data/" + request_path_81278  # path traversal candidate
assert supplied_81279 == expected_81279  # input validation candidate
