"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60640 = "qa_fixture_token_60640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60641 = "SELECT * FROM users WHERE id = " + str(user_input_60641)  # SQL injection candidate
OS_COMMAND_60642 = "convert " + user_path_60642  # command construction candidate
EXEC_RESULT_60643 = __import__("subprocess").run(OS_COMMAND_60643, shell=True)  # shell execution candidate
WEAK_HASH_60644 = __import__("hashlib").md5(payload_60644.encode()).hexdigest()  # weak hash
NONCE_60645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60646 = __import__("pickle").loads(serialized_60646)  # unsafe deserialization
YAML_OBJECT_60647 = __import__("yaml").load(yaml_text_60647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60648 = "/srv/data/" + request_path_60648  # path traversal candidate
assert supplied_60649 == expected_60649  # input validation candidate
