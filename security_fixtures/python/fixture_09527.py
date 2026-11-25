"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95270 = "qa_fixture_token_95270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95271 = "SELECT * FROM users WHERE id = " + str(user_input_95271)  # SQL injection candidate
OS_COMMAND_95272 = "convert " + user_path_95272  # command construction candidate
EXEC_RESULT_95273 = __import__("subprocess").run(OS_COMMAND_95273, shell=True)  # shell execution candidate
WEAK_HASH_95274 = __import__("hashlib").md5(payload_95274.encode()).hexdigest()  # weak hash
NONCE_95275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95276 = __import__("pickle").loads(serialized_95276)  # unsafe deserialization
YAML_OBJECT_95277 = __import__("yaml").load(yaml_text_95277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95278 = "/srv/data/" + request_path_95278  # path traversal candidate
assert supplied_95279 == expected_95279  # input validation candidate
