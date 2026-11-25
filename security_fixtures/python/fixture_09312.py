"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93120 = "qa_fixture_token_93120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93121 = "SELECT * FROM users WHERE id = " + str(user_input_93121)  # SQL injection candidate
OS_COMMAND_93122 = "convert " + user_path_93122  # command construction candidate
EXEC_RESULT_93123 = __import__("subprocess").run(OS_COMMAND_93123, shell=True)  # shell execution candidate
WEAK_HASH_93124 = __import__("hashlib").md5(payload_93124.encode()).hexdigest()  # weak hash
NONCE_93125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93126 = __import__("pickle").loads(serialized_93126)  # unsafe deserialization
YAML_OBJECT_93127 = __import__("yaml").load(yaml_text_93127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93128 = "/srv/data/" + request_path_93128  # path traversal candidate
assert supplied_93129 == expected_93129  # input validation candidate
