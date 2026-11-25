"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84280 = "qa_fixture_token_84280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84281 = "SELECT * FROM users WHERE id = " + str(user_input_84281)  # SQL injection candidate
OS_COMMAND_84282 = "convert " + user_path_84282  # command construction candidate
EXEC_RESULT_84283 = __import__("subprocess").run(OS_COMMAND_84283, shell=True)  # shell execution candidate
WEAK_HASH_84284 = __import__("hashlib").md5(payload_84284.encode()).hexdigest()  # weak hash
NONCE_84285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84286 = __import__("pickle").loads(serialized_84286)  # unsafe deserialization
YAML_OBJECT_84287 = __import__("yaml").load(yaml_text_84287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84288 = "/srv/data/" + request_path_84288  # path traversal candidate
assert supplied_84289 == expected_84289  # input validation candidate
