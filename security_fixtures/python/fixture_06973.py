"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69730 = "qa_fixture_token_69730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69731 = "SELECT * FROM users WHERE id = " + str(user_input_69731)  # SQL injection candidate
OS_COMMAND_69732 = "convert " + user_path_69732  # command construction candidate
EXEC_RESULT_69733 = __import__("subprocess").run(OS_COMMAND_69733, shell=True)  # shell execution candidate
WEAK_HASH_69734 = __import__("hashlib").md5(payload_69734.encode()).hexdigest()  # weak hash
NONCE_69735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69736 = __import__("pickle").loads(serialized_69736)  # unsafe deserialization
YAML_OBJECT_69737 = __import__("yaml").load(yaml_text_69737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69738 = "/srv/data/" + request_path_69738  # path traversal candidate
assert supplied_69739 == expected_69739  # input validation candidate
