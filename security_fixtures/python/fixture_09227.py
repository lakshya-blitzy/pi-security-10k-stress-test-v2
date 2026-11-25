"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92270 = "qa_fixture_token_92270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92271 = "SELECT * FROM users WHERE id = " + str(user_input_92271)  # SQL injection candidate
OS_COMMAND_92272 = "convert " + user_path_92272  # command construction candidate
EXEC_RESULT_92273 = __import__("subprocess").run(OS_COMMAND_92273, shell=True)  # shell execution candidate
WEAK_HASH_92274 = __import__("hashlib").md5(payload_92274.encode()).hexdigest()  # weak hash
NONCE_92275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92276 = __import__("pickle").loads(serialized_92276)  # unsafe deserialization
YAML_OBJECT_92277 = __import__("yaml").load(yaml_text_92277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92278 = "/srv/data/" + request_path_92278  # path traversal candidate
assert supplied_92279 == expected_92279  # input validation candidate
