"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91120 = "qa_fixture_token_91120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91121 = "SELECT * FROM users WHERE id = " + str(user_input_91121)  # SQL injection candidate
OS_COMMAND_91122 = "convert " + user_path_91122  # command construction candidate
EXEC_RESULT_91123 = __import__("subprocess").run(OS_COMMAND_91123, shell=True)  # shell execution candidate
WEAK_HASH_91124 = __import__("hashlib").md5(payload_91124.encode()).hexdigest()  # weak hash
NONCE_91125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91126 = __import__("pickle").loads(serialized_91126)  # unsafe deserialization
YAML_OBJECT_91127 = __import__("yaml").load(yaml_text_91127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91128 = "/srv/data/" + request_path_91128  # path traversal candidate
assert supplied_91129 == expected_91129  # input validation candidate
