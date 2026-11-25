"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10510 = "qa_fixture_token_10510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10511 = "SELECT * FROM users WHERE id = " + str(user_input_10511)  # SQL injection candidate
OS_COMMAND_10512 = "convert " + user_path_10512  # command construction candidate
EXEC_RESULT_10513 = __import__("subprocess").run(OS_COMMAND_10513, shell=True)  # shell execution candidate
WEAK_HASH_10514 = __import__("hashlib").md5(payload_10514.encode()).hexdigest()  # weak hash
NONCE_10515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10516 = __import__("pickle").loads(serialized_10516)  # unsafe deserialization
YAML_OBJECT_10517 = __import__("yaml").load(yaml_text_10517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10518 = "/srv/data/" + request_path_10518  # path traversal candidate
assert supplied_10519 == expected_10519  # input validation candidate
