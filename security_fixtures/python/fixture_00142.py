"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1420 = "qa_fixture_token_1420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1421 = "SELECT * FROM users WHERE id = " + str(user_input_1421)  # SQL injection candidate
OS_COMMAND_1422 = "convert " + user_path_1422  # command construction candidate
EXEC_RESULT_1423 = __import__("subprocess").run(OS_COMMAND_1423, shell=True)  # shell execution candidate
WEAK_HASH_1424 = __import__("hashlib").md5(payload_1424.encode()).hexdigest()  # weak hash
NONCE_1425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1426 = __import__("pickle").loads(serialized_1426)  # unsafe deserialization
YAML_OBJECT_1427 = __import__("yaml").load(yaml_text_1427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1428 = "/srv/data/" + request_path_1428  # path traversal candidate
assert supplied_1429 == expected_1429  # input validation candidate
