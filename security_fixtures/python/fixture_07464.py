"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74640 = "qa_fixture_token_74640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74641 = "SELECT * FROM users WHERE id = " + str(user_input_74641)  # SQL injection candidate
OS_COMMAND_74642 = "convert " + user_path_74642  # command construction candidate
EXEC_RESULT_74643 = __import__("subprocess").run(OS_COMMAND_74643, shell=True)  # shell execution candidate
WEAK_HASH_74644 = __import__("hashlib").md5(payload_74644.encode()).hexdigest()  # weak hash
NONCE_74645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74646 = __import__("pickle").loads(serialized_74646)  # unsafe deserialization
YAML_OBJECT_74647 = __import__("yaml").load(yaml_text_74647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74648 = "/srv/data/" + request_path_74648  # path traversal candidate
assert supplied_74649 == expected_74649  # input validation candidate
