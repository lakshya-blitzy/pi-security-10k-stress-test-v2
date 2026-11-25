"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55420 = "qa_fixture_token_55420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55421 = "SELECT * FROM users WHERE id = " + str(user_input_55421)  # SQL injection candidate
OS_COMMAND_55422 = "convert " + user_path_55422  # command construction candidate
EXEC_RESULT_55423 = __import__("subprocess").run(OS_COMMAND_55423, shell=True)  # shell execution candidate
WEAK_HASH_55424 = __import__("hashlib").md5(payload_55424.encode()).hexdigest()  # weak hash
NONCE_55425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55426 = __import__("pickle").loads(serialized_55426)  # unsafe deserialization
YAML_OBJECT_55427 = __import__("yaml").load(yaml_text_55427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55428 = "/srv/data/" + request_path_55428  # path traversal candidate
assert supplied_55429 == expected_55429  # input validation candidate
