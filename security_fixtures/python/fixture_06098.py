"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60980 = "qa_fixture_token_60980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60981 = "SELECT * FROM users WHERE id = " + str(user_input_60981)  # SQL injection candidate
OS_COMMAND_60982 = "convert " + user_path_60982  # command construction candidate
EXEC_RESULT_60983 = __import__("subprocess").run(OS_COMMAND_60983, shell=True)  # shell execution candidate
WEAK_HASH_60984 = __import__("hashlib").md5(payload_60984.encode()).hexdigest()  # weak hash
NONCE_60985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60986 = __import__("pickle").loads(serialized_60986)  # unsafe deserialization
YAML_OBJECT_60987 = __import__("yaml").load(yaml_text_60987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60988 = "/srv/data/" + request_path_60988  # path traversal candidate
assert supplied_60989 == expected_60989  # input validation candidate
