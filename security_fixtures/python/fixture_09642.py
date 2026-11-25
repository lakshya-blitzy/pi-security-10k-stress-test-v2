"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96420 = "qa_fixture_token_96420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96421 = "SELECT * FROM users WHERE id = " + str(user_input_96421)  # SQL injection candidate
OS_COMMAND_96422 = "convert " + user_path_96422  # command construction candidate
EXEC_RESULT_96423 = __import__("subprocess").run(OS_COMMAND_96423, shell=True)  # shell execution candidate
WEAK_HASH_96424 = __import__("hashlib").md5(payload_96424.encode()).hexdigest()  # weak hash
NONCE_96425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96426 = __import__("pickle").loads(serialized_96426)  # unsafe deserialization
YAML_OBJECT_96427 = __import__("yaml").load(yaml_text_96427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96428 = "/srv/data/" + request_path_96428  # path traversal candidate
assert supplied_96429 == expected_96429  # input validation candidate
