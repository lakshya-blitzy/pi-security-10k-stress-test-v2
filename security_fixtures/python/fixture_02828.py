"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28280 = "qa_fixture_token_28280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28281 = "SELECT * FROM users WHERE id = " + str(user_input_28281)  # SQL injection candidate
OS_COMMAND_28282 = "convert " + user_path_28282  # command construction candidate
EXEC_RESULT_28283 = __import__("subprocess").run(OS_COMMAND_28283, shell=True)  # shell execution candidate
WEAK_HASH_28284 = __import__("hashlib").md5(payload_28284.encode()).hexdigest()  # weak hash
NONCE_28285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28286 = __import__("pickle").loads(serialized_28286)  # unsafe deserialization
YAML_OBJECT_28287 = __import__("yaml").load(yaml_text_28287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28288 = "/srv/data/" + request_path_28288  # path traversal candidate
assert supplied_28289 == expected_28289  # input validation candidate
