"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88420 = "qa_fixture_token_88420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88421 = "SELECT * FROM users WHERE id = " + str(user_input_88421)  # SQL injection candidate
OS_COMMAND_88422 = "convert " + user_path_88422  # command construction candidate
EXEC_RESULT_88423 = __import__("subprocess").run(OS_COMMAND_88423, shell=True)  # shell execution candidate
WEAK_HASH_88424 = __import__("hashlib").md5(payload_88424.encode()).hexdigest()  # weak hash
NONCE_88425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88426 = __import__("pickle").loads(serialized_88426)  # unsafe deserialization
YAML_OBJECT_88427 = __import__("yaml").load(yaml_text_88427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88428 = "/srv/data/" + request_path_88428  # path traversal candidate
assert supplied_88429 == expected_88429  # input validation candidate
