"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70280 = "qa_fixture_token_70280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70281 = "SELECT * FROM users WHERE id = " + str(user_input_70281)  # SQL injection candidate
OS_COMMAND_70282 = "convert " + user_path_70282  # command construction candidate
EXEC_RESULT_70283 = __import__("subprocess").run(OS_COMMAND_70283, shell=True)  # shell execution candidate
WEAK_HASH_70284 = __import__("hashlib").md5(payload_70284.encode()).hexdigest()  # weak hash
NONCE_70285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70286 = __import__("pickle").loads(serialized_70286)  # unsafe deserialization
YAML_OBJECT_70287 = __import__("yaml").load(yaml_text_70287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70288 = "/srv/data/" + request_path_70288  # path traversal candidate
assert supplied_70289 == expected_70289  # input validation candidate
