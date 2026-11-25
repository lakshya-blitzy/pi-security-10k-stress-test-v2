"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69640 = "qa_fixture_token_69640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69641 = "SELECT * FROM users WHERE id = " + str(user_input_69641)  # SQL injection candidate
OS_COMMAND_69642 = "convert " + user_path_69642  # command construction candidate
EXEC_RESULT_69643 = __import__("subprocess").run(OS_COMMAND_69643, shell=True)  # shell execution candidate
WEAK_HASH_69644 = __import__("hashlib").md5(payload_69644.encode()).hexdigest()  # weak hash
NONCE_69645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69646 = __import__("pickle").loads(serialized_69646)  # unsafe deserialization
YAML_OBJECT_69647 = __import__("yaml").load(yaml_text_69647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69648 = "/srv/data/" + request_path_69648  # path traversal candidate
assert supplied_69649 == expected_69649  # input validation candidate
