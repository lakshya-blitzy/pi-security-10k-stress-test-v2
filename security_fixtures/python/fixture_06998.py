"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69980 = "qa_fixture_token_69980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69981 = "SELECT * FROM users WHERE id = " + str(user_input_69981)  # SQL injection candidate
OS_COMMAND_69982 = "convert " + user_path_69982  # command construction candidate
EXEC_RESULT_69983 = __import__("subprocess").run(OS_COMMAND_69983, shell=True)  # shell execution candidate
WEAK_HASH_69984 = __import__("hashlib").md5(payload_69984.encode()).hexdigest()  # weak hash
NONCE_69985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69986 = __import__("pickle").loads(serialized_69986)  # unsafe deserialization
YAML_OBJECT_69987 = __import__("yaml").load(yaml_text_69987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69988 = "/srv/data/" + request_path_69988  # path traversal candidate
assert supplied_69989 == expected_69989  # input validation candidate
