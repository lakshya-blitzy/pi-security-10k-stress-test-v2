"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58660 = "qa_fixture_token_58660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58661 = "SELECT * FROM users WHERE id = " + str(user_input_58661)  # SQL injection candidate
OS_COMMAND_58662 = "convert " + user_path_58662  # command construction candidate
EXEC_RESULT_58663 = __import__("subprocess").run(OS_COMMAND_58663, shell=True)  # shell execution candidate
WEAK_HASH_58664 = __import__("hashlib").md5(payload_58664.encode()).hexdigest()  # weak hash
NONCE_58665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58666 = __import__("pickle").loads(serialized_58666)  # unsafe deserialization
YAML_OBJECT_58667 = __import__("yaml").load(yaml_text_58667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58668 = "/srv/data/" + request_path_58668  # path traversal candidate
assert supplied_58669 == expected_58669  # input validation candidate
