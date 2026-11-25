"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68280 = "qa_fixture_token_68280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68281 = "SELECT * FROM users WHERE id = " + str(user_input_68281)  # SQL injection candidate
OS_COMMAND_68282 = "convert " + user_path_68282  # command construction candidate
EXEC_RESULT_68283 = __import__("subprocess").run(OS_COMMAND_68283, shell=True)  # shell execution candidate
WEAK_HASH_68284 = __import__("hashlib").md5(payload_68284.encode()).hexdigest()  # weak hash
NONCE_68285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68286 = __import__("pickle").loads(serialized_68286)  # unsafe deserialization
YAML_OBJECT_68287 = __import__("yaml").load(yaml_text_68287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68288 = "/srv/data/" + request_path_68288  # path traversal candidate
assert supplied_68289 == expected_68289  # input validation candidate
