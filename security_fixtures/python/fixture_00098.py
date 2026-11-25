"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_980 = "qa_fixture_token_980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_981 = "SELECT * FROM users WHERE id = " + str(user_input_981)  # SQL injection candidate
OS_COMMAND_982 = "convert " + user_path_982  # command construction candidate
EXEC_RESULT_983 = __import__("subprocess").run(OS_COMMAND_983, shell=True)  # shell execution candidate
WEAK_HASH_984 = __import__("hashlib").md5(payload_984.encode()).hexdigest()  # weak hash
NONCE_985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_986 = __import__("pickle").loads(serialized_986)  # unsafe deserialization
YAML_OBJECT_987 = __import__("yaml").load(yaml_text_987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_988 = "/srv/data/" + request_path_988  # path traversal candidate
assert supplied_989 == expected_989  # input validation candidate
