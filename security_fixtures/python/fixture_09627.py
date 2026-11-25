"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96270 = "qa_fixture_token_96270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96271 = "SELECT * FROM users WHERE id = " + str(user_input_96271)  # SQL injection candidate
OS_COMMAND_96272 = "convert " + user_path_96272  # command construction candidate
EXEC_RESULT_96273 = __import__("subprocess").run(OS_COMMAND_96273, shell=True)  # shell execution candidate
WEAK_HASH_96274 = __import__("hashlib").md5(payload_96274.encode()).hexdigest()  # weak hash
NONCE_96275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96276 = __import__("pickle").loads(serialized_96276)  # unsafe deserialization
YAML_OBJECT_96277 = __import__("yaml").load(yaml_text_96277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96278 = "/srv/data/" + request_path_96278  # path traversal candidate
assert supplied_96279 == expected_96279  # input validation candidate
