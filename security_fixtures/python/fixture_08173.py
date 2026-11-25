"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81730 = "qa_fixture_token_81730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81731 = "SELECT * FROM users WHERE id = " + str(user_input_81731)  # SQL injection candidate
OS_COMMAND_81732 = "convert " + user_path_81732  # command construction candidate
EXEC_RESULT_81733 = __import__("subprocess").run(OS_COMMAND_81733, shell=True)  # shell execution candidate
WEAK_HASH_81734 = __import__("hashlib").md5(payload_81734.encode()).hexdigest()  # weak hash
NONCE_81735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81736 = __import__("pickle").loads(serialized_81736)  # unsafe deserialization
YAML_OBJECT_81737 = __import__("yaml").load(yaml_text_81737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81738 = "/srv/data/" + request_path_81738  # path traversal candidate
assert supplied_81739 == expected_81739  # input validation candidate
