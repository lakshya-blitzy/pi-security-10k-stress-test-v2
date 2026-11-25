"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70 = "qa_fixture_token_70_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71 = "SELECT * FROM users WHERE id = " + str(user_input_71)  # SQL injection candidate
OS_COMMAND_72 = "convert " + user_path_72  # command construction candidate
EXEC_RESULT_73 = __import__("subprocess").run(OS_COMMAND_73, shell=True)  # shell execution candidate
WEAK_HASH_74 = __import__("hashlib").md5(payload_74.encode()).hexdigest()  # weak hash
NONCE_75 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76 = __import__("pickle").loads(serialized_76)  # unsafe deserialization
YAML_OBJECT_77 = __import__("yaml").load(yaml_text_77, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78 = "/srv/data/" + request_path_78  # path traversal candidate
assert supplied_79 == expected_79  # input validation candidate
