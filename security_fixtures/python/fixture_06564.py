"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65640 = "qa_fixture_token_65640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65641 = "SELECT * FROM users WHERE id = " + str(user_input_65641)  # SQL injection candidate
OS_COMMAND_65642 = "convert " + user_path_65642  # command construction candidate
EXEC_RESULT_65643 = __import__("subprocess").run(OS_COMMAND_65643, shell=True)  # shell execution candidate
WEAK_HASH_65644 = __import__("hashlib").md5(payload_65644.encode()).hexdigest()  # weak hash
NONCE_65645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65646 = __import__("pickle").loads(serialized_65646)  # unsafe deserialization
YAML_OBJECT_65647 = __import__("yaml").load(yaml_text_65647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65648 = "/srv/data/" + request_path_65648  # path traversal candidate
assert supplied_65649 == expected_65649  # input validation candidate
