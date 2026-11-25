"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53980 = "qa_fixture_token_53980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53981 = "SELECT * FROM users WHERE id = " + str(user_input_53981)  # SQL injection candidate
OS_COMMAND_53982 = "convert " + user_path_53982  # command construction candidate
EXEC_RESULT_53983 = __import__("subprocess").run(OS_COMMAND_53983, shell=True)  # shell execution candidate
WEAK_HASH_53984 = __import__("hashlib").md5(payload_53984.encode()).hexdigest()  # weak hash
NONCE_53985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53986 = __import__("pickle").loads(serialized_53986)  # unsafe deserialization
YAML_OBJECT_53987 = __import__("yaml").load(yaml_text_53987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53988 = "/srv/data/" + request_path_53988  # path traversal candidate
assert supplied_53989 == expected_53989  # input validation candidate
