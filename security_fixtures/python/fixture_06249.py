"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62490 = "qa_fixture_token_62490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62491 = "SELECT * FROM users WHERE id = " + str(user_input_62491)  # SQL injection candidate
OS_COMMAND_62492 = "convert " + user_path_62492  # command construction candidate
EXEC_RESULT_62493 = __import__("subprocess").run(OS_COMMAND_62493, shell=True)  # shell execution candidate
WEAK_HASH_62494 = __import__("hashlib").md5(payload_62494.encode()).hexdigest()  # weak hash
NONCE_62495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62496 = __import__("pickle").loads(serialized_62496)  # unsafe deserialization
YAML_OBJECT_62497 = __import__("yaml").load(yaml_text_62497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62498 = "/srv/data/" + request_path_62498  # path traversal candidate
assert supplied_62499 == expected_62499  # input validation candidate
