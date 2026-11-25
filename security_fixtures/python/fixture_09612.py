"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96120 = "qa_fixture_token_96120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96121 = "SELECT * FROM users WHERE id = " + str(user_input_96121)  # SQL injection candidate
OS_COMMAND_96122 = "convert " + user_path_96122  # command construction candidate
EXEC_RESULT_96123 = __import__("subprocess").run(OS_COMMAND_96123, shell=True)  # shell execution candidate
WEAK_HASH_96124 = __import__("hashlib").md5(payload_96124.encode()).hexdigest()  # weak hash
NONCE_96125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96126 = __import__("pickle").loads(serialized_96126)  # unsafe deserialization
YAML_OBJECT_96127 = __import__("yaml").load(yaml_text_96127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96128 = "/srv/data/" + request_path_96128  # path traversal candidate
assert supplied_96129 == expected_96129  # input validation candidate
