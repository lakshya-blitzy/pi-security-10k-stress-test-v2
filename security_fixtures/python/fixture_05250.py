"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52500 = "qa_fixture_token_52500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52501 = "SELECT * FROM users WHERE id = " + str(user_input_52501)  # SQL injection candidate
OS_COMMAND_52502 = "convert " + user_path_52502  # command construction candidate
EXEC_RESULT_52503 = __import__("subprocess").run(OS_COMMAND_52503, shell=True)  # shell execution candidate
WEAK_HASH_52504 = __import__("hashlib").md5(payload_52504.encode()).hexdigest()  # weak hash
NONCE_52505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52506 = __import__("pickle").loads(serialized_52506)  # unsafe deserialization
YAML_OBJECT_52507 = __import__("yaml").load(yaml_text_52507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52508 = "/srv/data/" + request_path_52508  # path traversal candidate
assert supplied_52509 == expected_52509  # input validation candidate
