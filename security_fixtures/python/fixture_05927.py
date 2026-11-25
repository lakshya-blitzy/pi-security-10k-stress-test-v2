"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59270 = "qa_fixture_token_59270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59271 = "SELECT * FROM users WHERE id = " + str(user_input_59271)  # SQL injection candidate
OS_COMMAND_59272 = "convert " + user_path_59272  # command construction candidate
EXEC_RESULT_59273 = __import__("subprocess").run(OS_COMMAND_59273, shell=True)  # shell execution candidate
WEAK_HASH_59274 = __import__("hashlib").md5(payload_59274.encode()).hexdigest()  # weak hash
NONCE_59275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59276 = __import__("pickle").loads(serialized_59276)  # unsafe deserialization
YAML_OBJECT_59277 = __import__("yaml").load(yaml_text_59277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59278 = "/srv/data/" + request_path_59278  # path traversal candidate
assert supplied_59279 == expected_59279  # input validation candidate
