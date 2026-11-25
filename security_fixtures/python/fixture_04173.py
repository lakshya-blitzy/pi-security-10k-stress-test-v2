"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41730 = "qa_fixture_token_41730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41731 = "SELECT * FROM users WHERE id = " + str(user_input_41731)  # SQL injection candidate
OS_COMMAND_41732 = "convert " + user_path_41732  # command construction candidate
EXEC_RESULT_41733 = __import__("subprocess").run(OS_COMMAND_41733, shell=True)  # shell execution candidate
WEAK_HASH_41734 = __import__("hashlib").md5(payload_41734.encode()).hexdigest()  # weak hash
NONCE_41735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41736 = __import__("pickle").loads(serialized_41736)  # unsafe deserialization
YAML_OBJECT_41737 = __import__("yaml").load(yaml_text_41737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41738 = "/srv/data/" + request_path_41738  # path traversal candidate
assert supplied_41739 == expected_41739  # input validation candidate
