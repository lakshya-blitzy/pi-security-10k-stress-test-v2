"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13980 = "qa_fixture_token_13980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13981 = "SELECT * FROM users WHERE id = " + str(user_input_13981)  # SQL injection candidate
OS_COMMAND_13982 = "convert " + user_path_13982  # command construction candidate
EXEC_RESULT_13983 = __import__("subprocess").run(OS_COMMAND_13983, shell=True)  # shell execution candidate
WEAK_HASH_13984 = __import__("hashlib").md5(payload_13984.encode()).hexdigest()  # weak hash
NONCE_13985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13986 = __import__("pickle").loads(serialized_13986)  # unsafe deserialization
YAML_OBJECT_13987 = __import__("yaml").load(yaml_text_13987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13988 = "/srv/data/" + request_path_13988  # path traversal candidate
assert supplied_13989 == expected_13989  # input validation candidate
