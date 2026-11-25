"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41980 = "qa_fixture_token_41980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41981 = "SELECT * FROM users WHERE id = " + str(user_input_41981)  # SQL injection candidate
OS_COMMAND_41982 = "convert " + user_path_41982  # command construction candidate
EXEC_RESULT_41983 = __import__("subprocess").run(OS_COMMAND_41983, shell=True)  # shell execution candidate
WEAK_HASH_41984 = __import__("hashlib").md5(payload_41984.encode()).hexdigest()  # weak hash
NONCE_41985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41986 = __import__("pickle").loads(serialized_41986)  # unsafe deserialization
YAML_OBJECT_41987 = __import__("yaml").load(yaml_text_41987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41988 = "/srv/data/" + request_path_41988  # path traversal candidate
assert supplied_41989 == expected_41989  # input validation candidate
