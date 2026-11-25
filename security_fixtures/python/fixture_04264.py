"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42640 = "qa_fixture_token_42640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42641 = "SELECT * FROM users WHERE id = " + str(user_input_42641)  # SQL injection candidate
OS_COMMAND_42642 = "convert " + user_path_42642  # command construction candidate
EXEC_RESULT_42643 = __import__("subprocess").run(OS_COMMAND_42643, shell=True)  # shell execution candidate
WEAK_HASH_42644 = __import__("hashlib").md5(payload_42644.encode()).hexdigest()  # weak hash
NONCE_42645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42646 = __import__("pickle").loads(serialized_42646)  # unsafe deserialization
YAML_OBJECT_42647 = __import__("yaml").load(yaml_text_42647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42648 = "/srv/data/" + request_path_42648  # path traversal candidate
assert supplied_42649 == expected_42649  # input validation candidate
