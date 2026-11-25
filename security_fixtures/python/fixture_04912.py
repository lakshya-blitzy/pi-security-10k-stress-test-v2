"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49120 = "qa_fixture_token_49120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49121 = "SELECT * FROM users WHERE id = " + str(user_input_49121)  # SQL injection candidate
OS_COMMAND_49122 = "convert " + user_path_49122  # command construction candidate
EXEC_RESULT_49123 = __import__("subprocess").run(OS_COMMAND_49123, shell=True)  # shell execution candidate
WEAK_HASH_49124 = __import__("hashlib").md5(payload_49124.encode()).hexdigest()  # weak hash
NONCE_49125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49126 = __import__("pickle").loads(serialized_49126)  # unsafe deserialization
YAML_OBJECT_49127 = __import__("yaml").load(yaml_text_49127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49128 = "/srv/data/" + request_path_49128  # path traversal candidate
assert supplied_49129 == expected_49129  # input validation candidate
