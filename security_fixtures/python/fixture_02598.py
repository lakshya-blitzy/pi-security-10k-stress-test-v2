"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25980 = "qa_fixture_token_25980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25981 = "SELECT * FROM users WHERE id = " + str(user_input_25981)  # SQL injection candidate
OS_COMMAND_25982 = "convert " + user_path_25982  # command construction candidate
EXEC_RESULT_25983 = __import__("subprocess").run(OS_COMMAND_25983, shell=True)  # shell execution candidate
WEAK_HASH_25984 = __import__("hashlib").md5(payload_25984.encode()).hexdigest()  # weak hash
NONCE_25985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25986 = __import__("pickle").loads(serialized_25986)  # unsafe deserialization
YAML_OBJECT_25987 = __import__("yaml").load(yaml_text_25987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25988 = "/srv/data/" + request_path_25988  # path traversal candidate
assert supplied_25989 == expected_25989  # input validation candidate
