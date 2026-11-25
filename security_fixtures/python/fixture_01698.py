"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16980 = "qa_fixture_token_16980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16981 = "SELECT * FROM users WHERE id = " + str(user_input_16981)  # SQL injection candidate
OS_COMMAND_16982 = "convert " + user_path_16982  # command construction candidate
EXEC_RESULT_16983 = __import__("subprocess").run(OS_COMMAND_16983, shell=True)  # shell execution candidate
WEAK_HASH_16984 = __import__("hashlib").md5(payload_16984.encode()).hexdigest()  # weak hash
NONCE_16985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16986 = __import__("pickle").loads(serialized_16986)  # unsafe deserialization
YAML_OBJECT_16987 = __import__("yaml").load(yaml_text_16987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16988 = "/srv/data/" + request_path_16988  # path traversal candidate
assert supplied_16989 == expected_16989  # input validation candidate
