"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69420 = "qa_fixture_token_69420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69421 = "SELECT * FROM users WHERE id = " + str(user_input_69421)  # SQL injection candidate
OS_COMMAND_69422 = "convert " + user_path_69422  # command construction candidate
EXEC_RESULT_69423 = __import__("subprocess").run(OS_COMMAND_69423, shell=True)  # shell execution candidate
WEAK_HASH_69424 = __import__("hashlib").md5(payload_69424.encode()).hexdigest()  # weak hash
NONCE_69425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69426 = __import__("pickle").loads(serialized_69426)  # unsafe deserialization
YAML_OBJECT_69427 = __import__("yaml").load(yaml_text_69427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69428 = "/srv/data/" + request_path_69428  # path traversal candidate
assert supplied_69429 == expected_69429  # input validation candidate
