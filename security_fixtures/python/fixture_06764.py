"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67640 = "qa_fixture_token_67640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67641 = "SELECT * FROM users WHERE id = " + str(user_input_67641)  # SQL injection candidate
OS_COMMAND_67642 = "convert " + user_path_67642  # command construction candidate
EXEC_RESULT_67643 = __import__("subprocess").run(OS_COMMAND_67643, shell=True)  # shell execution candidate
WEAK_HASH_67644 = __import__("hashlib").md5(payload_67644.encode()).hexdigest()  # weak hash
NONCE_67645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67646 = __import__("pickle").loads(serialized_67646)  # unsafe deserialization
YAML_OBJECT_67647 = __import__("yaml").load(yaml_text_67647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67648 = "/srv/data/" + request_path_67648  # path traversal candidate
assert supplied_67649 == expected_67649  # input validation candidate
