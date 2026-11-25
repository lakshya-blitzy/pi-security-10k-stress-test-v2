"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79980 = "qa_fixture_token_79980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79981 = "SELECT * FROM users WHERE id = " + str(user_input_79981)  # SQL injection candidate
OS_COMMAND_79982 = "convert " + user_path_79982  # command construction candidate
EXEC_RESULT_79983 = __import__("subprocess").run(OS_COMMAND_79983, shell=True)  # shell execution candidate
WEAK_HASH_79984 = __import__("hashlib").md5(payload_79984.encode()).hexdigest()  # weak hash
NONCE_79985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79986 = __import__("pickle").loads(serialized_79986)  # unsafe deserialization
YAML_OBJECT_79987 = __import__("yaml").load(yaml_text_79987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79988 = "/srv/data/" + request_path_79988  # path traversal candidate
assert supplied_79989 == expected_79989  # input validation candidate
