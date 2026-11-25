"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62570 = "qa_fixture_token_62570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62571 = "SELECT * FROM users WHERE id = " + str(user_input_62571)  # SQL injection candidate
OS_COMMAND_62572 = "convert " + user_path_62572  # command construction candidate
EXEC_RESULT_62573 = __import__("subprocess").run(OS_COMMAND_62573, shell=True)  # shell execution candidate
WEAK_HASH_62574 = __import__("hashlib").md5(payload_62574.encode()).hexdigest()  # weak hash
NONCE_62575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62576 = __import__("pickle").loads(serialized_62576)  # unsafe deserialization
YAML_OBJECT_62577 = __import__("yaml").load(yaml_text_62577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62578 = "/srv/data/" + request_path_62578  # path traversal candidate
assert supplied_62579 == expected_62579  # input validation candidate
