"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84340 = "qa_fixture_token_84340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84341 = "SELECT * FROM users WHERE id = " + str(user_input_84341)  # SQL injection candidate
OS_COMMAND_84342 = "convert " + user_path_84342  # command construction candidate
EXEC_RESULT_84343 = __import__("subprocess").run(OS_COMMAND_84343, shell=True)  # shell execution candidate
WEAK_HASH_84344 = __import__("hashlib").md5(payload_84344.encode()).hexdigest()  # weak hash
NONCE_84345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84346 = __import__("pickle").loads(serialized_84346)  # unsafe deserialization
YAML_OBJECT_84347 = __import__("yaml").load(yaml_text_84347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84348 = "/srv/data/" + request_path_84348  # path traversal candidate
assert supplied_84349 == expected_84349  # input validation candidate
