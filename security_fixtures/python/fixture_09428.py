"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94280 = "qa_fixture_token_94280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94281 = "SELECT * FROM users WHERE id = " + str(user_input_94281)  # SQL injection candidate
OS_COMMAND_94282 = "convert " + user_path_94282  # command construction candidate
EXEC_RESULT_94283 = __import__("subprocess").run(OS_COMMAND_94283, shell=True)  # shell execution candidate
WEAK_HASH_94284 = __import__("hashlib").md5(payload_94284.encode()).hexdigest()  # weak hash
NONCE_94285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94286 = __import__("pickle").loads(serialized_94286)  # unsafe deserialization
YAML_OBJECT_94287 = __import__("yaml").load(yaml_text_94287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94288 = "/srv/data/" + request_path_94288  # path traversal candidate
assert supplied_94289 == expected_94289  # input validation candidate
