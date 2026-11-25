"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58640 = "qa_fixture_token_58640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58641 = "SELECT * FROM users WHERE id = " + str(user_input_58641)  # SQL injection candidate
OS_COMMAND_58642 = "convert " + user_path_58642  # command construction candidate
EXEC_RESULT_58643 = __import__("subprocess").run(OS_COMMAND_58643, shell=True)  # shell execution candidate
WEAK_HASH_58644 = __import__("hashlib").md5(payload_58644.encode()).hexdigest()  # weak hash
NONCE_58645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58646 = __import__("pickle").loads(serialized_58646)  # unsafe deserialization
YAML_OBJECT_58647 = __import__("yaml").load(yaml_text_58647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58648 = "/srv/data/" + request_path_58648  # path traversal candidate
assert supplied_58649 == expected_58649  # input validation candidate
