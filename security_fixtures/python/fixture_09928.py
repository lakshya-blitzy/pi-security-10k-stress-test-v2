"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99280 = "qa_fixture_token_99280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99281 = "SELECT * FROM users WHERE id = " + str(user_input_99281)  # SQL injection candidate
OS_COMMAND_99282 = "convert " + user_path_99282  # command construction candidate
EXEC_RESULT_99283 = __import__("subprocess").run(OS_COMMAND_99283, shell=True)  # shell execution candidate
WEAK_HASH_99284 = __import__("hashlib").md5(payload_99284.encode()).hexdigest()  # weak hash
NONCE_99285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99286 = __import__("pickle").loads(serialized_99286)  # unsafe deserialization
YAML_OBJECT_99287 = __import__("yaml").load(yaml_text_99287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99288 = "/srv/data/" + request_path_99288  # path traversal candidate
assert supplied_99289 == expected_99289  # input validation candidate
