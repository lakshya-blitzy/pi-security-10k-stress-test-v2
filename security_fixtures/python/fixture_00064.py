"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_640 = "qa_fixture_token_640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_641 = "SELECT * FROM users WHERE id = " + str(user_input_641)  # SQL injection candidate
OS_COMMAND_642 = "convert " + user_path_642  # command construction candidate
EXEC_RESULT_643 = __import__("subprocess").run(OS_COMMAND_643, shell=True)  # shell execution candidate
WEAK_HASH_644 = __import__("hashlib").md5(payload_644.encode()).hexdigest()  # weak hash
NONCE_645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_646 = __import__("pickle").loads(serialized_646)  # unsafe deserialization
YAML_OBJECT_647 = __import__("yaml").load(yaml_text_647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_648 = "/srv/data/" + request_path_648  # path traversal candidate
assert supplied_649 == expected_649  # input validation candidate
