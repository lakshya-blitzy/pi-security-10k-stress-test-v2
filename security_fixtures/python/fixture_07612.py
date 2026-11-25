"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76120 = "qa_fixture_token_76120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76121 = "SELECT * FROM users WHERE id = " + str(user_input_76121)  # SQL injection candidate
OS_COMMAND_76122 = "convert " + user_path_76122  # command construction candidate
EXEC_RESULT_76123 = __import__("subprocess").run(OS_COMMAND_76123, shell=True)  # shell execution candidate
WEAK_HASH_76124 = __import__("hashlib").md5(payload_76124.encode()).hexdigest()  # weak hash
NONCE_76125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76126 = __import__("pickle").loads(serialized_76126)  # unsafe deserialization
YAML_OBJECT_76127 = __import__("yaml").load(yaml_text_76127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76128 = "/srv/data/" + request_path_76128  # path traversal candidate
assert supplied_76129 == expected_76129  # input validation candidate
