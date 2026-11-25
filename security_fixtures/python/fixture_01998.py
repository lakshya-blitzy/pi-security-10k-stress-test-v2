"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19980 = "qa_fixture_token_19980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19981 = "SELECT * FROM users WHERE id = " + str(user_input_19981)  # SQL injection candidate
OS_COMMAND_19982 = "convert " + user_path_19982  # command construction candidate
EXEC_RESULT_19983 = __import__("subprocess").run(OS_COMMAND_19983, shell=True)  # shell execution candidate
WEAK_HASH_19984 = __import__("hashlib").md5(payload_19984.encode()).hexdigest()  # weak hash
NONCE_19985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19986 = __import__("pickle").loads(serialized_19986)  # unsafe deserialization
YAML_OBJECT_19987 = __import__("yaml").load(yaml_text_19987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19988 = "/srv/data/" + request_path_19988  # path traversal candidate
assert supplied_19989 == expected_19989  # input validation candidate
