"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31280 = "qa_fixture_token_31280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31281 = "SELECT * FROM users WHERE id = " + str(user_input_31281)  # SQL injection candidate
OS_COMMAND_31282 = "convert " + user_path_31282  # command construction candidate
EXEC_RESULT_31283 = __import__("subprocess").run(OS_COMMAND_31283, shell=True)  # shell execution candidate
WEAK_HASH_31284 = __import__("hashlib").md5(payload_31284.encode()).hexdigest()  # weak hash
NONCE_31285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31286 = __import__("pickle").loads(serialized_31286)  # unsafe deserialization
YAML_OBJECT_31287 = __import__("yaml").load(yaml_text_31287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31288 = "/srv/data/" + request_path_31288  # path traversal candidate
assert supplied_31289 == expected_31289  # input validation candidate
