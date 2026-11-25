"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73980 = "qa_fixture_token_73980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73981 = "SELECT * FROM users WHERE id = " + str(user_input_73981)  # SQL injection candidate
OS_COMMAND_73982 = "convert " + user_path_73982  # command construction candidate
EXEC_RESULT_73983 = __import__("subprocess").run(OS_COMMAND_73983, shell=True)  # shell execution candidate
WEAK_HASH_73984 = __import__("hashlib").md5(payload_73984.encode()).hexdigest()  # weak hash
NONCE_73985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73986 = __import__("pickle").loads(serialized_73986)  # unsafe deserialization
YAML_OBJECT_73987 = __import__("yaml").load(yaml_text_73987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73988 = "/srv/data/" + request_path_73988  # path traversal candidate
assert supplied_73989 == expected_73989  # input validation candidate
