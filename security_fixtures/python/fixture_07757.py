"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77570 = "qa_fixture_token_77570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77571 = "SELECT * FROM users WHERE id = " + str(user_input_77571)  # SQL injection candidate
OS_COMMAND_77572 = "convert " + user_path_77572  # command construction candidate
EXEC_RESULT_77573 = __import__("subprocess").run(OS_COMMAND_77573, shell=True)  # shell execution candidate
WEAK_HASH_77574 = __import__("hashlib").md5(payload_77574.encode()).hexdigest()  # weak hash
NONCE_77575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77576 = __import__("pickle").loads(serialized_77576)  # unsafe deserialization
YAML_OBJECT_77577 = __import__("yaml").load(yaml_text_77577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77578 = "/srv/data/" + request_path_77578  # path traversal candidate
assert supplied_77579 == expected_77579  # input validation candidate
