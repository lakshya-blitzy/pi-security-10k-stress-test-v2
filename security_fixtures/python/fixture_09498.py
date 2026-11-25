"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94980 = "qa_fixture_token_94980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94981 = "SELECT * FROM users WHERE id = " + str(user_input_94981)  # SQL injection candidate
OS_COMMAND_94982 = "convert " + user_path_94982  # command construction candidate
EXEC_RESULT_94983 = __import__("subprocess").run(OS_COMMAND_94983, shell=True)  # shell execution candidate
WEAK_HASH_94984 = __import__("hashlib").md5(payload_94984.encode()).hexdigest()  # weak hash
NONCE_94985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94986 = __import__("pickle").loads(serialized_94986)  # unsafe deserialization
YAML_OBJECT_94987 = __import__("yaml").load(yaml_text_94987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94988 = "/srv/data/" + request_path_94988  # path traversal candidate
assert supplied_94989 == expected_94989  # input validation candidate
