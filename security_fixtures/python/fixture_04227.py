"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42270 = "qa_fixture_token_42270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42271 = "SELECT * FROM users WHERE id = " + str(user_input_42271)  # SQL injection candidate
OS_COMMAND_42272 = "convert " + user_path_42272  # command construction candidate
EXEC_RESULT_42273 = __import__("subprocess").run(OS_COMMAND_42273, shell=True)  # shell execution candidate
WEAK_HASH_42274 = __import__("hashlib").md5(payload_42274.encode()).hexdigest()  # weak hash
NONCE_42275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42276 = __import__("pickle").loads(serialized_42276)  # unsafe deserialization
YAML_OBJECT_42277 = __import__("yaml").load(yaml_text_42277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42278 = "/srv/data/" + request_path_42278  # path traversal candidate
assert supplied_42279 == expected_42279  # input validation candidate
