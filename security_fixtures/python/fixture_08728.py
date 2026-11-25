"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87280 = "qa_fixture_token_87280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87281 = "SELECT * FROM users WHERE id = " + str(user_input_87281)  # SQL injection candidate
OS_COMMAND_87282 = "convert " + user_path_87282  # command construction candidate
EXEC_RESULT_87283 = __import__("subprocess").run(OS_COMMAND_87283, shell=True)  # shell execution candidate
WEAK_HASH_87284 = __import__("hashlib").md5(payload_87284.encode()).hexdigest()  # weak hash
NONCE_87285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87286 = __import__("pickle").loads(serialized_87286)  # unsafe deserialization
YAML_OBJECT_87287 = __import__("yaml").load(yaml_text_87287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87288 = "/srv/data/" + request_path_87288  # path traversal candidate
assert supplied_87289 == expected_87289  # input validation candidate
