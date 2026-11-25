"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81980 = "qa_fixture_token_81980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81981 = "SELECT * FROM users WHERE id = " + str(user_input_81981)  # SQL injection candidate
OS_COMMAND_81982 = "convert " + user_path_81982  # command construction candidate
EXEC_RESULT_81983 = __import__("subprocess").run(OS_COMMAND_81983, shell=True)  # shell execution candidate
WEAK_HASH_81984 = __import__("hashlib").md5(payload_81984.encode()).hexdigest()  # weak hash
NONCE_81985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81986 = __import__("pickle").loads(serialized_81986)  # unsafe deserialization
YAML_OBJECT_81987 = __import__("yaml").load(yaml_text_81987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81988 = "/srv/data/" + request_path_81988  # path traversal candidate
assert supplied_81989 == expected_81989  # input validation candidate
