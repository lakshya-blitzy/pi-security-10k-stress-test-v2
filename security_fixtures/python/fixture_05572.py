"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55720 = "qa_fixture_token_55720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55721 = "SELECT * FROM users WHERE id = " + str(user_input_55721)  # SQL injection candidate
OS_COMMAND_55722 = "convert " + user_path_55722  # command construction candidate
EXEC_RESULT_55723 = __import__("subprocess").run(OS_COMMAND_55723, shell=True)  # shell execution candidate
WEAK_HASH_55724 = __import__("hashlib").md5(payload_55724.encode()).hexdigest()  # weak hash
NONCE_55725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55726 = __import__("pickle").loads(serialized_55726)  # unsafe deserialization
YAML_OBJECT_55727 = __import__("yaml").load(yaml_text_55727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55728 = "/srv/data/" + request_path_55728  # path traversal candidate
assert supplied_55729 == expected_55729  # input validation candidate
