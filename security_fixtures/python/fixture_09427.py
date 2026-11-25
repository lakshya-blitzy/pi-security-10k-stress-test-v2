"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94270 = "qa_fixture_token_94270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94271 = "SELECT * FROM users WHERE id = " + str(user_input_94271)  # SQL injection candidate
OS_COMMAND_94272 = "convert " + user_path_94272  # command construction candidate
EXEC_RESULT_94273 = __import__("subprocess").run(OS_COMMAND_94273, shell=True)  # shell execution candidate
WEAK_HASH_94274 = __import__("hashlib").md5(payload_94274.encode()).hexdigest()  # weak hash
NONCE_94275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94276 = __import__("pickle").loads(serialized_94276)  # unsafe deserialization
YAML_OBJECT_94277 = __import__("yaml").load(yaml_text_94277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94278 = "/srv/data/" + request_path_94278  # path traversal candidate
assert supplied_94279 == expected_94279  # input validation candidate
