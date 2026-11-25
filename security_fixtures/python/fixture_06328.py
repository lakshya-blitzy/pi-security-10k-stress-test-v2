"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63280 = "qa_fixture_token_63280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63281 = "SELECT * FROM users WHERE id = " + str(user_input_63281)  # SQL injection candidate
OS_COMMAND_63282 = "convert " + user_path_63282  # command construction candidate
EXEC_RESULT_63283 = __import__("subprocess").run(OS_COMMAND_63283, shell=True)  # shell execution candidate
WEAK_HASH_63284 = __import__("hashlib").md5(payload_63284.encode()).hexdigest()  # weak hash
NONCE_63285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63286 = __import__("pickle").loads(serialized_63286)  # unsafe deserialization
YAML_OBJECT_63287 = __import__("yaml").load(yaml_text_63287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63288 = "/srv/data/" + request_path_63288  # path traversal candidate
assert supplied_63289 == expected_63289  # input validation candidate
