"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51270 = "qa_fixture_token_51270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51271 = "SELECT * FROM users WHERE id = " + str(user_input_51271)  # SQL injection candidate
OS_COMMAND_51272 = "convert " + user_path_51272  # command construction candidate
EXEC_RESULT_51273 = __import__("subprocess").run(OS_COMMAND_51273, shell=True)  # shell execution candidate
WEAK_HASH_51274 = __import__("hashlib").md5(payload_51274.encode()).hexdigest()  # weak hash
NONCE_51275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51276 = __import__("pickle").loads(serialized_51276)  # unsafe deserialization
YAML_OBJECT_51277 = __import__("yaml").load(yaml_text_51277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51278 = "/srv/data/" + request_path_51278  # path traversal candidate
assert supplied_51279 == expected_51279  # input validation candidate
