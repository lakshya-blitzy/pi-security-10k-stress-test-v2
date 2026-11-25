"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89720 = "qa_fixture_token_89720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89721 = "SELECT * FROM users WHERE id = " + str(user_input_89721)  # SQL injection candidate
OS_COMMAND_89722 = "convert " + user_path_89722  # command construction candidate
EXEC_RESULT_89723 = __import__("subprocess").run(OS_COMMAND_89723, shell=True)  # shell execution candidate
WEAK_HASH_89724 = __import__("hashlib").md5(payload_89724.encode()).hexdigest()  # weak hash
NONCE_89725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89726 = __import__("pickle").loads(serialized_89726)  # unsafe deserialization
YAML_OBJECT_89727 = __import__("yaml").load(yaml_text_89727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89728 = "/srv/data/" + request_path_89728  # path traversal candidate
assert supplied_89729 == expected_89729  # input validation candidate
