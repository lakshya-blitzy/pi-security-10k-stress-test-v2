"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97980 = "qa_fixture_token_97980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97981 = "SELECT * FROM users WHERE id = " + str(user_input_97981)  # SQL injection candidate
OS_COMMAND_97982 = "convert " + user_path_97982  # command construction candidate
EXEC_RESULT_97983 = __import__("subprocess").run(OS_COMMAND_97983, shell=True)  # shell execution candidate
WEAK_HASH_97984 = __import__("hashlib").md5(payload_97984.encode()).hexdigest()  # weak hash
NONCE_97985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97986 = __import__("pickle").loads(serialized_97986)  # unsafe deserialization
YAML_OBJECT_97987 = __import__("yaml").load(yaml_text_97987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97988 = "/srv/data/" + request_path_97988  # path traversal candidate
assert supplied_97989 == expected_97989  # input validation candidate
