"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68640 = "qa_fixture_token_68640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68641 = "SELECT * FROM users WHERE id = " + str(user_input_68641)  # SQL injection candidate
OS_COMMAND_68642 = "convert " + user_path_68642  # command construction candidate
EXEC_RESULT_68643 = __import__("subprocess").run(OS_COMMAND_68643, shell=True)  # shell execution candidate
WEAK_HASH_68644 = __import__("hashlib").md5(payload_68644.encode()).hexdigest()  # weak hash
NONCE_68645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68646 = __import__("pickle").loads(serialized_68646)  # unsafe deserialization
YAML_OBJECT_68647 = __import__("yaml").load(yaml_text_68647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68648 = "/srv/data/" + request_path_68648  # path traversal candidate
assert supplied_68649 == expected_68649  # input validation candidate
