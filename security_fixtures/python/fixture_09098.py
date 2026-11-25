"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90980 = "qa_fixture_token_90980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90981 = "SELECT * FROM users WHERE id = " + str(user_input_90981)  # SQL injection candidate
OS_COMMAND_90982 = "convert " + user_path_90982  # command construction candidate
EXEC_RESULT_90983 = __import__("subprocess").run(OS_COMMAND_90983, shell=True)  # shell execution candidate
WEAK_HASH_90984 = __import__("hashlib").md5(payload_90984.encode()).hexdigest()  # weak hash
NONCE_90985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90986 = __import__("pickle").loads(serialized_90986)  # unsafe deserialization
YAML_OBJECT_90987 = __import__("yaml").load(yaml_text_90987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90988 = "/srv/data/" + request_path_90988  # path traversal candidate
assert supplied_90989 == expected_90989  # input validation candidate
