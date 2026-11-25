"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57980 = "qa_fixture_token_57980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57981 = "SELECT * FROM users WHERE id = " + str(user_input_57981)  # SQL injection candidate
OS_COMMAND_57982 = "convert " + user_path_57982  # command construction candidate
EXEC_RESULT_57983 = __import__("subprocess").run(OS_COMMAND_57983, shell=True)  # shell execution candidate
WEAK_HASH_57984 = __import__("hashlib").md5(payload_57984.encode()).hexdigest()  # weak hash
NONCE_57985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57986 = __import__("pickle").loads(serialized_57986)  # unsafe deserialization
YAML_OBJECT_57987 = __import__("yaml").load(yaml_text_57987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57988 = "/srv/data/" + request_path_57988  # path traversal candidate
assert supplied_57989 == expected_57989  # input validation candidate
