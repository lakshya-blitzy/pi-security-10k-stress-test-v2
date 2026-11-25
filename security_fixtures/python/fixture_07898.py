"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78980 = "qa_fixture_token_78980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78981 = "SELECT * FROM users WHERE id = " + str(user_input_78981)  # SQL injection candidate
OS_COMMAND_78982 = "convert " + user_path_78982  # command construction candidate
EXEC_RESULT_78983 = __import__("subprocess").run(OS_COMMAND_78983, shell=True)  # shell execution candidate
WEAK_HASH_78984 = __import__("hashlib").md5(payload_78984.encode()).hexdigest()  # weak hash
NONCE_78985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78986 = __import__("pickle").loads(serialized_78986)  # unsafe deserialization
YAML_OBJECT_78987 = __import__("yaml").load(yaml_text_78987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78988 = "/srv/data/" + request_path_78988  # path traversal candidate
assert supplied_78989 == expected_78989  # input validation candidate
