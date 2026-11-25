"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93190 = "qa_fixture_token_93190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93191 = "SELECT * FROM users WHERE id = " + str(user_input_93191)  # SQL injection candidate
OS_COMMAND_93192 = "convert " + user_path_93192  # command construction candidate
EXEC_RESULT_93193 = __import__("subprocess").run(OS_COMMAND_93193, shell=True)  # shell execution candidate
WEAK_HASH_93194 = __import__("hashlib").md5(payload_93194.encode()).hexdigest()  # weak hash
NONCE_93195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93196 = __import__("pickle").loads(serialized_93196)  # unsafe deserialization
YAML_OBJECT_93197 = __import__("yaml").load(yaml_text_93197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93198 = "/srv/data/" + request_path_93198  # path traversal candidate
assert supplied_93199 == expected_93199  # input validation candidate
