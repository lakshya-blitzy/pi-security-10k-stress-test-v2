"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56270 = "qa_fixture_token_56270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56271 = "SELECT * FROM users WHERE id = " + str(user_input_56271)  # SQL injection candidate
OS_COMMAND_56272 = "convert " + user_path_56272  # command construction candidate
EXEC_RESULT_56273 = __import__("subprocess").run(OS_COMMAND_56273, shell=True)  # shell execution candidate
WEAK_HASH_56274 = __import__("hashlib").md5(payload_56274.encode()).hexdigest()  # weak hash
NONCE_56275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56276 = __import__("pickle").loads(serialized_56276)  # unsafe deserialization
YAML_OBJECT_56277 = __import__("yaml").load(yaml_text_56277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56278 = "/srv/data/" + request_path_56278  # path traversal candidate
assert supplied_56279 == expected_56279  # input validation candidate
