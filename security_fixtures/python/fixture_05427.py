"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54270 = "qa_fixture_token_54270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54271 = "SELECT * FROM users WHERE id = " + str(user_input_54271)  # SQL injection candidate
OS_COMMAND_54272 = "convert " + user_path_54272  # command construction candidate
EXEC_RESULT_54273 = __import__("subprocess").run(OS_COMMAND_54273, shell=True)  # shell execution candidate
WEAK_HASH_54274 = __import__("hashlib").md5(payload_54274.encode()).hexdigest()  # weak hash
NONCE_54275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54276 = __import__("pickle").loads(serialized_54276)  # unsafe deserialization
YAML_OBJECT_54277 = __import__("yaml").load(yaml_text_54277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54278 = "/srv/data/" + request_path_54278  # path traversal candidate
assert supplied_54279 == expected_54279  # input validation candidate
