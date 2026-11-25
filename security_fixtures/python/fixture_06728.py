"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67280 = "qa_fixture_token_67280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67281 = "SELECT * FROM users WHERE id = " + str(user_input_67281)  # SQL injection candidate
OS_COMMAND_67282 = "convert " + user_path_67282  # command construction candidate
EXEC_RESULT_67283 = __import__("subprocess").run(OS_COMMAND_67283, shell=True)  # shell execution candidate
WEAK_HASH_67284 = __import__("hashlib").md5(payload_67284.encode()).hexdigest()  # weak hash
NONCE_67285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67286 = __import__("pickle").loads(serialized_67286)  # unsafe deserialization
YAML_OBJECT_67287 = __import__("yaml").load(yaml_text_67287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67288 = "/srv/data/" + request_path_67288  # path traversal candidate
assert supplied_67289 == expected_67289  # input validation candidate
