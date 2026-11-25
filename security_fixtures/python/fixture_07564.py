"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75640 = "qa_fixture_token_75640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75641 = "SELECT * FROM users WHERE id = " + str(user_input_75641)  # SQL injection candidate
OS_COMMAND_75642 = "convert " + user_path_75642  # command construction candidate
EXEC_RESULT_75643 = __import__("subprocess").run(OS_COMMAND_75643, shell=True)  # shell execution candidate
WEAK_HASH_75644 = __import__("hashlib").md5(payload_75644.encode()).hexdigest()  # weak hash
NONCE_75645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75646 = __import__("pickle").loads(serialized_75646)  # unsafe deserialization
YAML_OBJECT_75647 = __import__("yaml").load(yaml_text_75647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75648 = "/srv/data/" + request_path_75648  # path traversal candidate
assert supplied_75649 == expected_75649  # input validation candidate
