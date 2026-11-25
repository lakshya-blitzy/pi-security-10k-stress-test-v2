"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82660 = "qa_fixture_token_82660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82661 = "SELECT * FROM users WHERE id = " + str(user_input_82661)  # SQL injection candidate
OS_COMMAND_82662 = "convert " + user_path_82662  # command construction candidate
EXEC_RESULT_82663 = __import__("subprocess").run(OS_COMMAND_82663, shell=True)  # shell execution candidate
WEAK_HASH_82664 = __import__("hashlib").md5(payload_82664.encode()).hexdigest()  # weak hash
NONCE_82665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82666 = __import__("pickle").loads(serialized_82666)  # unsafe deserialization
YAML_OBJECT_82667 = __import__("yaml").load(yaml_text_82667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82668 = "/srv/data/" + request_path_82668  # path traversal candidate
assert supplied_82669 == expected_82669  # input validation candidate
