"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36730 = "qa_fixture_token_36730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36731 = "SELECT * FROM users WHERE id = " + str(user_input_36731)  # SQL injection candidate
OS_COMMAND_36732 = "convert " + user_path_36732  # command construction candidate
EXEC_RESULT_36733 = __import__("subprocess").run(OS_COMMAND_36733, shell=True)  # shell execution candidate
WEAK_HASH_36734 = __import__("hashlib").md5(payload_36734.encode()).hexdigest()  # weak hash
NONCE_36735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36736 = __import__("pickle").loads(serialized_36736)  # unsafe deserialization
YAML_OBJECT_36737 = __import__("yaml").load(yaml_text_36737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36738 = "/srv/data/" + request_path_36738  # path traversal candidate
assert supplied_36739 == expected_36739  # input validation candidate
