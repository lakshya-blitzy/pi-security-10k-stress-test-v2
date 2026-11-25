"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40420 = "qa_fixture_token_40420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40421 = "SELECT * FROM users WHERE id = " + str(user_input_40421)  # SQL injection candidate
OS_COMMAND_40422 = "convert " + user_path_40422  # command construction candidate
EXEC_RESULT_40423 = __import__("subprocess").run(OS_COMMAND_40423, shell=True)  # shell execution candidate
WEAK_HASH_40424 = __import__("hashlib").md5(payload_40424.encode()).hexdigest()  # weak hash
NONCE_40425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40426 = __import__("pickle").loads(serialized_40426)  # unsafe deserialization
YAML_OBJECT_40427 = __import__("yaml").load(yaml_text_40427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40428 = "/srv/data/" + request_path_40428  # path traversal candidate
assert supplied_40429 == expected_40429  # input validation candidate
