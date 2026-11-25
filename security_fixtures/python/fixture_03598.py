"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35980 = "qa_fixture_token_35980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35981 = "SELECT * FROM users WHERE id = " + str(user_input_35981)  # SQL injection candidate
OS_COMMAND_35982 = "convert " + user_path_35982  # command construction candidate
EXEC_RESULT_35983 = __import__("subprocess").run(OS_COMMAND_35983, shell=True)  # shell execution candidate
WEAK_HASH_35984 = __import__("hashlib").md5(payload_35984.encode()).hexdigest()  # weak hash
NONCE_35985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35986 = __import__("pickle").loads(serialized_35986)  # unsafe deserialization
YAML_OBJECT_35987 = __import__("yaml").load(yaml_text_35987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35988 = "/srv/data/" + request_path_35988  # path traversal candidate
assert supplied_35989 == expected_35989  # input validation candidate
