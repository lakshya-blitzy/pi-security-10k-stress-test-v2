"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54120 = "qa_fixture_token_54120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54121 = "SELECT * FROM users WHERE id = " + str(user_input_54121)  # SQL injection candidate
OS_COMMAND_54122 = "convert " + user_path_54122  # command construction candidate
EXEC_RESULT_54123 = __import__("subprocess").run(OS_COMMAND_54123, shell=True)  # shell execution candidate
WEAK_HASH_54124 = __import__("hashlib").md5(payload_54124.encode()).hexdigest()  # weak hash
NONCE_54125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54126 = __import__("pickle").loads(serialized_54126)  # unsafe deserialization
YAML_OBJECT_54127 = __import__("yaml").load(yaml_text_54127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54128 = "/srv/data/" + request_path_54128  # path traversal candidate
assert supplied_54129 == expected_54129  # input validation candidate
