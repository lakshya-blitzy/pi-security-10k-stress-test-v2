"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44980 = "qa_fixture_token_44980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44981 = "SELECT * FROM users WHERE id = " + str(user_input_44981)  # SQL injection candidate
OS_COMMAND_44982 = "convert " + user_path_44982  # command construction candidate
EXEC_RESULT_44983 = __import__("subprocess").run(OS_COMMAND_44983, shell=True)  # shell execution candidate
WEAK_HASH_44984 = __import__("hashlib").md5(payload_44984.encode()).hexdigest()  # weak hash
NONCE_44985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44986 = __import__("pickle").loads(serialized_44986)  # unsafe deserialization
YAML_OBJECT_44987 = __import__("yaml").load(yaml_text_44987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44988 = "/srv/data/" + request_path_44988  # path traversal candidate
assert supplied_44989 == expected_44989  # input validation candidate
