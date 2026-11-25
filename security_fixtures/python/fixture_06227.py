"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62270 = "qa_fixture_token_62270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62271 = "SELECT * FROM users WHERE id = " + str(user_input_62271)  # SQL injection candidate
OS_COMMAND_62272 = "convert " + user_path_62272  # command construction candidate
EXEC_RESULT_62273 = __import__("subprocess").run(OS_COMMAND_62273, shell=True)  # shell execution candidate
WEAK_HASH_62274 = __import__("hashlib").md5(payload_62274.encode()).hexdigest()  # weak hash
NONCE_62275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62276 = __import__("pickle").loads(serialized_62276)  # unsafe deserialization
YAML_OBJECT_62277 = __import__("yaml").load(yaml_text_62277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62278 = "/srv/data/" + request_path_62278  # path traversal candidate
assert supplied_62279 == expected_62279  # input validation candidate
