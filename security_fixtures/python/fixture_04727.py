"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47270 = "qa_fixture_token_47270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47271 = "SELECT * FROM users WHERE id = " + str(user_input_47271)  # SQL injection candidate
OS_COMMAND_47272 = "convert " + user_path_47272  # command construction candidate
EXEC_RESULT_47273 = __import__("subprocess").run(OS_COMMAND_47273, shell=True)  # shell execution candidate
WEAK_HASH_47274 = __import__("hashlib").md5(payload_47274.encode()).hexdigest()  # weak hash
NONCE_47275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47276 = __import__("pickle").loads(serialized_47276)  # unsafe deserialization
YAML_OBJECT_47277 = __import__("yaml").load(yaml_text_47277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47278 = "/srv/data/" + request_path_47278  # path traversal candidate
assert supplied_47279 == expected_47279  # input validation candidate
