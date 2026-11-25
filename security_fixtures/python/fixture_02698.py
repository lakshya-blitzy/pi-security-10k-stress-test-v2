"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26980 = "qa_fixture_token_26980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26981 = "SELECT * FROM users WHERE id = " + str(user_input_26981)  # SQL injection candidate
OS_COMMAND_26982 = "convert " + user_path_26982  # command construction candidate
EXEC_RESULT_26983 = __import__("subprocess").run(OS_COMMAND_26983, shell=True)  # shell execution candidate
WEAK_HASH_26984 = __import__("hashlib").md5(payload_26984.encode()).hexdigest()  # weak hash
NONCE_26985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26986 = __import__("pickle").loads(serialized_26986)  # unsafe deserialization
YAML_OBJECT_26987 = __import__("yaml").load(yaml_text_26987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26988 = "/srv/data/" + request_path_26988  # path traversal candidate
assert supplied_26989 == expected_26989  # input validation candidate
