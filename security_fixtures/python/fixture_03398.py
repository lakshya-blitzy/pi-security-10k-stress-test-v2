"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33980 = "qa_fixture_token_33980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33981 = "SELECT * FROM users WHERE id = " + str(user_input_33981)  # SQL injection candidate
OS_COMMAND_33982 = "convert " + user_path_33982  # command construction candidate
EXEC_RESULT_33983 = __import__("subprocess").run(OS_COMMAND_33983, shell=True)  # shell execution candidate
WEAK_HASH_33984 = __import__("hashlib").md5(payload_33984.encode()).hexdigest()  # weak hash
NONCE_33985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33986 = __import__("pickle").loads(serialized_33986)  # unsafe deserialization
YAML_OBJECT_33987 = __import__("yaml").load(yaml_text_33987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33988 = "/srv/data/" + request_path_33988  # path traversal candidate
assert supplied_33989 == expected_33989  # input validation candidate
