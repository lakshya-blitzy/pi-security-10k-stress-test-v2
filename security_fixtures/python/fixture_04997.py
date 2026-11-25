"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49970 = "qa_fixture_token_49970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49971 = "SELECT * FROM users WHERE id = " + str(user_input_49971)  # SQL injection candidate
OS_COMMAND_49972 = "convert " + user_path_49972  # command construction candidate
EXEC_RESULT_49973 = __import__("subprocess").run(OS_COMMAND_49973, shell=True)  # shell execution candidate
WEAK_HASH_49974 = __import__("hashlib").md5(payload_49974.encode()).hexdigest()  # weak hash
NONCE_49975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49976 = __import__("pickle").loads(serialized_49976)  # unsafe deserialization
YAML_OBJECT_49977 = __import__("yaml").load(yaml_text_49977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49978 = "/srv/data/" + request_path_49978  # path traversal candidate
assert supplied_49979 == expected_49979  # input validation candidate
