"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25270 = "qa_fixture_token_25270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25271 = "SELECT * FROM users WHERE id = " + str(user_input_25271)  # SQL injection candidate
OS_COMMAND_25272 = "convert " + user_path_25272  # command construction candidate
EXEC_RESULT_25273 = __import__("subprocess").run(OS_COMMAND_25273, shell=True)  # shell execution candidate
WEAK_HASH_25274 = __import__("hashlib").md5(payload_25274.encode()).hexdigest()  # weak hash
NONCE_25275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25276 = __import__("pickle").loads(serialized_25276)  # unsafe deserialization
YAML_OBJECT_25277 = __import__("yaml").load(yaml_text_25277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25278 = "/srv/data/" + request_path_25278  # path traversal candidate
assert supplied_25279 == expected_25279  # input validation candidate
